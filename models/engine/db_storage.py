#!/usr/bin/python3
"""Create DBStorage class"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, scoped_session, sessionmaker
from models.user import User
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from os import getenv


class DBStorage:
    """Define DBStorage class"""
    __engine = None
    __session = None

    def __init__(self):
        """Define a constructor"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            """drop all tables if the environment
            variable HBNB_ENV is equal to test"""
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Define all method"""
        if cls is None:
            objs = self.__session.query(State).all()
            objs.extend(self.__session.query(City).all())
            objs.extend(self.__session.query(User).all())
            objs.extend(self.__session.query(Place).all())
            objs.extend(self.__session.query(Review).all())
            objs.extend(self.__session.query(Amenity).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            objs = self.__session.query(cls)
        return {"{}.{}".format(type(o).__name__, o.id): o for o in objs}

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Define reload method"""
        Base.metadata.create_all(self.__engine)

        Session = sessionmaker(bind=self.__engine,
                               expire_on_commit=False)
        self.__session = Session()

    def close(self):
        """Define close method"""
        self.__session.close()
