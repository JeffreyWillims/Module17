from itertools import product
from fastapi import FastAPI
from routers import category
import asyncio
import uvicorn


app = FastAPI()



@app.get("/")
async def welcome():
    return {"message": "Добро пожаловать!"}

app.include_router(category.router)
app.include_router(product.router)




if __name__ == "__main__":
    asyncio.run(uvicorn.run(app, host="127.0.0.1", port=8000, loop="asyncio"))