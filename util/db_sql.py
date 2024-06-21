"""
此文件为调试sql语句所用，并无实际的使用作用
"""



def db_connect():
    db_params = {
        # 前提定义好主机名、用户名、密码、数据库名称
        "host": "fdbd:dc03:ff:501:84da:51d8:344e:977a",  # 数据库主机名
        "username": "ic_9216811627_w",  # 数据库用户名
        "password": "vYDyVVQ4noQVjT3_BkLHkYIvRMl1LOYR",  # 数据库密码
        "database": "ic_backend"  # 数据库名称
    }
    db = pymysql.connect(
        host=db_params["host"],
        user=db_params["username"],
        password=db_params["password"],
        database=db_params["database"]
    )
    return db


from util.db_check import *


def db_connect():
    db_params = {
        # 前提定义好主机名、用户名、密码、数据库名称
        "host": "fdbd:dc03:ff:501:84da:51d8:344e:977a",  # 数据库主机名
        "username": "ic_9216811627_w",  # 数据库用户名
        "password": "vYDyVVQ4noQVjT3_BkLHkYIvRMl1LOYR",  # 数据库密码
        "database": "ic_backend"  # 数据库名称
    }
    db = pymysql.connect(host=db_params["host"],
                         user=db_params["username"],
                         password=db_params["password"],
                         database=db_params["database"]
                         )
    return db


# def newest():  # 定义一个newest函数
#     """获取ic_info中最新的一条数据"""
#     # 连接到数据库： 使用pymysql.connect()方法连接到MySQL数据库，并传入db_params中的参数，最后返回给连接对象db
#     db = db_connect()
#     # 创建游标对象： 使用数据库连接对象的cursor()方法创建一个游标对象cursor，用于执行sql语句
#     cursor = db.cursor()
#     # 定义查询语句：数据库操作-->查询语句，然后赋值给sql
#     sql2 = "select req_id from ic_req where account_id=2100000056 and status='WaitCommunication' limit 1"
#
#     # 日志输出：
#     logging.info("sql is -->%s" % sql2)
#     # 初始化res变量： 将变量res初始化为，它被用作查询结果的占位符
#     res = ""
#     try:
#         # 执行查询语句：使用游标对象的execute()方法执行SQL查询语句
#         cursor.execute(sql2)
#         # 获取查询结果：使用游标对象fetchall()方法获取查询结果，
#         # 一个循环结构，它遍历了从数据库获取的结果集中的每一行数据。在每次迭代中，当前行的数据被赋值给变量 row。简单来说：就是将元组中的数据，遍历出来，显得好看一点而已
#         for row in cursor.fetchall():
#             print(row)  # 逐行打印每条数据
#         # 获取查询结果： 使用游标对象fetchall()方法获取查询结果，将查询结果赋值给到了res（与上面那个for循环的重复了，所以这个就先不用了）
#         # res = cursor.fetchall()
#
#         # 将查询结果转换成字符串类型，并使用print打印出来
#         # print(res)
#     # 异常处理： 用于捕获执行查询过程中的异常，并打印出错误信息
#     except Exception as e:
#         print("执行错误:", e)
#     # 关闭数据库：
#     db.close()
#     # 返回查询结果：将查询结果作为函数的返回值
#     return res
#
#
# # 结合上方法print调试时打印使用。调试完成后注释掉哦，不然就会有两条数据出现。
# newest()


