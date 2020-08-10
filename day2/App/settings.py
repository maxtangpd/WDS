import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

def get_db_uri(dbinfo):

    engine = dbinfo.get("ENGINE") or "sqlite"
    driver = dbinfo.get("DRIVER") or "sqlite"
    user = dbinfo.get("USER") or ""
    password = dbinfo.get("PASSWORD") or ""
    host = dbinfo.get("HOST") or "localhost"
    port = dbinfo.get("PORT") or ""
    name = dbinfo.get("NAME") or ""

    return "{}+{}://{}:{}@{}:{}/{}".format(engine, driver, user, password, host, port, name)

class Config:
    DEBUG = False

    TESTING = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False



class DevelopConfig(Config):

    DEBUG = True

    dbinfo ={
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "asdf1234qwer",
        "HOST": "LOCALHOST",
        "PORT": "3306",
        "NAME": "DAY2FLASK"
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


class TestConfig(Config):

    TESTING = True

    dbinfo ={
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "asdf1234qwer",
        "HOST": "LOCALHOST",
        "PORT": "3306",
        "NAME": "DAY2FLASK"
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


class StagingConfig(Config):

    dbinfo ={
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "asdf1234qwer",
        "HOST": "LOCALHOST",
        "PORT": "3306",
        "NAME": "DAY2FLASK"
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


class ProductConfig(Config):

    dbinfo ={
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "asdf1234qwer",
        "HOST": "LOCALHOST",
        "PORT": "3306",
        "NAME": "DAY2FLASK"
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)

envs = {
    "development": DevelopConfig,
    "testing": TestConfig,
    "staging": StagingConfig,
    "product": ProductConfig,
    "default": DevelopConfig
}