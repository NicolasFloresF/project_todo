# importing project modules
from project_todo.views.add_category import *
from project_todo.views.add_event import *
from project_todo.views.main_menu import *
from project_todo.views.alter_category import *
from project_todo.views.alter_event import *
from project_todo.views.alter_occurrence import *

# importing third-party modules
import flet as ft


def views_handler(page: ft.Page, update: int = None):
    page.clean()
    return {
        "/": main_menu,
        "/add_category": add_category,
        "/add_event": add_event,
        "/alter_category": alter_category,
        "/alter_event": alter_event,
        "/alter_occurrence": alter_occurrence,
    }
