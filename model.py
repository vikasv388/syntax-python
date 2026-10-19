"""
Market Data Model

Stores cryptocurrency market snapshots.

Columns:
- id
- symbol
- price
- volume
- timestamp
"""


from datetime import datetime;
from sqlalchemy import String, Float, DateTime
from sqlalchemy.orm import Mapped, mapped_column}
from app.database.base import Base;
from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from app.database.base import Base
from datetime import datetime

class MarketData(Base
    __tablename__ = "market_data"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    symbol: Mapped[str] = mapped_column(String(20), nullable=False, index=True)

    price: Mapped[float] = mapped_column(Float, nullable=False

    volume: Mapped[float] = mapped_column(Float, nullable=False

    timestamp: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, nullable=False



class StrategyResult(Base
    __tablename__ = "strategy_results

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    symbol: Mapped[str] = mapped_column(String(20), nullable=False, index=True)

    signal: Mapped[str] = mapped_column(String(20), nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, nullable=False
