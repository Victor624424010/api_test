import pymysql
from conf import config


def get_conn():
    conn = pymysql.connect(host = config.db_host,
                           port = config.db_port,
                           user = config.db_user,
                           password = config.db_password,
                           db = config.db,
                           charset = config.db_charset)
    return conn

def db_query(sql):
    config.logging.debug(sql)
    con = get_conn()
    cur = con.cursor()
    cur.execute(sql)
    r = cur.fetchall()
    config.logging.debug(r)
    cur.close()
    con.close()
    return r

def db_change(sql):
    config.logging.debug(sql)
    con = get_conn()
    cur = con.cursor()
    try:
        cur.execute(sql)
        con.commit()
    except Exception as e:
        config.logging.error(repr(e))
        # print(repr(e)) #d打印错误信息
        con.rollback()#回滚修改
    finally:
        cur.close()
        con.close()
def chack_card(number):
    r = db_query("select * from  cardinfo WHERE cardNumber =  '%s'" % number)
    if r:
        return True
    return False

def del_card(number):
    db_change("delete from cardinfo WHERE cardNumber =  '%s'" % number)

def up_card(number):
    db_change("UPDATE  cardinfo set cardstatus = '0' where cardnumber = '%s'" % number)


def chack_user(name):
    r = db_query("select * from carduser where userName = '%s'" % name)
    if r:
        return True
    return False

def del_user(name):
    db_change("delete from carduser where userName = '{}'" .format(name))



# if __name__ == '__main__':#用来判断是不会死从当前模块执行 当前模块main   否则写别的模块名字
#     del_card(6216600411107)