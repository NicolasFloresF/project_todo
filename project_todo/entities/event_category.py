""" This module defines the EventCategory entity, representing the relationship between events and categories. """

# importing project modules
from project_todo.common.entity_Interface import EntityInterface

# importing third-party modules
from sqlalchemy import Column, Integer


class EventCategory(EntityInterface.base, EntityInterface):
    """This class defines the EventCategory entity, representing the relationship between events and categories."""

    # defining the table name
    __tablename__ = "EventCategory"

    # defining the table columns
    # +---------------------+------+------+-----+---------+----------------+
    # | Field               | Type | Null | Key | Default | Extra          |
    # +---------------------+------+------+-----+---------+----------------+
    # | Category_idCategory | int  | NO   | MUL | NULL    |                |
    # | Event_idEvent       | int  | NO   | MUL | NULL    |                |
    # | id                  | int  | NO   | PRI | NULL    | auto_increment |
    # +---------------------+------+------+-----+---------+----------------+

    id = Column(Integer, primary_key=True, autoincrement=True)
    Category_idCategory = Column(Integer)
    Event_idEvent = Column(Integer)

    def __init__(self, idCategory: int, idEvent: int) -> object:
        """EventCategory constructor method

        Args:
            idCategory (int): The category ID
            idEvent (int): The event ID

        Returns:
            object: Initialized EventCategory instance
        """

        self.Category_idCategory = idCategory
        self.Event_idEvent = idEvent

        # Calling the parent class (EntityInterface) initialization method
        EntityInterface.__init__(self)
