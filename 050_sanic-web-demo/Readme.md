[toc]

# 1: sanic介绍
- 提到 API 开发，你可能会想到 Django REST Framework，Flask，FastAPI，没错，它们完全可以用来编写 API，不过，今天分享的这个框架可以让你更快把现有的函数转化为 API，它就是 Sanic。
- 是 Python3.7+ Web 服务器和 Web 框架，旨在提高性能。它允许使用 Python3.5 中添加的 async/await 语法，这可以有效避免阻塞从而达到提升响应速度的目的。Sanic致力于提供一种简单且快速，集创建和启动于一体的方法，来实现一个易于修改和拓展的 HTTP 服务，Sanic 具备开箱即用的功能，它可以用于编写，部署和扩展生产级 Web 应用程序。目前 Github 有 16.3k 的星，有广泛的社区支持
- **`sanic`**:https://github.com/sanic-org/sanic
- sanic Feature:
  - 内置极速 web server;
  - 生产准备就绪;
  - 极高的拓展性;
  - 简单直观的 API 设计;
  - 支持 ASGI;
# 2: 编写函数
`function.py`
# 3: 将函数转为web api

# 4: api接口测试
```bash
curl "http://localhost:8000/getdatetime"

curl "http://localhost:8000/getdatetime"


curl -X 'POST' 'http://localhost:8000/sumxy' -H "Content-Type: application/json" -d '{"x":10,"y":20}'
{"result":30}%
```