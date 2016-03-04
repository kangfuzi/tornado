chedan
Data_ware configure
=========
# 安装 mongodb
* 在/etc/yum.repos.d/目录下新建一个10gen.repo文件，加入以下内容：
  [10gen]
  name=10gen Repository
  baseurl=http://downloads-distro.mongodb.org/repo/redhat/os/x86_64
  gpgcheck=0
* 执行 sudo yum update 更新 yum
* 执行 sudo yum install mongo-10gen 安装客户端
* 执行 sudo yum install mongo-10gen-server 安装服务器端
* 执行 sudo service mongod start 启动 mongodb

# 安装pip
* easy_install -i http://pypi.douban.com/simple pip
* 其他方式安装（）

# 依赖 安装
* redis(pip install redis)
* Celery(pip install celery)
* Rabbitmq(brew rabbitmq)
* tcelery(pip install Tornado-celery)
* Tornado(pip install tornado)
* Jinja2(pip install Jinja2)
* pymongo(pip install pymongo)

* supervisor (brew supervisor)

# 第一种启动方式： 运行
* 启动rabbitmq-server
* 启动redis-server
* 启动mongodb
* 第一次运行请导入用户数据库，默认是13800138000密码kangfuzi1231!
    `mongo db.js`
* 启动celery(在仓库文件夹下运行celery -A handlers worker --app=handlers.tasks -l info)
* 启动python server.py
* 访问 http:/localhost:8999


# 用supervisor来控制启动
* 启动rabbitmq-server
* 启动redis-server
* 启动mongod
* 配置supervisor.conf
* 启动supervisor -c /etc/supervisor.conf
* 第一次运行请导入用户数据库，默认时13800138000密码kangfuzi1231!
    `mongo db.js`
* 访问 http:/localhost:8999


# 配置supervisor.conf
* supervisor安装：sudo pip install supervisor
* 配置根据自己需要做相应改动！
	[program:celery]
	command=celery worker --app=handlers.tasks -l info
	directory=/Users/kangfuzi/Documents/wangtao/gitServer/data_warehouse
	user=kangfuzi
	stdout_logfile=/tmp/celery.log
	stderr_logfile=/tmp/celery.log
	autostart=true
	autorestart=true
	startsecs=10
	[program:dataManager]
	command=python /Users/kangfuzi/Documents/wangtao/gitServer/data_warehouse/service.py
	user=kangfuzi
	stdout_file=/tmp/dataManager.log
	stderr_file=/tmp/dataManager.log
	autorestart=true


# mongodb启动方式
* mongodb 的开启需要先开启服务端，在打开客户端
		
		服务端的开启方法：
			找到mongodb的安装路径：  /usr/local/Cellar/mongodb/3.0.5/bin/
			开启服务：  	./mongod —dbpath=/usr/local/var/mongodb
		客户端开启的方法：  直接输入：  mongo   (mongo就行了)

		服务停止的方法： 
			在客户端输入（建议）：	
				use admin
				db.shutdownServer()
			也可以：
				mongod —shutdown —dbpath=/usr/local/var/mongodb


* mongod.conf  路径   /usr/local/etc/mongod.conf
