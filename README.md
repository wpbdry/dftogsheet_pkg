# gsheets

## Install gsheets
```shell
$ cd project/root/folder
$ git clone https://github.com/wpbdry/gsheets.git
$ pip install -r gsheets/requirements.txt
```

## Setup
1. Enable the
[Google Sheets API](https://developers.google.com/sheets/api/quickstart/python)
for the Google account you'd like to use.

## Simple Usage
```python
import pandas as pd
from gsheets import gsheets

data_frame = pd.DataFrame()
gsheets.write_to_sheet(data_frame, spreadsheet_id, sheet_name)
```

### Parameters
There are three mandatory parameters for the above function:
- `data_frame` is any pandas DataFrame object.
- `spreadsheet_id` is the part of the Google Spreadsheet URL
that is between `/d/` and `/edit`.
- `sheet_name` is the name of the sheet within the Google spreadsheet.
E.g. `Sheet1`.