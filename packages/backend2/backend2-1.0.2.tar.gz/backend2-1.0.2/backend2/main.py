import uvicorn
from fastapi import FastAPI
from backend2.db.database import engine, Base
from fastapi.middleware.cors import CORSMiddleware
from backend2.routers.test import router as test_router
from backend2.routers.table import router as table_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    openapi_url="/backend2/openapi.json",
    docs_url="/backend2/docs"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(test_router)
app.include_router(table_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


