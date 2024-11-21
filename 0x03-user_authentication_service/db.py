#!/usr/bin/env python3
"""
BD class
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from user import Base, User


class DB:

    def __init__(self):
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add a new user to the database and return the User object

        Args:
            email (string): email of user
            hashed_password (string): password of user

        Returns:
            User: user created or None if email or hashed_password
            is not provided
        """
        if not email or not hashed_password:
            return None
        user = User(email=email, hashed_password=hashed_password)
        session = self._session
        session.add(user)
        session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """Find a user by arbitrary keyword arguments

        Args:
            kwargs (dict): arbitrary keyword arguments

        Returns:
            User: user found

        Raises:
            NoResultFound: if no user is found
            InvalidRequestError: if invalid query arguments are passed
        """
        session = self._session
        try:
            return session.query(User).filter_by(**kwargs).one()
        except NoResultFound:
            raise NoResultFound("No user found with the given criteria")
        except InvalidRequestError:
            raise InvalidRequestError("Invalid query arguments")

    def update_user(self, user_id: int, **kwargs) -> None:
        """Update a user's attributes

        Args:
            user_id (int): ID of the user to update
            kwargs (dict): arbitrary keyword arguments for the attributes
                           to update

        Returns:
            None

        Raises:
            ValueError: if an argument does not correspond to a user attribute
        """
        session = self._session
        user = self.find_user_by(id=user_id)
        for key, value in kwargs.items():
            if not hasattr(user, key):
                raise ValueError(f"Attribute {key} does not exist on User")
            setattr(user, key, value)
        session.commit()
