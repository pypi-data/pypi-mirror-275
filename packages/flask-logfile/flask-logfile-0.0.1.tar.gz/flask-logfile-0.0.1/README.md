# flask-logfile

一个高可用的Flask日志文件插件

## 安装

```
pip install flask_logfile
```

## 示例

```
from flask import Flask
from flask_logfile import LogFile

app = Flask(__name__)
LogFile().init_app(app)

app.logger.debug('debug')
app.logger.info('info')
app.logger.warning('warning')
app.logger.error('error')
```
