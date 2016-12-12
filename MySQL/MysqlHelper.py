"""
Mysql帮助类，使用pymysql

1.获取新增row的ID
last_rowid = self.cursor.lastrowid

2.移动游标
self.cursor.scroll(1, mode='relative')  # 相对当前位置移动,向下移动一行
self.cursor.scroll(2, mode='absolute')  # 相对绝对位置移动

3.为防止SQL注入,应使用参数化sql语句，避免拼接

"""
import pymysql


class MysqlHelper:
    def __init__(self, db_config):
        self.__config = db_config

    # 单条（增|删|改）
    def execute(self, sql, params=None):
        result = 0
        try:
            conn = pymysql.connect(**self.__config)
            with conn.cursor() as cur:
                effect_row = cur.execute(sql, params)
                conn.commit()
                if effect_row == 1:
                    result = 1
        except Exception as e:
            print('Error:' + str(e))
        finally:
            conn.close()
            return result

    # 多条（增|删|改）
    def execute_many(self, sql, params=None):
        result = 0
        try:
            conn = pymysql.connect(**self.__config)
            with conn.cursor() as cur:
                effect_row = cur.executemany(sql, params)
                conn.commit()
                if effect_row >= 1:
                    result = 1
        except Exception as e:
            print('Error:' + str(e))
        finally:
            conn.close()
            return result

    # 查询（单条）
    def query_one(self, sql, params=None):
        result = None
        try:
            conn = pymysql.connect(**self.__config)
            with conn.cursor() as cur:
                cur.execute(sql, params)
                result = cur.fetchone()
        except Exception as e:
            print('Error:' + str(e))
        finally:
            conn.close()
            return result

    # 查询（多条）
    def query_many(self, sql, params=None):
        result = None
        try:
            conn = pymysql.connect(**self.__config)
            with conn.cursor() as cur:
                cur.execute(sql, params)
                result = cur.fetchall()
        except Exception as e:
            print('Error:' + str(e))
        finally:
            conn.close()
        return result

    # 查询（多条,返回字典类型）
    def query_with_dic(self, sql, params=None):
        result = None
        try:
            conn = pymysql.connect(**self.__config)
            with conn.cursor(cursor=pymysql.cursors.DictCursor) as cur:
                cur.execute(sql, params)
                result = cur.fetchall()
        except Exception as e:
            print('Error:' + str(e))
        finally:
            conn.close()
        return result

    # 使用事务
    def execute_with_transaction(self):
        result = False
        try:
            conn = pymysql.connect(**self.__config)
            with conn.cursor() as cur:
                cur.execute("UPDATE Writers SET Name = %s WHERE Id = %s", ("Leo Tolstoy", "1"))
                cur.execute("UPDATE Writers SET Name = %s WHERE Id = %s", ("Boris Pasternak", "2"))
                cur.execute("UPDATE Writer SET Name = %s WHERE Id = %s", ("Leonid Leonov", "3"))
                conn.commit()
                result = True
        except Exception as e:
            conn.rollback()
            print('Error:' + str(e))
        finally:
            conn.close()
        return result

    # 使用存储过程
    def execute_with_pro(self, pro, params=None):
        result = None
        try:
            conn = pymysql.connect(**self.__config)
            with conn.cursor() as cur:
                cur.callproc(pro, params)  # 调用存储过程
                result = cur.fetchall()
                conn.commit()
        except Exception as e:
            print('Error:' + str(e))
        finally:
            conn.close()
        return result


if __name__ == '__main__':
    pass
