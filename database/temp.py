from fastapi import FastAPI
from sqlalchemy import create_engine, text


def add_server(server_name: str):
    host = "db1.spareroom.com"
    username = "professor"
    password = "Bin-Table-Keyboard9"

    engine = create_engine(
        f"postgresql://{username}:{password}@{host}/runescape",
    )

    sql_query = text("""
    INSERT INTO servers (name, active)
    VALUES (:name, :active)
    """)

    value = {
        "name": server_name,
        "active": True,
    }

    with engine.connect() as conn:
        conn.execute(sql_query, value)
        return conn.commit()
