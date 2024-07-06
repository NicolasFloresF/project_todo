# importing modules from the project
from project_todo.entities.category import Category

# importing third-party modules
import flet as ft


def add_category(page: ft.Page):
    page.title = "Add Category"
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
        print(f"{categoryColor.value} {categoryName.value}")
        # Category(categoryName.value, categoryColor.value)
        print("Category added")

    categoryName = ft.TextField(label="Category Name")
    categoryColor = ft.TextField(
        label="Category Color",
        input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9A-F]"),
        max_length=6,
        prefix="#",
        prefix_text="#",
    )
    actions = [
        ft.TextButton("Save", on_click=lambda e: submit()),
        ft.TextButton("Cancel", on_click=lambda e: page.update()),
    ]

    page.add(categoryName, categoryColor, ft.Row(actions))
    page.update()
