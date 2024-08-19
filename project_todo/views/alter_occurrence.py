""" This module contains the view for altering an occurrence."""

# importing project modules
from project_todo.entities.event import Event
from project_todo.entities.occurrence import Occurrence
from project_todo.entities.event_category import EventCategory
from project_todo.entities.category import Category

# importing third-party modules
import datetime
import flet as ft


def alter_occurrence(page: ft.Page, toUpdate: int):
    """This function creates the view for altering an occurrence.

    Args:
        page (ft.Page): The page to be updated.
        toUpdate (int): The id of the occurrence to be altered.
    """
    from project_todo.common.routing import views_handler

    update: Occurrence
    update = Occurrence.find_by_id(toUpdate)

    event: Event
    event = Event.find_by_id(update.Event_idEvent)

    page.title = "Alter occurrence"
    page.horizontal_alignment = ft.CrossAxisAlignment.START
    page.update()

    def submit():
        if not deadlinePicker.value:
            page.dialog = dlg_modal
            dlg_modal.open = True
            page.update()
            return

        Occurrence.update(
            update.id,
            {
                "OccurrenceDeadlineDate": deadlinePicker.value,
            },
        )
        views_handler(page)["/"](page)

    def DeadlineChanged(e):
        deadlineButton[0].text = deadlinePicker.value.strftime("%d/%m/%Y")
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

    evntName = ft.Text(f"Event Name: {event.eventName}", theme_style=ft.TextThemeStyle.BODY_LARGE)
    evntDescription = ft.Text(f"Event Description: {event.eventName}", theme_style=ft.TextThemeStyle.BODY_LARGE)
    evntCreation = ft.Text(
        f"Event creation date: {event.eventDate.strftime('%d/%m/%Y')}", theme_style=ft.TextThemeStyle.BODY_LARGE
    )
    evntPriority = ft.Text(f"Priority: {event.eventPriority}", theme_style=ft.TextThemeStyle.BODY_LARGE)

    deadlinePicker = ft.DatePicker(
        value=update.OccurrenceDeadlineDate,
        on_change=DeadlineChanged,
    )
    deadlineText = ft.Text("Deadline Date:", theme_style=ft.TextThemeStyle.BODY_LARGE)
    deadlineButton = (
        ft.ElevatedButton(
            text=update.OccurrenceDeadlineDate.strftime("%d/%m/%Y"),
            icon=ft.icons.CALENDAR_MONTH,
            on_click=lambda e: page.open(deadlinePicker),
        ),
    )

    deadlineDateCol = ft.Column(controls=[deadlineText, ft.Column(deadlineButton)])

    actions = [
        ft.TextButton("Save", on_click=lambda e: submit()),
        ft.TextButton("Cancel", on_click=lambda e: views_handler(page)["/"](page)),
    ]

    page.add(
        evntName,
        evntDescription,
        evntCreation,
        evntPriority,
        deadlineDateCol,
        ft.Row(actions),
    )
    page.update()
