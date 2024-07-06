""" This module defines the Occurrence entity, representing an occurrence of a determined event. """

# importing project modules
from project_todo.common.entity_Interface import EntityInterface

# importing third-party modules
from sqlalchemy import Column, Integer, Date, Time, Boolean


class Occurrence(EntityInterface.base, EntityInterface):
    """This class defines the Occurrence entity, representing an occurrence of a determined event."""

    # defining the table name
    __tablename__ = "Occurrence"

    # defining the table columns
    # +------------------------+---------+------+-----+---------+----------------+
    # | Field                  | Type    | Null | Key | Default | Extra          |
    # +------------------------+---------+------+-----+---------+----------------+
    # | id                     | int     | NO   | PRI | NULL    | auto_increment |
    # | OccurrenceDeadlineDate | date    | NO   |     | NULL    |                |
    # | Event_idEvent          | int     | NO   | MUL | NULL    |                |
    # | OccurrenceStatus       | tinyint | NO   |     | NULL    |                |
    # +------------------------+---------+------+-----+---------+----------------+

    id = Column(Integer, primary_key=True, autoincrement=True)
    OccurrenceDeadlineDate = Column(Date, nullable=False)
    Event_idEvent = Column(Integer)
    OccurrenceStatus = Column(Boolean, nullable=False)

    def __init__(self, deadlineDate: Date, idEvent: Integer, status: bool) -> object:
        """Occurrence constructor method

        Args:
            deadlineDate (Date): The occurrence deadline date
            deadlineTime (Time): The occurrence deadline time
            idEvent (Integer): The event ID
            status (bool): The occurrence status, indicating if it is done or not

        Returns:
            object: Initialized Occurrence instance
        """
        self.id = Occurrence.all()[-1].id + 1
        self.OccurrenceDeadlineDate = deadlineDate
        self.Event_idEvent = idEvent
        self.OccurrenceStatus = status

        # Calling the parent class (EntityInterface) initialization method
        EntityInterface.__init__(self)
