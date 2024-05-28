import sqlalchemy as sa
from sqlalchemy import orm
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as sa
from sqlalchemy_utils import database_exists, create_database
from datetime import datetime as dt

class DbSqlA:
    base        = declarative_base()
    #fast_executemany=True,
    #pool_size=10,
    #max_overflow=2,
    #pool_recycle=300,
    #pool_pre_ping=True,
    #pool_use_lifo=True
    def __init__(self,ConnectionString,**kwargs):
        self.engine                 = sa.create_engine(ConnectionString, **kwargs)
        self.session                = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=self.engine))
        self.base.query             = self.session.query_property()
        self.orm_session            = orm.scoped_session(orm.sessionmaker())(bind=self.engine)
        self.base.metadata.bind     = self.engine    

    def create_all(self):
        if not database_exists(self.engine.url):
            create_database(self.engine.url)
        self.base.metadata.create_all(self.engine)


def tblUts(db):
    class auxDB:
        id      = sa.Column(sa.Integer,primary_key=True,autoincrement=True)

        def save(self):
            try:
                if not self.id:
                    db.session.add(self)
                db.session.commit()
            except:
                db.session.rollback()
                raise

        def delete(self):
            db.session.rollback()
            db.session.delete(self)
            db.session.commit()
    
    
    return auxDB

