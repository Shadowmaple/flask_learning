# flask learning
___

# notes

## 概念
+ 路由：
    处理 URL 和函数之间关系的映射程序。

    客户端发送请求给web服务器，web服务器再将请求发送给Flask程序实例。程序实例需要知道每个url请求所对应的运行代码是谁。所以程序中必须要创建一个 url 请求地址 到 python运行函数的一个映射。
    
+ 视图函数：
    应用程序路由的处理逻辑。视图函数被映射到一个或多个路由URL，以便Flask知道当客户端请求给定的URL时执行什么逻辑。主要作用是生成请求的响应。
+ token：
    在计算机身份认证中是令牌（临时）的意思
+ ORM：
    Object Relational Mapping,对象关系映射,将数据库中的表与面向对象语言中的类建立了一种对应关系。这样，要操作数据库，数据库中的表或者表中的一条记录就可以直接通过操作类或者类实例来完成。

+ web：基于http、html的，全球性、动态交互、跨平台的提供存储、网页浏览的一种系统
+ 资源：任何可以被识别、被命名、或被处理的实体
+ cookie：指某些网站为了辨别用户身份而储存在用户本地终端（Client Side）上的数据（通常经过加密）
+ JSON：
 (JavaScript Object Notation)，JavaScript对象表示法，是一种轻量级的数据交换语言，该语言以易于让人阅读的文字为基础，用来传输由属性值或者序列性的值组成的数据对象，是JavaScript的一个子集，是独立于语言的文本格式
+ session：即会话，是两个或更多个通信设备之间或计算机和用户之间的临时和交互式信息交换
+ 进程，是指计算机中已运行的程序。进程本身不是基本运行单位，而是线程的容器。在用户空间中，进程是加载器根据程序头提供的信息将程序加载到内存并运行的实体。同一程序可产生多个进程（一对多关系），以允许同时有多位用户运行同一程序，却不会相冲突。
+ 线程，是操作系统能够进行运算调度的最小单位。一个进程可以有很多线程，每条线程并行执行不同的任务。
+ 时间戳（Timestamp）是指字符串或编码信息用于辨识记录下来的时间日期
+ 活跃用户：该用户的登录状态是否通过用户名密码登录，通过“记住我”功能保持登录状态的用户是非活跃的
+ stack trace（堆栈跟踪）
+ 一个类的实例被关联到同一个类的其他实例的关系被称为*自引用关系*
+ Moment.js是一个小型的JavaScript开源库，它将日期和时间转换成目前可以想象到的所有格式
+ 软件：是一系列按照特定顺序组织的计算机数据和指令的集合。简单的说软件就是程序加文档的集合体。以开发语言作为描述语言，可以认为：软件=程序+数据+文档



## 简记

 - 避免循环依赖
 - 使用`render_template()`必须要有`templates`目录，只能是这个名称，否则无法识别
 - 传入`render_template()`中的参数可以是字典，也可以是字符串
 - `flash()`函数将要展示的闪现信息存储在session中，通过`get_flashed_message()`获取
 - with语句可以创建新的内部范围。在此范围内设置的变量在范围之外不可见。
 - `validators`参数用于验证输入字段是否符合预期。
 - `DataRequired()`验证器仅验证字段输入是否为空。
 - jinjia2模板继承：`{% extends 'base.html' %}`
 - `form.hidden_tag()`模板参数生成了一个隐藏字段，其中包含一个用于保护表单免受CSRF攻击的token
  `{{ form.hidden_tag() }}`，如无，则不能有效提交表单（亲身试水）
 - html5的*novalidate*属性规定当提交表单时不对其进行验证。
 - 基本定义为**class**类的目的是为了将其转为实例化对象，方便运用，即ORM
 - 使用SCRF必须要先设置密钥`secret_key`
 - `form.validate_on_submit()`实例方法会执行form校验的工作。当浏览器发起GET请求的时候，它返回False；发起post请求时，则返回True
 - `os.path.dirname(__file__)`返回当前文件的上一目录
 - `flask.request.get_json()`解析并将数据作为JSON返回，返回的值是字典格式的
 - 运行shell上下文环境之前要设置环境变量
 - `validate_on_submit` 将会检查是否是一个 POST 请求并且请求是否有效
 - Post/Redirect/Get模式
 - Flask-SQLAlchemy的所有查询对象都支持`paginate`方法
