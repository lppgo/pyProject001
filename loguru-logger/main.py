from loguru import logger
import sys 

# loguru 日志库
# https://github.com/Delgan/loguru?tab=readme-ov-file#features


# 1. 控制台输出
logger.remove(0)  # 移除默认的控制台输出
logger.add(sys.stderr, level="ERROR")  # 添加新的控制台输出，仅显示 ERROR 及以上级别的日志
logger.debug("debug info: x={x}",x=42)


# 2. 文件日志（每天滚动，保留 3 天，压缩为 zip）
logger.add(
    "app_{time:YYYY-MM-DD}.log",
    # rotation="00:00",
    rotation="500 MB",
    retention="3 days",
    compression="zip",
    enqueue=True, # 默认线程安全.使用队列，异步写入, Thread-safe,Multiprocess-safe
    backtrace=True, diagnose=True, # 异常回溯, 异常诊断
    format="{time:HH:mm:ss}|{level: <6}|{message}",
)

logger.info("info info: x={x}",x=42)

# 3. 捕获异常
@logger.catch(level="ERROR")
def risky_div(x):
    return 10 / x

risky_div(0)

# 4. 结构化日志
logger.add("data.json",serialize=True)
ctx = logger.bind(user="lucas", ip="10.0.0.1")
ctx.info("用户登录")

# 5. 延迟日志,对昂贵函数进行惰性求值
logger.opt(lazy=True).info("结果：{res}", res=lambda:sum(range(10**7)))

# 6. 适用于脚本和库
# 6.1 脚本 For scripts
config = {
    "handlers": [
        {"sink": sys.stdout, "format": "{time} - {message}"},
        {"sink": "file.log", "serialize": True},
    ],
    "extra": {"user": "someone"}
}
logger.configure(**config)

# 6.2 库 For libraries, should be your library's `__name__`
logger.disable("my_library")
logger.info("No matter added sinks, this message is not displayed")

# In your application, enable the logger in the library
logger.enable("my_library")
logger.info("This message however is propagated to the sinks")


# 7.与标准日志记录完全兼容
import loguru
import logging

# 创建标准日志记录器
logging.basicConfig(filename='example.log', level=logging.DEBUG)

# 配置Loguru不使用其内部日志记录器
loguru.logger.propagate = False

# 使用Loguru记录消息并将其发送到标准日志记录器
loguru.logger.debug('This message will be logged to both Loguru and the standard logger') 