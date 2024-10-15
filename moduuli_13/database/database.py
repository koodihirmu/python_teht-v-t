import json

import mysql.connector


class Database:
    def __init__(self) -> None:
        # load different path if this file is being ran directly
        if __name__ == "__main__":
            with open("../../secret.json") as file:
                json_file = json.load(file)
        else:
            with open("secret.json") as file:
                json_file = json.load(file)

        self.cxn = mysql.connector.connect(
            host=json_file["database"]["host"],
            database=json_file["database"]["database"],
            user=json_file["database"]["user"],
            password=json_file["database"]["password"],
            autocommit=json_file["database"]["autocommit"],
        )
        self.cursor = self.cxn.cursor(dictionary=True)

    def fetch_row(self, table, operator, id: dict) -> dict:
        sql = f"""
        SELECT * FROM {table} WHERE {list(id.keys())[0]} {operator} "{id['ident']}"
        """
        self.cursor.execute(sql)
        data = self.cursor.fetchone()
        if data is not None:
            return dict(data)
        else:
            return None


if __name__ == "__main__":
    try:
        db = Database()
        print(db.fetch_row("airport", "=", {"ident": "EFHK"}))
    except Exception as e:
        print(e)
    input("Press Enter ...")
