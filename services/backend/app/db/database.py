from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..core import config

# 엔진 생성 create_async_engine() 알아볼것
db_engine = create_engine(config.DATABASE_URL)
# 세션 생성
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)


# 세션을 반환하는 함수
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
