#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm import scoped_session
import uuid

from user import Base, User

attList = [
            'id',
            'email',
            'hashed_password',
            'session_id',
            'reset_token'
        ]


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

    def add_user(self, email: str, hashed_password: str) -> User:
        """creates and saves a user to DB"""
        email_ = email
        hashed_ = hashed_password

        Base.metadata.create_all(self._engine)
        session_factory = sessionmaker(bind=self._engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session

        user = User(
            email=email_,
            hashed_password=hashed_,
        )
        Session.add(user)
        Session.commit
        Session.query(User).one()
        return user

    def find_user_by(self, **kwargs) -> User:
        """find a user by given attribute"""

        session = self.__session
        for x in kwargs.keys():
            if x not in attList:
                raise InvalidRequestError

        return session.query(User).filter_by(**kwargs).one()

    def update_user(self, user_id: int, **kwargs) -> None:
        """updates a user with keyword args"""
        user = self.find_user_by(id=user_id)

        for k, v in kwargs.items():
            if k in attList:
                setattr(user, k, v)
            else:
                raise ValueError

            self._session.add(user)
            self._session.commit
            self._session.query(User)
