# dftogsheet
A Python module for writing pandas DataFrame objects directly to Google Spreadsheets

## Install dftogsheet
```shell
$ pip install dftogsheet
```

## Setup
1. Enable the
[Google Sheets API](https://developers.google.com/sheets/api/quickstart/python).
2. Enter a name for your project. This is the name that will be displayed when your
app asks for permission to edit your spreadsheets in Google Drive later.
2. Download `credentials.json` into `project-root-folder/.dftogsheet/credentials/` folder.

## Simple Usage
```python
import pandas as pd
import dftogsheet

data_frame = pd.DataFrame()
dftogsheet.write_to_sheet(data_frame, spreadsheet_id, sheet_name)
```

### Parameters
There are three mandatory parameters for the above function:
- `data_frame` is any pandas DataFrame object.
- `spreadsheet_id` is the part of the Google Spreadsheet URL
that is between `/d/` and `/edit`.
- `sheet_name` is the name of the sheet within the Google spreadsheet.
E.g. `Sheet1`.

## Advanced usage
With only the above function, this library pretty much only does one thing.
But there is actually a lot more flexibility provided to you if you know what's going on.
Please look into the two functions in `dftogsheets/__init__.py` to understand what is going on
under the hood when you run the above code and to understand how you can use the `Sheet` class
and its methods more powerfully. If you have any suggestions, you are always more than welcome
to [contribute](#how-can-i-contribute) ;)

### Changing scopes, valueInputOption, and location of credentials file
What is the valueInputOption?
Read [this page](https://developers.google.com/sheets/api/reference/rest/v4/ValueInputOption) \
\
These settings are actually controlled by the `Config` class. A new instance of the `Config` class
with default values is created for you in `dftogsheet.write_section_to_sheet` so you don't have to
think about it for the sample code above. However, it is possible to fully customize
these configurations by creating your own `config` object for your project.
Please look into `dftogheets/config.py` to understand how you can do that.


## What's new in version 0.0.5
- Move location of credential files