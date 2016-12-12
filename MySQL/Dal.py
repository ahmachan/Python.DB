import MysqlHelper
import AppConfig

"""
# 插入一条数据
reCount = cur.excute('insert into lcj(name,age) vaules(%s,%s)',('ff',18))

# 插入多行（部分字段）
ret = cur.executemany("insert into lcj(name,tel)values(%s,%s)", [("kk",13212344321),("kw",13245678906)])

# 插入多行（全部字段）
ret = cur.executemany("insert into lcj values(%s,%s,%s,%s,%s)", [(41,"xiaoluo41",'man',24,13212344332),
                                                              (42,"xiaoluo42",'gril',21,13245678948),
                                                              (43,"xiaoluo43",'gril',22,13245678949),
                                                        (44,"xiaoluo44",'main',24,13543245648)])
"""


class Dal:
    def __init__(self):
        self.w_config = AppConfig.db_write_config
        self.r_config = AppConfig.db_read_config

    def execute(self, sql, params=None):
        result = False
        try:
            i = MysqlHelper(self.w_config).execute(sql, params)
            result = i > 0
        except Exception as e:
            print('Error:' + str(e))
        return result

    def execute_many(self, sql, params=None):
        result = False
        try:
            i = MysqlHelper(self.w_config).execute_many(sql, params)
            result = i > 0
        except Exception as e:
            print('Error:' + str(e))
        return result

    def select_one(self, sql, params=None):
        result = None
        try:
            result = MysqlHelper(self.r_config).query_one(sql, params)
        except Exception as e:
            print('Error:' + str(e))
        return result

    def select_many(self, sql, params=None):
        result = None
        try:
            result = MysqlHelper(self.r_config).query_many(sql, params)
        except Exception as e:
            print('Error:' + str(e))
        return result


if __name__ == '__main__':
    pass
