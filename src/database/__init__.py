from settings import DATABASE_URL
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

engine = create_engine(DATABASE_URL)#, pool_pre_ping=False, pool_recycle=3600, echo_pool=False)
session_local = sessionmaker(bind=engine)


def get_db():
    session: Session = session_local()
    try:
        yield session
        session.commit()
    except Exception as exc:
        session.rollback()
        raise exc
    finally:
        session.close()
