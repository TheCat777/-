import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session
import sqlalchemy.ext.declarative as dec

SqlAlchemyBase = dec.declarative_base()

session_factory = None


def global_init(db_file):
    global session_factory, sa, orm

    if session_factory:
        return

    conn_str = f'sqlite:///{db_file.strip()}?check_same_thread=False'
    print("Подключение к БД")

    engine = sa.create_engine(conn_str, echo=False)
    session_factory = orm.sessionmaker(bind=engine)

    from .Models import Users, Posts, Comments

    SqlAlchemyBase.metadata.create_all(engine)


def create_session() -> Session:
    global session_factory
    return session_factory()
