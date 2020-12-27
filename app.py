async def on_startup(dp):
    import filters
    import middlewares
    filters.setup(dp)
    middlewares.setup(dp)

    from utils.notify_admins import on_startup_notify
    await on_startup_notify(dp)


async def month_report():
    """Отчет за месяц"""

    import asyncio
    from utils.report import month_report

    while True:
        await month_report()
        await asyncio.sleep(86400)


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    dp.loop.create_task(month_report())
    executor.start_polling(dp, on_startup=on_startup)