# # 方法三：
# # 连接到 MySQL 数据库
# def connect_to_mysql(host, username, password, database):
#     # 定义了一个名为connect_to_mysql的函数，用户连接到MySQL数据库，它接受主机名、用户名、密码和数据库名作为输入参数。
#     try:
#         # 在try块中，使用pymysql.connect()方法创建于数据库的连接，并将连接对象存储在connection变量中。
#         connection = pymysql.connect(
#             host=host,
#             user=username,
#             password=password,
#             database=database
#         )
#         # 如果连接成功，则打印成功的消息并返回连接对象
#         print("成功连接到 MySQL 数据库")
#         return connection
#     # 如果连接失败，则打印失败的消息并返回None
#     except pymysql.Error as error:
#         print(f"连接到 MySQL 数据库时出现错误: {error}")
#         return None
#
#
# # 执行查询
# def execute_query(connection, sql):  # connection：连接数据库的参数；sql：查询语句
#     # 定义了一个名为execute_query的函数，用于执行查询语句，他接受数据库连接对象和查询语句作为输入参数。
#     try:
#         # 在函数内部，首先创建一个游标对象 cursor，
#         cursor = connection.cursor()
#         # 然后使用execute()方法执行查询语句
#         cursor.execute(sql)
#         # 通过调用fetchall()方法获取查询结果，并将结果存储在result变量中
#         result = cursor.fetchall()
#         # 最后关闭游标
#         cursor.close()
#         # 并返回查询结果，
#         return result
#     # 如果执行查询时发生错误，将打印错误消息并返回None
#     except pymysql.Error as error:
#         print(f"执行查询时出现错误: {error}")
#         return None
#
#
# # 断开与 MySQL 数据库的连接
# def disconnect_from_mysql(connection):
#     # 定义了一个名为disconnect_from_mysql的函数，用于断开与MySQL数据库的连接，它接受数据库连接对象最为输入参数，
#     # 在函数内部，首先检查连接对象是否存在，
#     if connection:
#         # 然后调用链接对象的close()方法关闭连接。
#         connection.close()
#         # 最后打印连接已断开的消息。
#         print("与 MySQL 数据库的连接已断开")
#
#
# # 连接到现有的 MySQL 数据库
# host = 'fdbd:dc03:ff:501:84da:51d8:344e:977a'  # 数据库主机名
# username = 'ic_9216811627_w'  # 数据库用户名
# password = 'vYDyVVQ4noQVjT3_BkLHkYIvRMl1LOYR'  # 数据库密码
# database = 'ic_backend'  # 数据库名称
# # 调用connect_to_mysql函数，已建立与数据库的连接，将返回的连接对象存储在connection变量中。
# connection = connect_to_mysql(host, username, password, database)
# # 执行查询
# if connection:  # 检查连接对象connection是否成功建立了与数据库的连接，若连接成功，条件为真，则执行sql查询；若是连接失败，则返回None，条件为假，代码块内的语句将被跳过。
#     sql = "SELECT * FROM ic_backend.ic_info where account_id =2100000056 Limit 1,3"  # 执行sql语句
#     # 调用execute_query函数（connection：连接数据库；sql：查询语句）执行查询，将查询结果存储在result变量中，
#     result = execute_query(connection, sql)  # connection：连接数据库；sql：查询语句
#
#     # 处理查询结果
#     if result:
#         # 检查result是否存在，即是否成功获取到了查询的数据，如果查询结果在且非空，条件为真，代码块内的语句将被执行；如果查询结果为None或为空，条件为假，代码块内的 语句将被跳过。
#         for row in result:  # 在条件为真时，循环遍历查询结果中的每一行数据，并print打印出每一行内容
#             print(row)
#
# # 断开与 MySQL 数据库的连接
# disconnect_from_mysql(connection)  # 最后调用disconnect_from_mysql函数断开与MySQL数据库的连接。


# # 方法二：
# 连接到 MySQL 数据库
def all2():
    """获取ic_info中前三条数据"""
    try:
        # 连接到数据库
        db = db_connect()
        print("连接数据库成功")
        # 创建游标对象
        cursor = db.cursor()
        # 定义查询语句
        sql = "SELECT * FROM ic_info where account_id =2100000056 Limit 1,3"
        # 执行查询语句
        cursor.execute(sql)
        # 获取查询结果： 使用游标对象fetchall()方法获取查询结果，将查询结果赋值给到了res（与上面那个for循环的重复了，所以这个就先不用了）
        res = cursor.fetchall()
        # 将查询结果转换成字符串类型，并使用print打印出来
        print(res)
        # 关闭游标
        cursor.close()
        # 关闭数据库连接
        db.close()
        print("关闭数据库连接")
    except pymysql.Error as e:
        print("连接数据库发生错误:", e)


# 调用 all1() 函数将触发其执行，并在控制台打印查询结果
all2()
