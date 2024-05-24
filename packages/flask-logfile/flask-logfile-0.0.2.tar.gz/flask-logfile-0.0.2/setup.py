from setuptools import setup

'''
安装Twine： 
    # pip install twine

打包发布：
    1.修改setup.py文件版本号
    2.删除历史发布目录dist、build
    3.使用setuptools打包: 
        # python setup.py sdist
        # python setup.py install 
    4.使用twine发布到pypi:
        # python -m twine upload dist/* 
    
参考文档：
    https://setuptools.readthedocs.io/en/latest/references/keywords.html
    https://packaging.python.org/tutorials/packaging-projects/#setup-args
    https://blog.csdn.net/xujing19920814/article/details/80374360

备注：
    需要setuptools工具配合twine工具才能使用markdown文档

快速上传：
    python pypi.py
'''

desc_doc = 'README.md'

setup(
    name='flask-logfile',
    version='0.0.2',
    author='wall-1',
    url='https://github.com/WALL-1/flask-logfile.git',
    packages=['flask_logfile'],
    install_requires=[
        'flask',
        'logzero'
    ],
    description='一个高可用的Flask日志文件插件',
    long_description_content_type='text/markdown',
    long_description=open(desc_doc, encoding='utf-8').read(),
)
