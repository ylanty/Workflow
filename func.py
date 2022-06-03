import pymysql
import time
import os

def create_new_conn():
    return pymysql.connect(host=os.environ["mysql_host"],
                         user=os.environ["mysql_username"],
                         password=os.environ["mysql_password"],
                         database=os.environ["mysql_database"])

def executesql(web_name,result):
    # 打开数据库连接
    db = create_new_conn()
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor()
    # SQL 语句
    sql = "INSERT INTO `daylylog`(`web_name`, `day_time`, `result`, `sys_time`) VALUES ('%s', date_format(date_add(sysdate(), interval 8 hour),'%Y-%m-%d'), '%s',date_add(sysdate(), interval 8 hour))" %(web_name,result)
    try:
       # 执行sql语句
       cursor.execute(sql)
       # 执行sql语句
       db.commit()
    except:
       # 发生错误时回滚
       db.rollback()
    finally:
        # 关闭数据库连接
        cursor.close()
        db.close()

def isexecuted(web_name):
    # 打开数据库连接
    db = create_new_conn()
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor()
    # SQL 语句
    sql = "SELECT * FROM `daylylog` WHERE `web_name` = '%s' and `day_time` = date_format(date_add(sysdate(), interval 8 hour),'%Y-%m-%d') " %web_name
    try:
       # 执行sql语句
       cursor.execute(sql)
       # 获取所有记录列表
       results = cursor.fetchall()
       if len(results)>0:
           return True
       else:
           return False
    except:
       # 发生错误
       print ("Error: unable to fetch data")
       return False
    finally:
        # 关闭数据库连接
        cursor.close()
        db.close()
        
def daylylog(msg):
    try:
        file_handle=open('daylylog.txt',mode='a')
        file_handle.writelines([time.strftime("%Y/%m/%d %H:%M:%S "),msg,'\n'])
        file_handle.close()
        print(time.strftime("%Y/%m/%d %H:%M:%S ")+msg)
    except Exception as e:
        print("daylylog有错误:", e)

