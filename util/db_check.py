import logging

import pymysql


def db_connect():
    """连接数据库"""
    db_params = {
        "host": 'fdbd:dc03:ff:501:c734:3b2:89f9:c221',  # 主机名
        "user": 'ti_bs_w',  # 用户名
        "password": '2HYTTc8eE9Ye6h2_AN3E6LsrvqdUp0wp',  # 密码
        "database": 'ti_bs'  # 数据库名称
    }
    db = pymysql.connect(
        host=db_params["host"],
        user=db_params["user"],
        password=db_params["password"],
        database=db_params["database"]
    )
    return db


"""****************************************====这部分是SELECT查询的SQL语句====****************************************"""


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


# print(domain_customize_select("SELECT dn_audit_status FROM domain_info WHERE account_id ='2100266070' AND supplier ='xinNet' ORDER BY `id` DESC")[0][0])
# domain_customize_select("UPDATE domain_info SET status='2' WHERE domain = 'auto-test10.cn'")


def domain_one():
    """获取单一的正常的域名(数据库倒序最新的第二条)"""
    db = db_connect()
    print(db)
    cursor = db.cursor()
    sql = "SELECT domain FROM domain_info WHERE account_id ='2100266070' AND supplier ='xinNet' AND dn_audit_status = '512' AND status  = '1' AND verify_status = '4' ORDER BY `id` DESC"
    logging.info("sql is -->%s" % sql)
    try:
        cursor.execute(sql)
        return cursor.fetchmany(3)[1][0]
    except Exception as error:
        print("执行错误", error)
    cursor.close()
    db.close()


# print(domain_one())


def domain_one1():
    """获取单一的正常的域名(数据库倒序最新的第三条)"""
    db = db_connect()
    cursor = db.cursor()
    sql = "SELECT domain FROM domain_info WHERE account_id ='2100266070' AND supplier ='xinNet' AND dn_audit_status = '512' AND status  = '1' AND verify_status = '4' ORDER BY `id` DESC"
    logging.info("sql is -->%s" % sql)
    try:
        cursor.execute(sql)
        return cursor.fetchmany(3)[2][0]
    except Exception as error:
        print("执行错误", error)
    cursor.close()
    db.close()


# print(domain_one1())

def domain_async_task():
    """获取异步任务的域名"""
    db = db_connect()
    cursor = db.cursor()
    sql = "SELECT task_no FROM domain_async_task WHERE account_id='2100266070' ORDER BY `id` DESC LIMIT 1"
    logging.info("sql is -->%s" % sql)
    try:
        cursor.execute(sql)
        return cursor.fetchall()[0][0]
    except Exception as error:
        print("执行错误", error)
    cursor.close()
    db.close()


# print(domain_async_task())

def RenewDomain_domain():
    """获取单一的正常的域名"""
    db = db_connect()
    cursor = db.cursor()
    sql = "SELECT domain FROM domain_info WHERE account_id = '2100266070' AND expired_time < '2034-01-01' AND status = '1' AND verify_status = '4' AND dn_audit_status = '512' "
    logging.info("sql is -->%s" % sql)
    try:
        cursor.execute(sql)
        return cursor.fetchmany(3)[2][0]
    except Exception as error:
        print("执行错误", error)
    cursor.close()
    db.close()


def RenewDomain_expired_time():
    """获取域名的到期时间"""
    db = db_connect()
    cursor = db.cursor()
    sql = "SELECT expired_time FROM domain_info WHERE account_id = '2100266070' AND expired_time < '2034-01-01' AND status = '1' AND verify_status = '4' AND dn_audit_status = '512' "
    try:
        cursor.execute(sql)
        return cursor.fetchmany(3)[2][0]
    except Exception as error:
        print("执行错误", error)
    cursor.close()
    db.close()


"""****************************************====这部分是UPDATE修改的SQL语句====****************************************"""


def domain_status_update(sql):
    """根据SQL修改语句,更新数据库内容"""
    db = db_connect()
    # print(db)
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()  # 提交事务
        affected_rows = cursor.rowcount
        print(f"更新成功了{affected_rows}条数据")
    except Exception:
        logging.info("请检查sql语句")
    finally:
        cursor.close()
        db.close()


# domain_status_update("UPDATE domain_info SET status='2' WHERE domain = 'auto-test10.cn'")


def domain_status1():
    """将domain_info库内的最新三条域名状态，由非正常(256)改成正常(512)状态"""
    db = db_connect()
    print(db)
    cursor = db.cursor()
    sql = "UPDATE domain_info SET dn_audit_status = '512' WHERE account_id = '2100266070' AND dn_audit_status = '256' AND status = '1' AND verify_status = '4' AND supplier = 'xinNet' ORDER BY `id` DESC LIMIT 3"
    try:
        cursor.execute(sql)
        db.commit()  # 提交事务
        affected_rows = cursor.rowcount
        print(f"更新成功，受影响的行数：{affected_rows}")
    except Exception as error:
        print("查看sql语句是否正确")
        db.rollback()  # 回滚事务
    finally:
        cursor.close()
        db.close()


# print(domain_status())

def domain_RegistrantChange_error():
    """修改域名状态，并返回域名名称"""
    db = db_connect()  # 创建数据库
    # print(db) # 为了校验数据库是否能正常连接，如果打印有：<pymysql.connections.Connection object at 0x7fbb380b3fd0>  字段，说明连接正常
    cursor = db.cursor()  # 创建游标
    # 先修改一条域名status=1
    sql = "UPDATE domain_info SET status='2' WHERE account_id='2100266070' AND status='1' AND verify_status = '4' AND dn_audit_status = '512' LIMIT 1"
    try:
        cursor.execute(sql)
        db.commit()  # 提交事务
        # 再次查找域名
        select_domain = "SELECT domain FROM domain_info WHERE status='2' AND account_id='2100266070'"
        cursor.execute(select_domain)
        extracted_domain_name = cursor.fetchall()

        return extracted_domain_name[0][0]  # return 返回一个参数
    except Exception as error:
        print("执行错误", error)
        db.rollback()  # 回滚事务

    finally:
        cursor.close()
        db.close()


# print(f"提取到的域名：{domain_RegistrantChange_error()}")
def domain_select_update(select_sql, update_sql):
    """查找域名，和修改查找域名"""
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

# print(domain_select_update("SELECT domain FROM domain_info WHERE status='4' AND account_id='2100266070'", "UPDATE domain_info SET status='2' WHERE domain='openapi中文f7494504.cn'"))
