import emoji
import pymysql


# 喵喵自己的SQL
class MiaoSql:
    """喵喵自己的MYSQL
    初始化数据库对象

    Parameters
    ----------
    con : dict\n
        {\n
            host: 主机号,
            user: 用户名,
            password: 密码,
            database: 数据库名
        }
    """

    cursor = None
    _sjk = None

    raw_data = None
    _out_cols = None

    # 数据库连接
    def __init__(self, con: dict):
        """初始化数据库对象"""
        self._config = con
        self._sjk = pymysql.connect(**self._config)
        self.cursor = self._sjk.cursor()

    # 数据库断开
    def __del__(self):
        """销毁数据库对象"""
        self._sjk.commit()
        self.cursor.close()
        self._sjk.close()

    # 获取某表的数据条数
    def get_len(self, table: str) -> int:
        """获取某表的数据条数

        Parameters
        ----------
        table : str
            要查询的表名

        Returns
        -------
        int
            表的数据条数
        """
        qur = f"select * from `{table}`;"
        res = self.cursor.execute(qur)
        return res

    # 判断某数据是否在表中
    def if_in_it(self, table: str, cols: list, vals: list) -> bool:
        """判断某数据是否在表中

        Parameters
        ----------
        table : str
            要查询的表名
        cols : list
            要查询的列 的列表
        vals : list
            值的列表，与列对应

        Returns
        -------
        bool
            是否存在表内
        """
        assert len(cols) == len(vals), f"列[{len(cols)}]与值[{len(vals)}]的数目不相同"

        qur = f"SELECT * FROM `{table}` WHERE {' AND '.join([col + ' = ' + self.format_val(val) for col, val in zip(cols, vals)])} "
        print(qur)
        res = self.cursor.execute(qur)

        if res == 0:
            return False
        else:
            return True

    def sel(
        self,
        table: str,
        condition: str = None,
        out_cols: list = None,
        order: str = None,
    ):
        """自定义查询\n
        最自定义的一集

        Parameters
        ----------
        table : str
            表名
        condition : str, optional
            查询条件
        out_cols : list, optional
            输出列的列表，默认全输出
        order : str, optional
            以某一列排序输出

        Returns
        -------
        _type_
            查询结构对象
        """

        qur = (
            f"SELECT {'*' if not out_cols else ', '.join('`' + out_col + '`' for out_col in out_cols)} FROM `{table}` "
            f"WHERE {condition if condition else 1} "
            f"{'' if not order else 'ORDER BY `' + order + '`'}"
        )
        print(qur)
        res = self.cursor.execute(qur)
        return res

    def sel_eq(
        self,
        table: str,
        cols: list[str],
        vals: list[str],
        out_cols: list = None,
        order: str = None,
        use_or: bool = False,
    ):
        """以 = 查询

        Parameters
        ----------
        table : str
            要查询的表名
        cols : list[str]
            要查询的列
        vals : list[str]
            值
        out_cols : list, optional
            输出的列，默认全列
        order : str, optional
            以某列排序输出
        use_or : bool, optional
            使用or或and，默认and

        Returns
        -------
        _type_
            查询结果对象
        """
        assert len(cols) == len(vals), f"列[{len(cols)}]与值[{len(vals)}]的数目不相同"

        qur = (
            f"SELECT {'*' if not out_cols else ', '.join('`' + out_col + '`' for out_col in out_cols)} FROM `{table}` "
            f"WHERE {(' OR ' if use_or else ' AND ').join([col + ' = ' + self.format_val(val) for col, val in zip(cols, vals)])} "
            f"{'' if not order else 'ORDER BY `' + order + '`'}"
        )
        print(qur)
        res = self.cursor.execute(qur)
        return res

    def sel_like(
        self,
        table: str,
        cols: list[str],
        vals: list[str],
        out_cols: list = None,
        order: str = None,
        use_or: bool = False,
    ):
        """以 like 查询

        Parameters
        ----------
        table : str
            要查询的表名
        cols : list[str]
            要查询的列
        vals : list[str]
            值
        out_cols : list, optional
            输出的列，默认全列
        order : str, optional
            以某列排序输出
        use_or : bool, optional
            使用or或and，默认and

        Returns
        -------
        _type_
            查询结果对象
        """
        assert len(cols) == len(vals), f"列[{len(cols)}]与值[{len(vals)}]的数目不相同"

        qur = (
            f"SELECT {'*' if not out_cols else ', '.join('`' + out_col + '`' for out_col in out_cols)} FROM `{table}` "
            f"WHERE {(' OR ' if use_or else ' AND ').join([col + ' LIKE ' + self.format_val(val) for col, val in zip(cols, vals)])} "
            f"{'' if not order else 'ORDER BY `' + order + '`'}"
        )
        print(qur)
        res = self.cursor.execute(qur)
        return res
        pass

    def add(self, table: str, cols: list[str], vals: list[str]):
        """插入语句

        Parameters
        ----------
        table : str
            要插入的表名
        cols : list[str]
            列的列表
        vals : list[str]
            值的列表

        Returns
        -------
        _type_
            查询结果对象
        """
        assert len(cols) == len(vals), f"列[{len(cols)}]与值[{len(vals)}]的数目不相同"

        qur = (
            f"INSERT INTO `{table}` ({', '.join([col for col in cols])}) VALUES "
            f"({', '.join([self.format_val(val) for val in vals])});"
        )
        print(qur)
        res = self.cursor.execute(qur)
        return res

    def delete(self, table: str, cols: list[str], vals: list, use_or: bool = False):
        """删除语句

        Parameters
        ----------
        table : str
            要查询的表
        cols : list[str]
            查询条件的列名
        vals : list
            查询条件的值
        use_or : bool, optional
            使用or或and，默认and

        Returns
        -------
        _type_
            查询结果对象
        """
        assert len(cols) == len(vals), f"列[{len(cols)}]与值[{len(vals)}]的数目不相同"

        qur = (
            f"DELETE FROM `{table}` "
            f"WHERE {(' OR ' if use_or else ' AND ').join([col + '=' + self.format_val(val) for col, val in zip(cols, vals)])};"
        )
        print(qur)
        res = self.cursor.execute(qur)
        return res

    def update(
        self,
        table: str,
        new_cols: list[str],
        new_vals: list[str],
        old_cols: list[str],
        old_vals: list[str],
        use_or: bool = False,
    ):
        """更新语句

        Parameters
        ----------
        table : str
            _description_
        new_cols : list[str]
            _description_
        new_vals : list[str]
            _description_
        old_cols : list[str]
            _description_
        old_vals : list[str]
            _description_
        use_or : bool, optional
            _description_, by default False

        Returns
        -------
        _type_
            查询结果对象
        """
        assert len(new_cols) == len(
            new_vals
        ), f"新列[{len(new_cols)}]与值[{len(new_vals)}]的数目不相同"
        assert len(old_cols) == len(
            old_vals
        ), f"旧列[{len(old_cols)}]与值[{len(old_vals)}]的数目不相同"

        qur = (
            f"UPDATE `{table}` "
            f"SET {', '.join([col + ' = ' + self.format_val(val) for col, val in zip(new_cols, new_vals)])} "
            f"WHERE {(' OR ' if use_or else ' AND ').join([col + '=' + self.format_val(val) for col, val in zip(old_cols, old_vals)])};"
        )
        print(qur)
        res = self.cursor.execute(qur)
        return res

    def format_val(self, s: str) -> str:
        """规范化字符串

        Parameters
        ----------
        s : str
            要处理的字符串

        Returns
        -------
        str
            处理后的字符串
        """
        if type(s) == str:
            s = emoji.demojize(s, delimiters=(" ", " "))
            s = s.replace(r"\"", '"').replace("\\", "").replace('"', r"\"")
            return '"' + s + '"'
        else:
            return str(s)

    def get_DictInList(self):
        res = self.cursor.fetchall()
        pass

    def ping(self):
        self._sjk.ping(reconnect=True)

    def commit(self):
        self._sjk.commit()


# OpenMySql的with版本
class OpenMiaoSql:
    """MySql的with版本"""

    sql = None

    def __init__(self, con: dict):
        self.sql = MiaoSql(con)

    def __enter__(self):
        return self.sql

    def __exit__(self, exc_type, exc_val, exc_tb):
        del self.sql
