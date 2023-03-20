import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'cmsblobudacity'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'l97xWhJmKpi0XzhDWjknh14w+qAXDFECFx402/oxw+Aghfsz143gIeTOh5UDuuvUWkiNxsYQqea3+ASt3l+wzA=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images1'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'udacitycmsserver2.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'CMS'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'cmsAdmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'Sako8338%'

    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    CLIENT_SECRET = "Ct28Q~wuQCMA3gCXvTq0Q7xp9iVZWja1pzoqoa~2"
 
    AUTHORITY = "https://login.microsoftonline.com/common"

    CLIENT_ID = "1ba68d31-f9d5-49e2-857d-555fe631928a"

    REDIRECT_PATH = "/getAToken"

    SCOPE = ["User.Read"] 

    SESSION_TYPE = "filesystem"