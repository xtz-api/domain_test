import logging

import pymysql

DB_params = {
    "host" : '10.225.71.238',
    "user" : 'ti_bs_w',
    "password" : '2HYTTc8eE9Ye6h2_AN3E6LsrvqdUp0wp',
    "database" : 'ti_bs'
}

def db_connect():
    db = pymysql.connect(host=DB_params["host"],
                         user=DB_params["user"],
                         password=DB_params["password"],
                         database=DB_params["database"])
    return db

def domain_get_templateList_db(sql):
    """获取当前用例的购物车列表"""
    # 打开数据库连接
    db = pymysql.connect(host=DB_params["host"],
                         user=DB_params["user"],
                         password=DB_params["password"],
                         database=DB_params["database"])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # SQL 查询语句
    logging.info("sql is -> %s"%sql)
    res = 0
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        res = cursor.fetchall()
    except:
        print("Error: unable to fetch data")
    # 关闭数据库连接
    db.close()
    return res[0][0]

def domain_get_templateDetail_db(sql):
    """获取当前用例的购物车列表"""
    # 打开数据库连接
    db = pymysql.connect(host=DB_params["host"],
                         user=DB_params["user"],
                         password=DB_params["password"],
                         database=DB_params["database"])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # SQL 查询语句
    logging.info("sql is -> %s"%sql)
    res = 0
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        res = cursor.fetchall()
    except:
        print("Error: unable to fetch data")
    # 关闭数据库连接
    db.close()
    return res

def domain_get_shopingList_db():
    """获取当前用例的购物车列表"""
    # 打开数据库连接
    db = pymysql.connect(host=DB_params["host"],
                         user=DB_params["user"],
                         password=DB_params["password"],
                         database=DB_params["database"])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # SQL 查询语句
    sql = "SELECT * FROM `domain_shopping_list` WHERE `account_id`=2100000056 AND `user_id`=2100000056"
    logging.info("sql is -> %s"%sql)
    res = 0
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        res = cursor.fetchall()
    except:
        print("Error: unable to fetch data")
    # 关闭数据库连接
    db.close()
    return res

def domain_get_shopingList_by_domain(domain):
    """获取当前用例的购物车列表"""
    # 打开数据库连接
    db = pymysql.connect(host=DB_params["host"],
                         user=DB_params["user"],
                         password=DB_params["password"],
                         database=DB_params["database"])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # SQL 查询语句
    sql = "SELECT * FROM `domain_shopping_list` WHERE `account_id`=2100000056 and `test_domain` = %s%s%s"%('"', domain, '"')
    logging.info("sql is -> %s"%sql)
    res = 0
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        res = cursor.fetchall()
        for row in res:
            id = row[0]
            account_id = row[1]
            user_id = row[2]
            domian = row[3]
            zone = row[4]
            # 打印结果
            print("id=%s,account_id=%s,user_id=%s,domian=%s,zone=%s" % \
                  (id, account_id, user_id, domian, zone))
    except:
        print("Error: unable to fetch data")
    # 关闭数据库连接
    db.close()
    return res

def domain_get_all_zones():
    """获取所有的zone列表"""
    # 打开数据库连接
    db = db_connect()
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # SQL 查询语句
    sql = "SELECT zone FROM `domain_zone_info`"
    logging.info("sql is -> %s"%sql)
    res_list = []
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        res = cursor.fetchall()
        for i in res:
            res_list.append(i[0])

    except:
        print("Error: unable to fetch data")
    # 关闭数据库连接
    db.close()
    return res_list

def domain_update_db(sql):
    """更改数据库"""
    # 打开数据库连接
    db = pymysql.connect(host=DB_params["host"],
                         user=DB_params["user"],
                         password=DB_params["password"],
                         database=DB_params["database"])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # SQL 查询语句
    logging.info("sql is -> %s"%sql)
    res = 0
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        res = db.commit()
    except:
        print("Error: unable to update data")
        db.rollback()
    # 关闭数据库连接
    db.close()
    return res

