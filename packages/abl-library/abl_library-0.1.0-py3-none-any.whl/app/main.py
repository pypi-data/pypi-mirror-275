from fastapi import FastAPI
from app.routes import ping, hello, authors, pubsub

app = FastAPI()

app.include_router(ping.router)
app.include_router(hello.router)
# app.include_router(authors.router)
# app.include_router(pubsub.router)

@app.on_event("startup")
async def startup_event():
    print("Application startup")

@app.on_event("shutdown")
async def shutdown_event():
    print("Application shutdown")