```python
>>> user.followed_posts().paginate(1, 20, False).items
```
 - url_for()函数的一个有趣的地方是，你可以添加任何关键字参数，如果这些参数的名字没有直接在URL中匹配使用，那么Flask将它们设置为URL的查询字符串参数。
 - Flask-Moment依赖moment.js和jquery.js。使用bootstrap时则导入jquery.js
```
<html>
    <head>

        {{ moment.include_jquery() }}
        {{ moment.include_moment() }}

        <!--使用中文,默认是英语的-->
　　   {{ moment.lang("zh-CN") }} 
　　　　 
</head> <body> ... </body> </html>
```
>文档：http://www.cnblogs.com/agmcs/p/4446589.html

 - `os.system('cat errors.py')`：执行`cat errors.py`系统命令，如可行则返回0，否则为1
    ```
    >>> import os
    >>> os.system('cat errors.py') == 0
    ……(代码省略)
    
    True
    ```
 - flask的两种**上下文**：应用上下文，请求上下文

## 操作
+ 虚拟环境
    + 安装：`python3 -m venv venv1`
    + 激活：`source venv1/bin/activate`
    + 退出：`deactivate`
+ 安装flask：`pip3 install flask`
+ 设置环境变量：`export FLASK_APP=xxx.py`
+ 运行flask：`flask run`
+ 安装flask-sqlalchemy：`pip install flask-sqlalchemy`
+ 环境变量（总）
    + 设置：`vi ~/.bahrc`
    + 激活：`source .bashrc`
+ 查看pip下已安装的库：`pip3 list`
+ 执行
    + 前端：`sudo npm run serve`
    + 后端：`python3 manage.py runserver -p 6666`
+ 调试模式:
    + 更改环境变量：`export FLASK_DEBUG=1`
    + 重启服务：`flask run`


## 数据库
### 事先配置
先配置，两项必配
```
import os
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
```
之后再创建实例
```
db = SQLAlchemy(app)
```

### 数据库操作
|操作说明|操作方法 |
| ---|---|
|删除所有的表|db.drop_all()|
|创建所有的表| db.create_all() |
|添加数据| db.session.add(obj) |
|添加多个数据|db.session.add_all([obj1,obj2]) |
|提交| db.session.commit() |
|删除| db.session.delete(obj) |
|回滚| db.session.rollback() |

####实际操作
创建表
```
$ python3
>>> …… #省略导入
>>> db.create_all()
```
移除所有表：
```
>>> db.drop_all()
```

添加一个用户
```
>>> from app import db
>>> from app.model import User
>>> u = User(username='john', email='john@example.com')
>>> db.session.add(u)
>>> db.session.commit()
```
修改
```
# 第一种方法
>>> User.query().filter_by(username='abc').update({'name': '123'})
>>> session.commit()

# 第二种方法
>>> user = User.query.filter_by(username='abc').first()
>>> user.name = '223'
>>> session.commit()
```
删除
```
>>> db.session.delete(u)
>>> db.session.commit()
```
示例
```
>>> User.query.all() # User类没有创建`__repr__`方法，所以默认显示的是id（1，2……）
<User 1><User 2>
>>> User.query.get(1)
<User 1>
>>> User.query.get(1).username
'xyz'
>>> User.query.filter_by(username='xyz')
<flask_sqlalchemy.BaseQuery object at 0x7fd6ca0e8f28>
>>> User.query.filter_by(username='xyz').first()    # 查找获取对象，重点
<User 1>
>>> User.query.filter_by(username='xyz').first().password
'123'
>>> User.query.filter_by(username='xyz').first().id
1
```


### 数据库迁移
#### 准备条件
迁移插件：`flask-migrate`
创建实例：
```
from flask_migrate import Migrate
migrate = Migrate(app,db)
```
#### 运行操作
+ 第一种运行方式
    + 创建迁移存储库：`flask db init`
    + 自动迁移（注释）：`flask db migrate -m "users table"`
    + 将迁移脚本应用到数据库，即更新：`flask db upgrade`
    + 回滚上次迁移：`flask db downgrade`
