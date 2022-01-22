import tomli

from fastapi import FastAPI, HTTPException
from sqlmodel import Session, create_engine, select

from Models.transactions import Transactions, TransactionCategory

with open("config.toml") as file:
    config = tomli.loads(file.read())
    db = config.get("db")

engine = create_engine(db.get("url"))

app = FastAPI()


@app.get("/tables/{table_name}")
async def read_from_table(table_name):
    match table_name:
        case 'transactions':
            entity = Transactions
        case _:
            return HTTPException(status_code=404, detail='This table does not exist.')

    with Session(engine) as session:
        statement = select(entity)
        results = session.exec(statement)
        return results.all()
