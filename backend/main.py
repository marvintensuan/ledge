from fastapi import FastAPI

app = FastAPI()

@app.get("/tables/{table_name}")
async def read_from_table(table_name):
    return 200