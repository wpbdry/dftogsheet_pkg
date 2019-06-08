import os.path
import json

'''
Default configurations:
'''
# If modifying these scopes, delete the file token.pickle.
scopes = ['https://www.googleapis.com/auth/spreadsheets']

# Type of input
# Documentation https://developers.google.com/sheets/api/reference/rest/v4/ValueInputOption
value_input_option = 'RAW'

# Paths to credentials files
token = '.dftogsheet/credentials/token.pickle'
credentials = '.dftogsheet/credentials/credentials.json'

# Path to config file
with open('dftogsheet/config-location.json') as config_location:  
    config = json.load(config_location)['path']

'''
Set project specific variables if they exist
'''
if os.path.exists(config):
    with open(config) as config:
        project_config = json.load(config)
        try:
            scopes = project_config['scopes']
        except:
            pass
        try:
            value_input_option = project_config['valueInputOption']
        except:
            pass
        try:
            token = project_config['token']
        except:
            pass
        try:
            credentials = project_config['credentials']
        except:
            pass
