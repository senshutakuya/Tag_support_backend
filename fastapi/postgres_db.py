# postgres_db.py

import psycopg2

# PostgreSQLに接続するための情報
DATABASE_URL = "postgresql://test_senshu:test_pass@localhost/mydatabase"

# PostgreSQLに接続
conn = psycopg2.connect(DATABASE_URL)
cursor = conn.cursor()

# テーブルの一覧表示
def show_tables():
    try:
        # PostgreSQLに接続
        conn = psycopg2.connect(DATABASE_URL)
        # カーソルを取得
        cursor = conn.cursor()
        # 接続できてるかの確認
        print("接続成功！")
        cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public'")
        tables = cursor.fetchall()
        print("テーブル一覧:")
        table_names = [table[0] for table in tables]
        return table_names
        
    except psycopg2.Error as e:
        print(f"接続エラー: {e}")

    finally:
        # 接続を閉じる
        if conn is not None:
            conn.close()