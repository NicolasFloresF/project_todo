""" This module defines the Event entity, representing an event to be done. """

# importing project modules
from project_todo.common.entity_Interface import EntityInterface
from project_todo.entities.event_category import EventCategory
from project_todo.entities.category import Category

# importing third-party modules
from sqlalchemy import Column, Integer, String, DateTime, Boolean


class Event(EntityInterface.base, EntityInterface):
    """This class defines the Event entity, representing an event to be done."""

    # defining the table name
    __tablename__ = "Event"

    # defining the table columns
    # +-------------------+--------------+------+-----+---------+----------------+
    # | Field             | Type         | Null | Key | Default | Extra          |
    # +-------------------+--------------+------+-----+---------+----------------+
    # | id                | int          | NO   | PRI | NULL    | auto_increment |
    # | eventName         | varchar(45)  | NO   |     | NULL    |                |
    # | eventDate         | datetime(6)  | NO   |     | NULL    |                |
    # | event_description | varchar(255) | YES  |     | NULL    |                |
    # | eventPriority     | varchar(45)  | YES  |     | NULL    |                |
    # | EventHasDeadline  | tinyint      | NO   |     | NULL    |                |
    # | EventStatus       | tinyint      | NO   |     | NULL    |                |
    # +-------------------+--------------+------+-----+---------+----------------+

    id = Column(Integer, primary_key=True, autoincrement=True)
    eventName = Column(String(45), nullable=False)
    eventDate = Column(DateTime, nullable=False)
    event_description = Column(String(255), nullable=True)
    eventPriority = Column(String(45), nullable=True)
    EventHasDeadline = Column(Boolean, nullable=False)
    EventStatus = Column(Boolean, nullable=False)

    def __init__(
        self, name: str, date: DateTime, description: str, priority: str, deadline: bool, status: bool
    ) -> object:
        """Event constructor

        Args:
            name (str): The event name
            date (DateTime): The event creation date
            description (str): The event description
            priority (str): The event priority
            deadline (bool): Boolean indicating if the event has a deadline

        Returns:
            object: Initialized Event instance
        """

        self.eventName = name
        self.eventDate = date
        self.event_description = description
        self.eventPriority = priority
        self.EventHasDeadline = deadline
        self.EventStatus = status

        # Calling the parent class (EntityInterface) initialization method
        EntityInterface.__init__(self)

    @property
    def categories(self) -> list:
        """Returns the categories of the event.

        Returns:
            list: List of categories of the event.
        """

        cats = [Category.find_by_id(cat.id) for cat in EventCategory.all() if cat.Event_idEvent == self.id]
        return cats
