import click
import csv
import os
import sqlite_utils

@click.command()
@click.argument(
    "export_file",
    type=click.Path(exists=True, file_okay=True, dir_okay=False, allow_dash=False),
    required=True,
)
@click.argument(
    "db_path",
    type=click.Path(file_okay=True, dir_okay=False, allow_dash=False),
    required=True,
)
def cli(export_file, db_path):
    "Convert exported CSV from Visible app to a SQLite DB"
    db = sqlite_utils.Database(db_path)

    with open(export_file, newline='') as csvfile:
        csvreader = csv.DictReader(csvfile)
        csvreader.fieldnames[-1] = csvreader.fieldnames[-1].strip()
        for row in csvreader:
            db["Observations"].insert({
                "observation_date": row["observation_date"],
                "value": row["observation_value"],
                "tracker": db["Trackers"].lookup({
                    "name":  row["tracker_name"]
                },
                {"tracker_category": row["tracker_category"]},
                extracts={"tracker_category": "TrackerCategories"}),
            }, foreign_keys=[("tracker", "Trackers")])
