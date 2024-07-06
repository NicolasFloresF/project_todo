# importing project modules
from project_todo.views.add_category import *
from project_todo.views.add_event import *
from project_todo.views.main_menu import *

# importing third-party modules
import flet as ft


def views_handler(page: ft.Page):
    return {
        "/": ft.View(
            route="/",
            controls=[main_menu(page)],
        ),
        "/add_category": ft.View(
            route="/add_category",
            controls=[add_category(page)],
        ),
        "/add_event": ft.View(
            route="/add_event",
            controls=[add_event(page)],
        ),
    }
