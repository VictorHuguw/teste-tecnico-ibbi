from fastapi import FastAPI
from app.routes import hello_route

app = FastAPI()

# Inclui a rota do módulo hello_route
app.include_router(hello_route.router)

@app.get("/")
def read_root():
    return {"message": "Go to /hello to see the greeting."}
