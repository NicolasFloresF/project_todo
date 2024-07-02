"""This module defines the EntityInterface class, which is a generic class for entity manipulation."""

# importing third-party modules
from sqlalchemy.orm import declarative_base
from sqlalchemy import func


class EntityInterface:
    """This class defines basic methods for generic entity manipulation."""

    base = declarative_base()

    def __init__(self) -> object:
        """initializes the object and registers it in the database.

        Returns:
            object: Instance of the class being instantiated.
        """

        self.id = (
            EntityInterface.session.query(func.count(self.__class__.id)).scalar() + 1
        )

        # Registering the instance in the database
        EntityInterface.session.add(self)

        # Confirming the registration
        EntityInterface.session.commit()

    @classmethod
    def all(cls) -> list:
        """Returns the list of created objects of a given class.

        Returns:
            list: List of objects from a given class.
        """
        return EntityInterface.session.query(cls).all()

    @classmethod
    def update(cls, id: int, new_attributes: dict):
        """Updates an instance

        Args:
            id (int): ID of the instance to be updated
            new_attributes (dict): Dictionary with de new atrributes of the instance
        """

        # get the instance by its ID
        instance = EntityInterface.session.query(cls).filter(cls.id == id).first()

        # update the instance with the new attributes
        if instance:
            for key, value in new_attributes.items():
                setattr(instance, key, value)

        # confirm the update
        EntityInterface.session.commit()

    @classmethod
    def delete(cls, id: int):
        """Delete an instance by its ID

        Args:
            id (int): ID of the instance to be deleted
        """

        # get the instance by its ID
        instance = EntityInterface.session.query(cls).filter(cls.id == id).first()

        # delete the instance
        if instance:
            EntityInterface.session.delete(instance)

        # confirm the deletion
        EntityInterface.session.commit()
