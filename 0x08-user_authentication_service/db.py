#!/usr/bin/env python3

"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

from user import Base, User


def has_keys(**kwargs):
    """
    If all the keys in the kwargs dictionary are not in the properties list,
    raise an error."
    """
    properties = ['id', 'email', 'hashed_password',
                  'session_id', 'reset_token']
    result = all(
        [True if key in properties else False for key in kwargs.keys()])
    if not result:
        raise(InvalidRequestError("Invalid request"))
    return True


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str):
        """Add a new user to the DB
         """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """Find a user by parameters
        """
        has_keys(**kwargs)
        try:
            user = self._session.query(User).filter_by(**kwargs).one()
        except NoResultFound:
            raise NoResultFound("No user found")
        return user

    def update_user(self, user_id: int, **kwargs):
        """Update a user by parameters """
        has_keys(**kwargs)
        user_found = self.find_user_by(id=user_id)
        [setattr(user_found, key, value) for key, value in kwargs.items()]
        return None
