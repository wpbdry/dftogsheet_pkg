name = "dftogsheet"

from dftogsheet.auth import *
from dftogsheet.config import Config
from dftogsheet.sheet import *


def write_section_to_sheet(df_subsection, spreadsheet_id, sheet_name, offset=0):
    section = sheet.Sheet(df_subsection)
    section.unsupported_datatypes_tostr()
    section.set_range(sheet_name=sheet_name, offset=offset)
    config = Config()
    section.write(spreadsheet_id, config)


def write_to_sheet(df, spreadsheet_id, sheet_name):
    # Headers
    write_section_to_sheet(df.columns, spreadsheet_id, sheet_name)
    # Body
    write_section_to_sheet(df.values, spreadsheet_id, sheet_name, offset=1)
    