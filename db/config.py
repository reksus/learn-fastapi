from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker
from config import settings

DATABASE_URL = settings.DATABASE_URL

engine = create_async_engine(DATABASE_URL, future=True, echo=True)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
Base = declarative_base()





# async def get_session():    
#     async with AsyncLocalSession() as session:
#         try:
#             async with session.begin():
#                 yield session
#         except Exception as e:
#             print(e)
#             await session.rollback()
#         finally:
#             await session.close()


# def async_session(func):
#     async def wrapper(*args, **kwargs):
#         async with get_session() as session:
#             return await func(session, *args, **kwargs)
#     return wrapper

