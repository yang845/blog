import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY') or 'it is a secret!'
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = int(os.getenv('MAIL_PORT','587'))
    MAIL_USERNAME = os.getenv('MAIL_USERNAME') or '1986436987@qq.com'
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD') or 'dtukgbkrniquedgi'
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in ['true', 'on', '1']
    MZ_MAIL_SUBJECT_PREFIX = '[MZBlog]'
    MZ_MAIL_SENDER = 'MZBlog Admin <1986436987@qq.com>'
    MZ_ADMIN = os.environ.get('MZ_ADMIN') or 'yang'
    MZ_PASSWORD = os.environ.get('MZ_PASSWORD') or '123456'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASKY_POSTS_PER_PAGE = 9
    FLASK_ADMIN_SWATCH = 'Paper'
    BABEL_DEFAULT_LOCALE = 'zh_Hans_CN'
    REMEMBER_COOKIE_DURATION = timedelta(days=10)

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    DIALECT = 'mysql'
    DRIVER = 'mysqlconnector'
    USERNAME = 'yang'
    PASSWORD = '971229'
    HOST = '127.0.0.1'
    PORT = '3306'
    DATABASE = 'development_db'
    SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8mb4".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST
                                                                           , PORT, DATABASE)

class TestingConfig(Config):
    DEBUG = True
    DIALECT = 'mysql'
    DRIVER = 'mysqlconnector'
    USERNAME = 'yang'
    PASSWORD = '971229'
    HOST = '127.0.0.1'
    PORT = '3306'
    DATABASE = 'test_db'
    SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8mb4".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST
                                                                           , PORT, DATABASE)

class ProductionConfig(Config):
    DIALECT = 'mysql'
    DRIVER = 'mysqlconnector'
    USERNAME = 'yang'
    PASSWORD = '971229'
    HOST = '127.0.0.1'
    PORT = '3306'
    DATABASE = 'mzblog_db'
    SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8mb4".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST
                                                                          , PORT, DATABASE)

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)

        # 出错时邮件通知管理员
        import logging
        from logging.handlers import SMTPHandler
        credentials = None
        secure = None
        if getattr(cls, 'MAIL_USERNAME', None) is not None:
            credentials = (cls.MAIL_USERNAME, cls.MAIL_PASSWORD)
            if getattr(cls, 'MAIL_USE_TLS', None):
                secure()
        mail_handler = SMTPHandler(
            mailhost=(cls.MAIL_SERVER, cls.MAIL_PORT),
            fromaddr=cls.MZ_MAIL_SENDER,
            toaddrs=[cls.MZ_ADMIN],
            subject=cls.MZ_MAIL_SUBJECT_PREFIX + 'Application Error',
            credentials=credentials,
            secure=secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)

class DockerConfig(ProductionConfig):

    @classmethod
    def init_app(cls, app):
        ProductionConfig.init_app(app)

        # 输出到stderr
        import logging
        from logging import StreamHandler
        file_headler = StreamHandler()
        file_headler.setLevel(logging.INFO)
        app.logger.addHandler(file_headler)

config = {
    'development':DevelopmentConfig,
    'testing':TestingConfig,
    'production':ProductionConfig,
    'docker':DockerConfig,
    'default':DevelopmentConfig
}
