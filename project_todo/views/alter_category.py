"""This module contains the view for altering a category."""

# importing modules from the project
from project_todo.entities.category import Category

# importing third-party modules
import flet as ft


def alter_category(page: ft.Page, toUpdate: int):
    """This function creates the view for altering a category.

    Args:
        page (ft.Page): The page to be updated.
        toUpdate (int): The id of the category to be altered.
    """
    from project_todo.common.routing import views_handler

    update: Category
    update = Category.find_by_id(toUpdate)

    page.title = "Alter Category"
    page.horizontal_alignment = ft.CrossAxisAlignment.START
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

    def submit():
        if not categoryName.value or not categoryColor.value:
            page.dialog = dlg_modal
            dlg_modal.open = True
            page.update()
            return
        Category.update(update.id, {"categoryName": categoryName.value, "categoryColor": "#" + categoryColor.value})
        views_handler(page)["/"](page)

    categoryName = ft.TextField(label="Category Name", value=update.categoryName)
    categoryColor = ft.TextField(
        label="Category Color",
        input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9A-F]"),
        max_length=6,
        prefix="#",
        prefix_text="#",
        value=update.categoryColor[1:],
    )
    actions = [
        ft.TextButton("Save", on_click=lambda e: submit()),
        ft.TextButton("Cancel", on_click=lambda e: views_handler(page)["/"](page)),
    ]

    page.add(categoryName, categoryColor, ft.Row(actions))
    page.update()
