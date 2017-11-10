workers = 5 # 可以理解为进程数，会自动分配到你机器上的多CPU，完成简单并行化
worker_class = 'eventlet' # worker的类型，如何选择见：http://docs.gunicorn.org/en/stable/design.html#choosing-a-worker-type
bind = '0.0.0.0:5000' # 服务使用的端口
accesslog = '../logs/gunicorn.log' # 存放访问日志的位置，注意首先需要存在logs文件夹，才可自动创建log文件
errorlog = '../logs/gunicorn.log' # 存放错误日志的位置，可与访问日志相同
reload = False # 如果应用的代码有变动，work将会自动重启，适用于开发阶段
daemon = True # 是否后台运行
timeout = 5 # server端的请求超时秒数