""" ... """

# importing project modules
from project_todo.common import *
from project_todo.entities import *
from project_todo.views import *

# importing third-party modules
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main(): ...


if __name__ == "__main__":

    # can i access a database whitout password? (the root user does not have a password)
    # how to create environment variables to store the database data?
    EntityInterface.engine = create_engine("mysql+pymysql://root:@localhost/")
    EntityInterface.base.metadata.create_all(EntityInterface.engine)
    EntityInterface.session_maker = sessionmaker(bind=EntityInterface.engine)
    EntityInterface.session = EntityInterface.session_maker()
    main()