+ 第二种方式
    + `python3 manage.py db init`   初始化数据库,会创建一个migations文件夹,并且会在数据库中生成一个alembic_version表 
    + `python3 manage.py db migrate`  创建迁移历史
    + `python3 manage.py db upgrade`  更新数据库
    + `python3 manage.py db downgrade`  回滚数据库

## 单元测试
### 代码实例
```
import unittest
from app import app, db
from app.models import User

class UserTest(unittest.TestCase):
    def setUp(self):
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all

    def test_user_login(self):
        u1 = User(userName='2332', name = 'Zhang', userId='afjdsiewwalj124kbkh32')
        u2 = User(userName='2333', name='Hao', userId='1234567890')
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()

        self.assertEqual(u1.userName, '2332')
        self.assertEqual(u2.name, 'Hao')
        self.assertTrue(u1.userName)

    def test_email_modify(self):
        u = User(userName='33')
        u.email = '2@qq.com'

        self.assertEqual(u.email, '2@qq.com')

if __name__ == '__main__':
    unittest.main(verbosity=2)
```
### 注意点
1. 在unittest.main()中加 verbosity 参数可以控制输出的错误报告的详细程度，默认是 1，如果设为 0，则不输出每一用例的执行结果，即没有上面的结果中的第1行；如果设为 2，则输出详细的执行结果
2. 每个测试的函数前必须以`test_*`为名，否则不会执行
3. 每次测试的关键是要求`assertEqual()`检查预期结果; `assertTrue()`或`assertFalse()`核实情况; 或`assertRaises()`验证是否引发了特定异常。使用这些方法代替`assert`语句，以便测试运行器可以累积所有测试结果并生成报告。

# 问题
+ 装饰器？在这里的作用？
+ `microblog.py`的作用？
+ 请求钩子
+ flash()
+ Jinja2？
+ app.config.from_object(Config)
+ class LoginForm(FlaskForm) 之类的继承
+ token？loginform类？
+ 出现提示

>    (venv1) lawler@maple:~/flask-try/app/templates$ [5517:5517:0121/095745.965368:ERROR:gcm_channel_status_request.cc(151)] GCM channel request failed.
[5517:5517:0121/095912.140323:ERROR:gcm_channel_status_request.cc(151)] GCM channel request failed.

+ 继承的object是怎么样的
>import os
>class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

+ 爬虫运用`requests.session()`的必要性
+ Lab是什么
+ `db.relationship()`
+ login = LoginManager(app)
+ url_parse()
+ `user_loader`用户加载函数
+  python的类方法，静态方法和实例方法
+  flask的g对象



# 要点

## 第九章 分页
+ Post/Redirect/Get模式
+ User类的`followed_posts()`方法
+ Flask-SQLAlchemy的`paginate()`方法
+ items属性：请求内容的数据列表
+ request.args.get()
+ has_next: 当前页之后存在后续页面时为真
+ has_prev: 当前页之前存在前置页面时为真
+ next_num: 下一页的页码
+ prev_num: 上一页的页码

## 第十章 邮件
+ flask-mail
+ JSON Web Tokens
+ 静态方法与类方法
+ external=True参数
+ 异步
+ 应用上下文和请求上下文

## 第十一章 日期和时间
+ Moment.js是一个小型的JavaScript开源库，它将日期和时间转换成目前可以想象到的所有格式
+ Flask-Moment
+ moment对象为不同的渲染选项提供了几种方法：format()，fromNow()和calendar()方法
+ Flask-Moment依赖moment.js和jquery.js。需要直接包含在HTML文档

## 第十二章 国际化和本地化
+ Click
+ flask-babel
+ lazy_gettext()，_()

## 第十六章 全文搜索


# SQLAlchemy列选项
[参考](https://blog.csdn.net/wuqing942274053/article/details/72511486)
|选项名	|说明|
| :---: | :---:|
| primary_key |	如果设为True，这列就是表的主键|
|unique | 如果设为True，这列不允许出现重复的值|
|index | 如果设为True，这列创建索引，提升查询效率|
|nullable |	如果设为True，这列允许使用空值；如果设为False，这列不允许使用空值|
|default |	为这列定义默认值|


