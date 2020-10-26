from abc import ABC, abstractmethod

from app.environment import is_prod


class Config(ABC):

    @property
    @abstractmethod
    def SQLALCHEMY_DATABASE_URI(self):
        return "{}+{}://{}:{}@{}:{}/{}".format(
            self.DIALECT,
            self.DRIVER,
            self.USER,
            self.PASSWORD,
            self.HOST,
            self.PORT,
            self.DATABASE,
        )


class ProductionConfig(Config):

    # Flask Config
    DEBUG = False
    TESTING = False
    SECRET_KEY = ""

    # ORM Config
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # DB connection settings
    USER = ""
    PASSWORD = ""
    DIALECT = ""
    DRIVER = ""
    PORT = ""
    DATABASE = ""
    HOST = ""

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        return "{}+{}://{}:{}@{}:{}/{}".format(
            self.DIALECT,
            self.DRIVER,
            self.USER,
            self.PASSWORD,
            self.HOST,
            self.PORT,
            self.DATABASE,
        )


class DevelopmentConfig(Config):

    # Flask Config
    DEBUG = True
    SECRET_KEY = "mysecretkey"

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        return "sqlite:///development.sqlite3"


def environment_config() -> Config:
    if is_prod():
        return ProductionConfig()
    return DevelopmentConfig()
