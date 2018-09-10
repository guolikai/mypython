http://www.cnblogs.com/nulige/p/6351318.html
1.一对一消息队列
2.消息订阅发布
Exchange的作用就是转发消息，给订阅者发消息。

Exchange在定义的时候是有类型的，以决定到底是哪些Queue符合条件，可以接收消息。
一共有四种类型:
    1、fanout: 所有bind到此exchange的queue都可以接收消息  （给所有人发消息）
    2、direct: 通过routingKey和exchange决定的哪一组queue可以接收消息 （给指定的一些queue发消息）
    3、topic（话题）:所有符合routingKey(此时可以是一个表达式)的routingKey所bind的queue可以接收消息 （给订阅话题的人发消息）
     表达式符号说明：#代表一个或多个字符，*代表任何字符
     示例：#.a会匹配a.a，aa.a，aaa.a等
          *.a会匹配a.a，b.a，c.a等
		  备注：使用RoutingKey为#，Exchange Type为topic的时候相当于使用fanout　
    4、headers: 通过headers 来决定把消息发给哪些queue  （通过消息头，决定发送给哪些队列）
2.1 广播
    适用场景:视频直播
2.2 组播

2.3 特定
    举例:收集MySQL的err日志
以上消息都是单向的,无法反馈给服务端。

3. 双向处理 rpc机制:
Remote Producre Call
远程 过程 调用
