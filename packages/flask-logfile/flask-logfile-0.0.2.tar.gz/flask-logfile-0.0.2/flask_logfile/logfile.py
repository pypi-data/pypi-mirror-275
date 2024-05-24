'''
Author: Jinghe Lee
Date: 2024-05-20 19:10:57
Editor: Visual Studio Code
'''
import os

from flask import Flask
from flask.logging import default_handler
from logging import DEBUG,getLogger, StreamHandler, Formatter
from logging.handlers import TimedRotatingFileHandler
from logzero import LogFormatter


class LogFile:
    DEFAULT_LOG_LEVEL = DEBUG

    DEFAULT_LOG_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
    DEFAULT_LOG_STREAM_FORMAT = \
        '[%(asctime)s|%(name)s|%(filename)s:%(lineno)d] %(color)s[%(levelname)s]%(end_color)s: %(color)s%(message)s%(end_color)s'

    DEFAULT_LOG_FILE = 'logs/flask.log'
    DEFAULT_LOG_FILE_ENCODING = 'utf8'
    DEFAULT_LOG_FILE_FORMAT = \
        '[%(asctime)s|%(name)s|%(filename)s:%(lineno)d] [%(levelname)s]: %(message)s'
    DEFAULT_LOG_FILE_SPLIT_UNIT = 'd'
    DEFAULT_LOG_FILE_SPLIT_INTERVAL = 1
    DEFAULT_LOG_FILE_BACKUP_COUNT = 0

    def __init__(self, app: Flask = None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask):
        config = app.config
        # 日志等级配置
        log_level = config.get(
            'LOG_LEVEL', LogFile.DEFAULT_LOG_LEVEL)
        # 日志日期格式
        date_format = config.get(
            'LOG_DATE_FORMAT', LogFile.DEFAULT_LOG_DATE_FORMAT)
        # 控制台日志格式
        stream_format = config.get(
            'LOG_STREAM_FORMAT', LogFile.DEFAULT_LOG_STREAM_FORMAT)

        # 日志文件路径
        log_file = config.get('LOG_FILE', LogFile.DEFAULT_LOG_FILE)
        # 文件日志格式
        log_file_format = config.get(
            'LOG_FILE_FORMAT', LogFile.DEFAULT_LOG_FILE_FORMAT)
        # 日志文件编码
        log_file_encoding = config.get(
            'LOG_FILE_ENCODING', LogFile.DEFAULT_LOG_FILE_ENCODING)
        # 日志文件日期拆分单位（日、时、分、秒 对应 d、h、m、s）
        log_file_split_unit = config.get(
            'LOG_FILE_SPLIT_UNIT', LogFile.DEFAULT_LOG_FILE_SPLIT_UNIT)
        # 间隔多久拆分一次
        log_file_split_interval = config.get(
            'LOG_FILE_SPLIT_INTERVAL', LogFile.DEFAULT_LOG_FILE_SPLIT_INTERVAL)
        # 日志文件备份数
        log_file_backup_count = config.get(
            'LOG_FILE_BACKUP_COUNT', LogFile.DEFAULT_LOG_FILE_BACKUP_COUNT)

        # 创建日志目录
        log_dir, _ = os.path.split(log_file)
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # 控制台日志监听器
        stream_formatter = LogFormatter(fmt=stream_format, datefmt=date_format)
        stream_handler = StreamHandler()
        stream_handler.setFormatter(stream_formatter)

        # 日志文件监听器
        file_formatter = Formatter(fmt=log_file_format, datefmt=date_format)
        file_handler = TimedRotatingFileHandler(
            filename=log_file,
            encoding=log_file_encoding,
            when=log_file_split_unit,
            interval=log_file_split_interval,
            backupCount=log_file_backup_count)
        file_handler.setFormatter(file_formatter)

        # 更换日志监听器
        # app.logger.removeHandler(default_handler)
        # app.logger.addHandler(stream_handler)
        # app.logger.addHandler(file_handler)
        # app.logger.setLevel(log_level)
        # app.logger.handlers.clear()

        root_loggr = getLogger()
        root_loggr.removeHandler(default_handler)
        root_loggr.addHandler(stream_handler)
        root_loggr.addHandler(file_handler)
        root_loggr.setLevel(log_level)

        if not isinstance(app.extensions,dict):
            app.extensions = dict()
        app.extensions['logfile'] = self
