""" This is the main module of the project, responsible for running the application and calling the necessary methods. """

# importing project modules
from project_todo.common import *
from project_todo.entities import *
from project_todo.views import *

# importing third-party modules
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
import flet as ft
from datetime import date, time


def main(page: ft.Page):
    # page.title = "To-Do App"
    # page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    # page.update()
    #
    ## create application instance
    # todo = TodoApp()
    #
    ## add application's root control to the page
    # page.add(todo)
    # todo.refresh()
    # for event in Event.all():
    #    print(event.eventName)

    # page.add(main_menu())
    main_menu(page)


if __name__ == "__main__":

    load_dotenv()
    username = os.getenv("USER_NAME")
    password = os.getenv("PASSWORD")
    host = os.getenv("HOST")
    database = os.getenv("DATABASE")
    EntityInterface.engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}/{database}")
    EntityInterface.base.metadata.create_all(EntityInterface.engine)
    EntityInterface.session_maker = sessionmaker(bind=EntityInterface.engine)
    EntityInterface.session = EntityInterface.session_maker()
    ft.app(target=main)
