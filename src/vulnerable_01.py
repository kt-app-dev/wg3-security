import os
import sqlite3

# --- 1. コマンドインジェクション ---
def command_injection(user_input):
    os.system("ls " + user_input)


# --- 2. SQLインジェクション ---
def sql_injection(user_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = '" + user_id + "';")
    return cursor.fetchall()



# --- テスト用の関数呼び出し ---
if __name__ == "__main__":
    command_injection("; echo Hungry")
    sql_injection("1=1")
