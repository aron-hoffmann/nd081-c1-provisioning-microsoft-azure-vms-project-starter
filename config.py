import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = "1cae752e-e6b0-42c1-8214-f9196a3541c9"

    BLOB_ACCOUNT = "udacityspeicherkonto"
    BLOB_STORAGE_KEY = "mGyESsZrnOTcnoGhUIYnksMHGx9xo0jVa600xLSmKXfA531GK7IJWCchRlJo+HB1E7ypnB7x5rQn2Ol4Q4RQLg=="
    BLOB_CONTAINER = "imgs"

    SQL_SERVER = "udacityserverhoffi.database.windows.net"
    SQL_DATABASE = "udacity_database"
    SQL_USER_NAME = "hoffi"
    SQL_PASSWORD = "Cheat2win+1"
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    CLIENT_SECRET = "07fA50-Iz8cOo5siy_I._.vlvX1ItWd.Kw"
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    # CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    # if not CLIENT_SECRET:
    #     raise ValueError("Need to define CLIENT_SECRET environment variable")

    AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

    CLIENT_ID = "7b478353-397a-430b-8161-f2251e28325c"

    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session