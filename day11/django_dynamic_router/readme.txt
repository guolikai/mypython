该实例通过反射机制实现Django的动态路由

主要代码实现
1、url.py
	配置url映射
2、activator.py
	根据url中获取的参数，通过反射调用指定 app/view.py 中的函数

如：

http://127.0.0.1:9000/app01/index/	==》 执行app01/view.py文件中的index函数

http://127.0.0.1:9000/app02/index/	==》 执行app02/view.py文件中的index函数

http://127.0.0.1:9000/app01/login/	==》 执行app01/view.py文件中的login函数


