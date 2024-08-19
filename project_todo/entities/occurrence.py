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

    @classmethod
    def delete_by_event_id(cls, event_id: int):
        """Deletes all Occurrence instances with the given event ID.

        Args:
            event_id (int): The event ID
        """
        # Gathering the instance by its ID
        instance = EntityInterface.session.query(Occurrence).filter(Occurrence.Event_idEvent == event_id).first()

        while instance:
            # Removing the instance from the database
            EntityInterface.session.delete(instance)

            # Confirming the transaction
            EntityInterface.session.commit()

            print(f"Instância {id} deletada com sucesso.")

            instance = EntityInterface.session.query(Occurrence).filter(Occurrence.Event_idEvent == event_id).first()
        else:
            print(f"Instância com ID {id} não encontrada.")
