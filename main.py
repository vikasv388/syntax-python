"""
Crypto Market Analytics Application

Main FastAPI entry point.

Responsibilities:
- Create application instance
- Register routes
- Initialize database
- Start scheduler
"""

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.database.base import Base
from app.database.database import engine
from app.api.test_routes import router as test_router
from app.api.market_routes import router as market_router
from app.api.analytics_routes import router as analytic_router
from app.api.strategy_routes import router as strategy_router
from app.scheduler.market_scheduler import start_scheduler
from app.models import *


@asynccontextmanager
async def lifespan(app: FastAPI
    # Startup logic(create database tables)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    start_scheduler()

    yield  # Application runs here

    await engine.dispose()  # Shutdown logic


app = FastAPI(
    title="Crypto Market Analytics App",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(test_router
app.include_router(market_router)
app.include_router(analytic_router)
app.include_router(strategy_router

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/"
async def root(
    return {
        "message": "Crypto Market Analytics API Running"
    
