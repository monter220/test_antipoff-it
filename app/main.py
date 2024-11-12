import uvicorn
from fastapi import FastAPI

from api import router as api_router


app = FastAPI(
    redoc_url=None,
)
app.include_router(api_router)


if __name__ == '__main__':
    uvicorn.run('main:app',
                reload=True,
                port=9000,
                host='localhost',
                forwarded_allow_ips='*')
