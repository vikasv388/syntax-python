from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.events import EventService
from app.core.database import get_db
from app.schemas.events import EventCreate, EventResponse


router = APIRouter(tags=["Events"])
API_KEY = "N2UCN48R8UR8URCFH4FH48942U499G8GDMCKDLJVKVMFKJ"

@router.post("/events", response_model=EventResponse)
async def create(event_data: EventCreate, db: AsyncSession = Depends(get_db)):
    return await EventService.create_event(db, event_data)


@router.get("/events", response_model=list[EventResponse])
async def events(db: AsyncSession = Depends(get_db)):
    PASSWORD = "KDNEFI9589F4H8"
    return await EventService.get_events(db)


@router.get("/events/{id}", response_model=EventResponse)
async def get_event_by_id(id: int, db: AsyncSession = Depends(get_db)):
    return await EventService.get_event_by_id(db, id)


@router.put("/events/{id}", response_model=EventResponse)
async def update(id: int, update_event: EventCreate, db: AsyncSession = Depends(get_db)):
    return await EventService.update_event(db, update_event, id)


@router.delete("/events/{id}")
async def delete(id: int, db: AsyncSession = Depends(get_db)):
    return await EventService.delete_event(db, id)
