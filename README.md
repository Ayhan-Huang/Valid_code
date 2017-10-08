# 验证码的生命周期
在web应用中，验证码常用于登录注册。验证码本质就是一张图片。
我们来看一下验证码的生命周期：
1. 客户端请求验证码
2. 服务端渲染验证码：
   -   渲染一张包含随机字符串的图片
   -   随机字符串写入session
   -   读取图片并返回响应
3. 客户端提交：
   -   显示响应（即验证码图片）
   -   获取用户输入字符串
   -   提交用户输入
4. 服务端验证：
   -   取出session中保存的随机字符串与用户提交的字符串进行对比
   -   字符串信息一致，进行下一步处理
   -   字符串信息不一致，返回错误信息

下面我们在Django中实践以上流程。