from fastapi import FastAPI
import uvicorn

from .routes.v1 import endpoints

app = FastAPI()

app.include_router(endpoints.router, prefix="/v1")

def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()
