import psycopg2
import os
from psycopg2.extras import RealDictCursor

from config import DATABASE
from config import SQL_ROOT_PATH


class BaseProvider:
    """
    Базовый класс для работы с БД
    """
    def __init__(self, module_sql_path):
        """
        При совершение запроса
        """
        self.query = None
        self.connect, self.current_connect = BaseProvider.connect()
        self.sql_root = os.path.join(SQL_ROOT_PATH, module_sql_path)
        self.is_debug = False

    def __del__(self):
        """
        После завершения обработки запроса
        """
        self.connect.commit()
        self.connect.close()

    @staticmethod
    def import_sql(sql_root, name):
        with open(os.path.join(sql_root, name), encoding='utf-8', mode='r') as _fne:
            return _fne.read()

    def exec_by_file(self, name, params):
        query = self.import_sql(self.sql_root, name)
        return self.exec(query, params)

    def execute(self):
        if self.is_debug:
            print(self.query)
        return self.exec(self.query)

    @staticmethod
    def connect():
        """
        Метод подключения к бд
        :return:
        """
        config_connect = "dbname='{dbname}' user='{user}' host='{host}' password='{password}'"
        connect = psycopg2.connect(config_connect.format(**DATABASE))
        return connect, connect.cursor(cursor_factory=RealDictCursor)

    @staticmethod
    def exec(query=None, args=None, file=None):
        """
        Метод для выполнения sql запроса
        :param query:
        :param args:
        :param file:
        :return:
        """
        return BaseProvider._switch(query=query, args=args, file=file)

    @staticmethod
    def _switch(query=None, args=None, file=None):
        """
        Метод разводящий - для выбора режима sql запроса
        с аргументами
        без аргументов
        файл с аргументами
        файл без аргументов
        :param query:
        :param args:
        :param file:
        :return:
        """
        if query and args:
            return BaseProvider._query_exec_args(query, args)
        if query and not args:
            return BaseProvider._query_exec(query)
        if file and args:
            return BaseProvider._query_file_args_exec(file, args)
        if file:
            return BaseProvider._query_file_exec(file)
        return

    @staticmethod
    def _query_exec(query):
        """
        Выполнить sql без аргументов
        :param query:
        :return:
        """
        return BaseProvider._exec(query)

    @staticmethod
    def _query_file_exec(file):
        """
        Метод вычитывает sql запрос из файла и исполняет его без аргументов
        :param file:
        :return:
        """
        with open(file, 'r') as f:
            query = f.read()
            return BaseProvider._exec(query)

    @staticmethod
    def _query_file_args_exec(file, args):
        """
        Метод вычитывает sql запрос из файла и исполняет его с аргументами
        :param file:
        :param args:
        :return:
        """
        with open(file, 'r') as f:
            query = f.read().format(**args)
            return BaseProvider._exec(query)

    @staticmethod
    def _query_exec_args(query, args):
        """
        Метод выполняет sql запрос с аргументами
        :param query:
        :param args:
        :return:
        """
        for k, v in args.items():
            alert_items = ['"', ';', '*', 'drop', 'select', '=', 'insert']
            if isinstance(v, str):
                if "'" not in args[k]:
                    args[k] = f"'{args[k]}'"
                for alert in alert_items:
                    if alert in v:
                        args[k] = args[k].replace(alert, '')
        query = query.format(**args).replace('None', 'Null')
        # print(query)
        return BaseProvider._exec(query)

    @staticmethod
    def _exec(query):
        """
        Метод выполняет SQL запрос к базе
        :param query: str SQL запрос
        :return: dict результат выполнения запроса
        """
        connect, current_connect = BaseProvider.connect()
        current_connect.autocommit = True
        result = None
        try:
            current_connect.execute(query)
            connect.commit()
        except psycopg2.Error as e:
            print(e.pgerror)
            print(e.diag.message_primary)
        finally:
            try:
                result = current_connect.fetchall()
            except:
                pass
            finally:
                connect.close()
                # print(result)
                return result
