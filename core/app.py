import uvicorn
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware

from api.products import router as products_router
from core.configs import configs

app = FastAPI(
    responses={
        404: {"description": "Not found"},
        400: {"description": "Bad request"},
    }
)

app.add_middleware(
    DBSessionMiddleware,
    db_url=f"postgresql://{configs.DB_USER}:{configs.DB_PASSWORD}@{configs.DB_HOST}/{configs.DB_NAME}",
)

app.include_router(prefix="/v1", router=products_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
