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
from pytest import mark, fixture


def main(page: ft.Page):
    views_handler(page)["/"](page)



def session_db():
    load_dotenv()
    username = os.getenv("USER_NAME")
    password = os.getenv("PASSWORD")
    host = os.getenv("HOST")
    database = os.getenv("DATABASE")
    EntityInterface.engine = create_engine(
        f"mysql+pymysql://{username}:{password}@{host}/{database}"
    )
    EntityInterface.base.metadata.create_all(EntityInterface.engine)
    EntityInterface.session_maker = sessionmaker(bind=EntityInterface.engine)
    EntityInterface.session = EntityInterface.session_maker()

    # return EntityInterface.session
    ft.app(target=main)


def test_add_category_with_cedilla_in_categoryName():
    main()
    
    teste = add_category(page: ft.Page)

    print(teste)
    # failCategory = Category(name="alçapao", color="#FFFFFF")
