# flask-logfile

一个高可用的Flask日志文件插件

## 安装

```
pip install flask_logfile
```

## 示例

```
import logging

from flask import Flask
from flask_logfile import LogFile


app = Flask(__name__)

app.config['LOG_LEVEL'] = logging.INFO
app.config['LOG_FILE'] = '`logs/main.log`'

LogFile().init_app(app)

app.logger.debug('debug')
app.logger.info('info')
app.logger.warning('warning')
app.logger.error('error')
```

## 配置说明

| 配置变量                  | 功能说明                                                                                                 |
| ------------------------- | -------------------------------------------------------------------------------------------------------- |
| LOG_LEVEL                 | 日志等级，同logging模块，默认：`DEBUG`                                                                 |
| LOG_DATE_FORMAT           | 日志时间格式，默认：`%Y-%m-%d %H:%M:%S`                                                                |
| LOG_STREAM_FORMAT | 控制台日志格式，可参考[官方文档](https://docs.python.org/3.7/library/logging.html#logrecord-attributes)|
| LOG_FILE           | 日志文件路径，默认：`logs/flask.log`                                                                |
| LOG_FILE_ENCODING                 | 日志文件编码，默认：`utf8`                                                                 |
| LOG_FILE_FORMAT           | 日志文件日志格式，可参考[官方文档](https://docs.python.org/3.7/library/logging.html#logrecord-attributes)                                                                |
|LOG_FILE_SPLIT_UNIT                 | 日志文件拆分时间单位，默认：`d`（天）                                                               |
|FILE_SPLIT_INTERVAL           | 日志文件拆分间隔，默认：`1`个时间单元                                                         |
|LOG_FILE_BACKUP_COUNT                 | 日志文件备份数量，默认：0|
