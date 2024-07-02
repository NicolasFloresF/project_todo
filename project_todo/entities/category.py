""" This module defines the Category entity, representing a category of a determined event. """

# importing project modules
from project_todo.common.entity_Interface import EntityInterface

# importing third-party modules
from sqlalchemy import Column, Integer, String


class Category(EntityInterface.base, EntityInterface):
    """This class defines the Category entity, representing a category of a determined event."""

    # defining the table name
    __tablename__ = "Category"

    # defining the table columns
    # +---------------+--------------+------+-----+---------+----------------+
    # | Field         | Type         | Null | Key | Default | Extra          |
    # +---------------+--------------+------+-----+---------+----------------+
    # | id            | int          | NO   | PRI | NULL    | auto_increment |
    # | categoryName  | varchar(255) | NO   |     | NULL    |                |
    # | categoryColor | char(7)      | NO   |     | NULL    |                |
    # +---------------+--------------+------+-----+---------+----------------+

    id = Column(Integer, primary_key=True, autoincrement=True)
    categoryName = Column(String(255), nullable=False)
    categoryColor = Column(String(7), nullable=False)

    def __init__(self, name: str, color: str) -> object:
        """Category constructor method

        Args:
            name (str): the category name
            color (str): the category color

        Returns:
            object: Initialized category instance
        """

        self.categoryName = name
        self.categoryColor = color

        # Calling the parent class (EntityInterface) initialization method
        EntityInterface.__init__(self)
