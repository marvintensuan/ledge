import tomli

from fastapi import FastAPI
from sqlmodel import Session, create_engine

from Models.transactions import Transactions, TransactionCategory

with open("config.toml") as file:
    config = tomli.loads(file.read())
    db = config.get("db")

engine = create_engine(db.get("url"))

app = FastAPI()


@app.get("/tables/{table_name}")
async def read_from_table(table_name):
    with Session(engine) as session:
        ...
    return 200
