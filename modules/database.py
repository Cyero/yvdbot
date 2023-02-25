import psycopg2
import sqlite3
import os


def get_db_env() -> str:
    dbname = os.getenv('PGDATABASE')
    user = os.getenv('PGUSER')
    password = os.getenv('PGPASSWORD')
    port = os.getenv('PGPORT')
    host = os.getenv('PGHOST')
    if host is None and port is None:
        cfg = f"dbname={dbname} user={user} password={password}"
        return cfg
    elif host is not None and port is None:
        cfg = f"dbname={dbname} user={user} password={password} host={host}"
        return cfg
    elif host is None and port is not None:
        cfg = f"dbname={dbname} user={user} password={password} port={port}"
        return cfg
    else:
        cfg = f"dbname={dbname} user={user} password={password} port={port} host={host}"
        return cfg


class Database:
    def __init__(self, db_config: str) -> None:
        try:
            self.connection = psycopg2.connect(db_config)
            self.id_type = "serial PRIMARY KEY"
            self.user_id_type = "bigint NOT NULL"
        except psycopg2.OperationalError:
            self.connection = sqlite3.connect('./src/users.db')
            self.id_type = "INTEGER PRIMARY KEY AUTOINCREMENT"
            self.user_id_type = "TEXT NOT NULL"
        self.cursor = self.connection.cursor()

    def user_existing(self, user_id) -> None:
        with self.connection:
            self.cursor.execute(f"SELECT * FROM users WHERE user_id = ({user_id})")
            result = self.cursor.fetchmany(1)
            if bool(len(result)) is not True:
                self.cursor.execute(f"INSERT INTO users (user_id) VALUES ({user_id})")
                self.connection.commit()
            else:
                self.cursor.execute(f"UPDATE users SET active = (1) WHERE user_id = ({user_id})")
                self.connection.commit()

    def check_table_existing(self) -> None:
        with self.connection:
            self.cursor.execute(f"CREATE TABLE IF NOT EXISTS users (id {self.id_type}, user_id {self.user_id_type}, "
                                f"active integer DEFAULT 1)")
            self.connection.commit()

    def set_activity(self, user_id, active) -> None:
        with self.connection:
            self.cursor.execute(f"UPDATE users SET active = ({active}) WHERE user_id = ({user_id})")
            self.connection.commit()

    def get_user(self) -> list:
        with self.connection:
            self.cursor.execute("SELECT user_id FROM users WHERE active = (1) ")
            result = self.cursor.fetchall()
            return result

    def drop_db(self) -> None:
        with self.connection:
            self.cursor.execute("DROP TABLE IF EXISTS users")
            self.check_table_existing()
            self.connection.commit()

    def close_db(self) -> None:
        self.connection.close()
