import logging

import pymysql


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

print(db_connect())

"""需求--数据库查询"""


def opportunityID_sql():
    """获取最新的一条opportunityID"""
    db = db_connect()
    cursor = db.cursor()
    sql = "SELECT req_id FROM ic_req WHERE account_id=2100266070 ORDER BY req_id DESC LIMIT 1"
    logging.info("sql is -->%s" % sql)
    try:
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        print("执行错误:", e)
    db.close()


# print(opportunityID_sql()[0][0])


def customize_sql(sql):
    """获取自定义SQL，根据SQL语句自定义获取内容"""
    db = db_connect()
    cursor = db.cursor()
    logging.info("sql is -->%s" % sql)
    try:
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        print("执行错误:", e)
    cursor.close()
    db.close()


"""模板管理--数据库查询"""


def templateID_sql():
    """获取最新的一条TemplateID"""
    db = db_connect()
    cursor = db.cursor()
    sql = "SELECT template_id FROM ic_template WHERE account_id=2100266070 ORDER BY template_id DESC LIMIT 1"
    logging.info("sql is -->%s" % sql)
    try:
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        print("执行错误:", e)
    db.close()


# print(customize_sql("SELECT req_id FROM ic_req WHERE account_id=2100266070 AND status='WaitPlaceOrder' AND req_service='CloudICRegistration' ORDER BY id ASC LIMIT 1")[0][0])


def ic_select_update(select_sql, update_sql):
    """查找、修改 and 查找并修改"""
    db = db_connect()  # 创建数据库
    # print(db) # 为了校验数据库是否能正常连接，如果打印有：<pymysql.connections.Connection object at 0x7fbb380b3fd0>  字段，说明连接正常
    cursor = db.cursor()  # 创建游标
    try:
        if update_sql == "":  # 如果修改的sql为空，则只执行查询的语句
            cursor.execute(select_sql)
            return cursor.fetchall()[0][0]  # return 返回一个参数
        elif select_sql == "":  # 如果查询的sql为空，则只执行修改的语句
            cursor.execute(update_sql)
            db.commit()
            print("执行update_sql，修改成功")
        else:  # 如果上述不成立，则执行修改and查询的语句
            # domain_status_update(update_sql)
            cursor.execute(update_sql)
            db.commit()
            print("执行update_sql，修改成功")
            cursor.execute(select_sql)
            return cursor.fetchall()[0][0]  # return 返回一个参数

    except Exception as error:
        print("执行错误", error)
        db.rollback()  # 回滚事务

    finally:
        cursor.close()
        db.close()


# print(ic_select_update("SELECT req_id FROM ic_req WHERE account_id = '2100266070' ORDER BY `id` DESC  ", ""))
# print(domain_select_update("SELECT req_service FROM ic_req WHERE account_id = '2100266070' AND req_service = 'EnterpriseAccountCertificationGuide'", ""))
