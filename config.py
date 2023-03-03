import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'cmsstoragepython'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'E6dztiYDlow4Dut1tl+lsVsh6RyZWI0R9B1Yi8XnnhxZ4C5GqCosFAKPpH3Sbt8slOlDK+u18t0x+AStSAqw9g=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'cmsprojectserver.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'CMSDB'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'CMS'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'Godfather2403'

    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    CLIENT_SECRET = "on38Q~nEl8bangcEBXO.CrvSNpf-pEWSUHDNRcF9"
 
    AUTHORITY = "https://login.microsoftonline.com/common"

    CLIENT_ID = "e3a1457f-3fef-4bc4-899b-2b5ae6ab3748"

    REDIRECT_PATH = "/getAToken"


    SCOPE = ["User.Read"] 

    SESSION_TYPE = "filesystem"