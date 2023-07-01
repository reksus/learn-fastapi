from db.config import async_session
from db.dals.book_dal import BookDAL


async def get_book_dal():
    async with async_session() as session:
        try:
            async with session.begin():
                yield BookDAL(session)
        except: 
            await session.rollback()
        finally:
            await session.close()


async def get_async_session():
    async with async_session() as session:
        try:
            async with session.begin():
                yield session
        except: 
            await session.rollback()
        finally:
            await session.close()