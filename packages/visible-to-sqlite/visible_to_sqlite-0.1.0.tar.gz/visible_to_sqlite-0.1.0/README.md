# visible-to-sqlite

*Convert exported CSV from the [Visible app](https://www.makevisible.com/) to a SQLite DB.*

Heavily inspired by [healthkit-to-sqlite](https://github.com/dogsheep/healthkit-to-sqlite) and the rest of the [Dogsheep](https://dogsheep.github.io/) family.  Designed to be explored with [Datasette](https://datasette.io/).

## Usage

Run: `visible-to-sqlite Visible_Data_Export.csv ./visible.db`

And then probably: `datasette ./visible.db`
