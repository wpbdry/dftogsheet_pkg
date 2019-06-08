import pandas as pd
import webbrowser
import dftogsheet


class Test:
    def __init__(
        self,
        spreadsheet_id='1aZPHi_54EN8AC6f5nrXTUauBgQG26MxHSv3iSUfby0w',
        spreadsheet_url='https://docs.google.com/spreadsheets/d/1aZPHi_54EN8AC6f5nrXTUauBgQG26MxHSv3iSUfby0w/edit#gid=0',
        sheet_name='Sheet1',
        data={
            'First Name': ['wpb', 'John', 'Lisa', '', 'Remember to delete this so you know whether the next test works!'],
            'Last Name': ['dry', 'Doe', 'Smith', '', ''],
            'Email': ['wpbdry@gmail.com', 'john.doe@example.tld', 'lisa@smith.com', '', '']
        }
    ):
        self.spreadsheet_id = spreadsheet_id
        self.spreadsheet_url = spreadsheet_url
        self.sheet = sheet_name
        if isinstance(data, dict):
            self.data = data
        else:
            raise AttributeError('Invalid data.')

    def run(self):
        print('Running test...')
        df = pd.DataFrame(data=self.data)
        dftogsheet.write_to_sheet(df, self.spreadsheet_id, self.sheet)
        webbrowser.open(self.spreadsheet_url)
        print('Test complete. Please check sucess in web browser.')


def test():
    test = Test()
    test.run()

# Run test
test()
