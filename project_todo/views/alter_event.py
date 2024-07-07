# importing project modules
from project_todo.entities.event import Event
from project_todo.entities.occurrence import Occurrence
from project_todo.entities.event_category import EventCategory
from project_todo.entities.category import Category

# importing third-party modules
import datetime
import flet as ft


class CategoriesRow(ft.Column):
    def __init__(self, id: int, catDelete):
        super().__init__()

        category = Category.find_by_id(id)
        self.id = id
        self.name = category.categoryName
        self.color = category.categoryColor
        self.cat_delete = catDelete

        self.row = ft.Row(
            controls=[
                ft.Text(self.name),
                ft.Text(self.color),
                ft.IconButton(ft.icons.DELETE, on_click=self.remove_cat),
            ]
        )

        self.controls = [self.row]

    def remove_cat(self, e):
        self.cat_delete(self)


def alter_event(page: ft.Page, toUpdate: int):
    from project_todo.common.routing import views_handler

    update: Event
    update = Event.find_by_id(toUpdate)

    page.title = "Alter Event"
    page.horizontal_alignment = ft.CrossAxisAlignment.START
    page.update()

    def submit():
        if not eventName.value or not eventDescription.value or not eventPriority[0].value:
            page.dialog = dlg_modal
            dlg_modal.open = True
            page.update()
            return

        Event.update(
            update.id,
            {
                "eventName": eventName.value,
                "eventDescription": eventDescription.value,
                "eventPriority": eventPriority[0].value,
            },
        )

        # event categories
        for cat in update.categories:
            EventCategory.delete_by_event_id(update.id)

        for cat in cats.controls:
            print(cat.id)
            EventCategory(cat.id, update.id)

        views_handler(page)["/"](page)

    def cat_Delete(cat):
        cats.controls.remove(cat)
        page.update()

    def add_cat(e):
        print(catsDropdown[0].value)
        teste = CategoriesRow(catsDropdown[0].value, cat_Delete)
        cats.controls.append(teste)
        page.update()

    async def close_dlg(e):
        dlg_modal.open = False
        await e.control.page.update_async()

    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Error"),
        content=ft.Text("Please fill in all fields."),
        actions=[
            ft.TextButton("ok", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    eventName = ft.TextField(label="Event Name", value=update.eventName)
    eventDescription = ft.TextField(label="Event Description", value=update.event_description)
    eventPriority = (
        ft.Dropdown(
            width=200,
            options=[
                ft.dropdown.Option("Low"),
                ft.dropdown.Option("Medium"),
                ft.dropdown.Option("High"),
            ],
            label="Priority",
            value=update.eventPriority,
        ),
    )

    # category control

    cats = ft.Column()

    catsDropdown = (
        ft.Dropdown(
            width=500,
            options=[],
            label="Categories",
            value="",
            on_change=add_cat,
        ),
    )

    for cat in Category.all():
        catsDropdown[0].options.append(ft.dropdown.Option(cat.id, text=cat.categoryName))

    for cat in update.categories:
        print(cat)
        cats.controls.append(CategoriesRow(cat.id, cat_Delete))

    actions = [
        ft.TextButton("Save", on_click=lambda e: submit()),
        ft.TextButton("Cancel", on_click=lambda e: views_handler(page)["/"](page)),
    ]

    page.add(
        eventName,
        eventDescription,
        ft.Column(eventPriority),
        catsDropdown[0],
        cats,
        ft.Row(actions),
    )
    page.update()
