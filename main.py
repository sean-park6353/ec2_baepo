from fastapi import FastAPI
from routes.user.user_route import user_router
from starlette.middleware.cors import CORSMiddleware
app = FastAPI()

app.include_router(user_router)

origins = [
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def main():
    return "123"