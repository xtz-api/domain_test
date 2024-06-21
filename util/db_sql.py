"""
本文件仅供调试SQL语句使用，以及一些方法参考
"""
import logging

import pymysql


def db_connect():  # 定义好一个方法，供后续调用
    # ：连接数据库，定义好：主机名、用户名、密码、数据库名称
    db_params = {
        "host": 'fdbd:dc03:ff:501:c734:3b2:89f9:c221',  # 主机名
        "user": 'ti_bs_w',  # 用户名
        "password": '2HYTTc8eE9Ye6h2_AN3E6LsrvqdUp0wp',  # 密码
        "database": 'ti_bs'  # 数据库名称
    }
    # 建立数据库连接
    db = pymysql.connect(
        host=db_params["host"],
        user=db_params["user"],
        password=db_params["password"],
        database=db_params["database"]
    )
    # 返回数据库连接对象，在使用其他代码时，可通过db_connect()函数来获取数据库的连接
    return db


"""
代码方法详解：
    1、获取数据
        cursor.fetchall() ：取所有的数据 
                fetchone()获取一条数据；
                fetchmany(3)取3条数据；
    2、打印数据
        2.1、直接print打印
            cursor.execute(sql)  
            result1 = cursor.fetchall() 
            print(result1)
        2.2、使用for循环打印出每列的内容
            result1 = cursor.fetchall()
            for row in result1: 
                print(row)
        2.3、使用for循环，打印详细的列内容，如只想要这三条数据的前三列内容
            result1 = cursor.fetchall()
            for row in result1: 
                did = row[0]  # 打印第一列的内容
                domain = row[1]  # 打印第二列的内容
                zone = row[2]  # 打印第三列的内容
                print(did, domain, zone)
"""


def db_select():
    """固定SQL查询---使用循环打印的数据"""


#     db = db_connect()  # 将上方的方法简单赋值给db
#     print(db)  # 调试连，返回结果：<pymysql.connections.Connection object at 0x7fe0a819aee0>
#     cursor = db.cursor()  # 获取游标，将游标赋值给cursor
#
#     # print(cursor)  # 调试连接，返回结果<pymysql.cursors.Cursor object at 0x7fe0a8169be0>
#     sql = "SELECT * FROM domain_info ORDER BY `id` DESC LIMIT 0,3"
#     logging.info("sql is -->%s" % sql)
#     cursor.execute(sql)  # 执行操作，通常搭配SQL语句执行
#     result = cursor.fetchall()  # 取所有的数据
#     cursor.close()  # 关闭游标
#     db.close()  # 关闭数据库连接
#     return result  # 返回获取的数据
#
#
# result1 = db_select()  # 将整个方法return返回的获取数据，赋值给到了result1
# for row in result1:  # 使用循环打印数据
#     print(row)  # 以每行的数据循环打印出来
# print("*******************************************")
#

def domain_RegistrantChange_error():
    """修改域名状态，并返回域名名称"""


#     db = db_connect()  # 创建数据库
#     # print(db) # 为了校验数据库是否能正常连接，如果打印有：<pymysql.connections.Connection object at 0x7fbb380b3fd0>  字段，说明连接正常
#     cursor = db.cursor()  # 创建游标
#     # 先修改一条域名status=1
#     sql = "UPDATE domain_info SET status='2' WHERE account_id='2100266070' AND status='1' AND verify_status = '4' AND dn_audit_status = '512' LIMIT 1"
#     try:
#         cursor.execute(sql)
#         db.commit()  # 提交事务
#         # 再次查找域名
#         select_domain = "SELECT domain FROM domain_info WHERE status='2' AND account_id='2100266070'"
#         cursor.execute(select_domain)
#         extracted_domain_name = cursor.fetchall()
#
#         return extracted_domain_name[0][0]  # return 返回一个参数
#     except Exception as error:
#         print("执行错误", error)
#         db.rollback()  # 回滚事务
#
#     finally:
#         cursor.close()
#         db.close()
#
#
# print(domain_RegistrantChange_error())


# def domain_select_update(select_sql, update_sql):
#     """查找域名，和修改查找域名"""
#     db = db_connect()  # 创建数据库
#     # print(db) # 为了校验数据库是否能正常连接，如果打印有：<pymysql.connections.Connection object at 0x7fbb380b3fd0>  字段，说明连接正常
#     cursor = db.cursor()  # 创建游标
#     # 先修改一条域名status=1
#     try:
#         if update_sql == "":  # 如果修改的sql为空，则只执行查询的语句
#             cursor.execute(select_sql)
#             return cursor.fetchall()[0][0]  # return 返回一个参数
#         elif select_sql == "":  # 如果查询的sql为空，则只执行修改的语句
#             cursor.execute(update_sql)
#             db.commit()
#             print("修改成功")
#         else:  # 如果上述不成立，则执行修改and查询的语句
#             # domain_status_update(update_sql)
#             cursor.execute(update_sql)
#             db.commit()
#             print("修改成功")
#             cursor.execute(select_sql)
#             return cursor.fetchall()[0][0]  # return 返回一个参数
#
#     except Exception as error:
#         print("执行错误", error)
#         db.rollback()  # 回滚事务
#
#     finally:
#         cursor.close()
#         db.close()
#
#
# print(domain_select_update("SELECT domain FROM domain_info WHERE account_id = '2100266070' AND expired_time < '2034-01-01'AND supplier = 'xinNet' AND status = '1' AND verify_status = '4' AND dn_audit_status = '512'",
#                            ""))
# # UPDATE domain_info SET status='2' WHERE domain='openapi中文f7494504.cn    expired_time'

def domain_customize_select(sql):
    """获取自定义SQL，根据SQL语句获取内容"""
    db = db_connect()
    cursor = db.cursor()
    logging.info("sql is -->%s" % sql)
    try:
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as error:
        print("执行错误", error)
    cursor.close()
    db.close()


print(domain_customize_select("SELECT domain FROM domain_info WHERE account_id = '2100266070' AND expired_time < '2034-01-01' AND status = '1' AND verify_status = '4' AND dn_audit_status = '512' LIMIT 1,2")[0][0])
print("************************")
print(domain_customize_select("SELECT expired_time FROM domain_info WHERE account_id = '2100266070' AND expired_time < '2034-01-01' "
                              "AND status = '1' AND verify_status = '4' AND dn_audit_status = '512' LIMIT 1,2")[0][0])
