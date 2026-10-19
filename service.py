from sqlalchemy import select, desc
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.market_data import MarketData
from app.models.strategy_result import StrategyResult
from app.strategy.moving_average_strategy import MovingAverageStrategy


class StrategyService:
@staticmethod
async def run_strategy(db: AsyncSession):
result = await db.execute(
    select(MarketData.symbol)
    .distinct()
)

symbols = result.scalars().all()

    signals = []

        for symbol in symbols:

            history_result = await db.execute(
                select(MarketData)
                .where(MarketData.symbol == symbol)
                .order_by(desc(MarketData.timestamp))
                .limit(10)
            )

            history = history_result.scalars().all()

            prices = [item.price for item in history]

            signal = MovingAverageStrategy.generate_signal(prices)

            strategy_result = StrategyResult(symbol=symbol, signal=signal)

            db.add(strategy_result)

            signals.append(
                {
                    "symbol": symbol,
                    "signal": signal
                }
            )

        await db.commit()

        return signals[:10]

    @staticmethod
    async def get_strategy_results(db: AsyncSession):
    result = await db.execute(
        select(StrategyResult)
        .order_by(desc(StrategyResult.created_at))
    )

    strategy = result.scalars().all()

    return strategy
