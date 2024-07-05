# importing modules from the project
from project_todo.entities.event import Event
from project_todo.entities.occurrence import Occurrence

# importing third-party modules
import datetime
import flet as ft


# TODO: Confirmar exclusão
# TODO: Dar nome aos inputs e submeter para dar update no banco
# TODO: CRUD categorias
# TODO: adcionar eventos
class TasksRow(ft.Column):
    def __init__(self, event: Event, ocurrence: Occurrence, page: ft.Page):
        super().__init__()

        if ocurrence:
            status = ocurrence.OccurrenceStatus
        else:
            status = event.EventStatus

        self.exp = ft.ExpansionTile(
            title=ft.Checkbox(label=f"{event.eventName}", value=status),
            maintain_state=True,
        )

        self.consult = ft.Column(
            controls=[
                ft.ListTile(
                    title=ft.Text(
                        f"Description: {event.event_description}",
                    )
                ),
                ft.ListTile(title=ft.Text(f"Creation date: {event.eventDate}")),
                ft.ListTile(title=ft.Text(f"Priority: {event.eventPriority}")),
                ft.ListTile(title=ft.Text(f"Deadline Date: {ocurrence.OccurrenceDeadlineDate if ocurrence else 'No'}")),
                ft.ListTile(title=ft.Text(f"Deadline Time: {ocurrence.OccurrenceDeadlineTime if ocurrence else 'No'}")),
                ft.ListTile(title=ft.Text(f"Deadline: {event.EventHasDeadline}")),
                ft.ListTile(
                    trailing=ft.Row(
                        alignment=ft.MainAxisAlignment.END,
                        controls=[
                            ft.IconButton(ft.icons.CREATE, on_click=self.edit_clicked),
                            ft.IconButton(ft.icons.DELETE),
                        ],
                    )
                ),
            ],
        )

        self.form = ft.Column(
            visible=False,
            controls=[
                ft.TextField(label="Description", value=event.event_description),
                ft.Dropdown(
                    width=200,
                    options=[
                        ft.dropdown.Option("Low"),
                        ft.dropdown.Option("Medium"),
                        ft.dropdown.Option("High"),
                    ],
                    label="Priority",
                    value=event.eventPriority,
                ),
                ft.ElevatedButton(
                    "Deadline Date",
                    icon=ft.icons.CALENDAR_MONTH,
                    on_click=lambda e: page.open(
                        ft.DatePicker(
                            first_date=datetime.datetime(year=2023, month=10, day=1),
                            last_date=datetime.datetime(year=2024, month=10, day=1),
                        )
                    ),
                ),
                ft.ElevatedButton(
                    "Deadline Time",
                    icon=ft.icons.CALENDAR_MONTH,
                    on_click=lambda e: page.open(
                        ft.TimePicker(
                            confirm_text="Confirm",
                            error_invalid_text="Time out of range",
                            help_text="Pick your time slot",
                        ),
                    ),
                ),
                ft.Checkbox(label="Deadline", value=event.EventHasDeadline),
                ft.ListTile(
                    trailing=ft.Row(
                        alignment=ft.MainAxisAlignment.END,
                        controls=[
                            ft.TextButton("Save"),
                            ft.TextButton("Cancel", on_click=self.edit_cancel),
                        ],
                    ),
                ),
            ],
        )

        self.exp.controls.append(self.consult)
        self.exp.controls.append(self.form)
        self.controls = [self.exp]

    def edit_clicked(self, e):
        self.consult.visible = False
        self.form.visible = True
        self.update()

    def edit_cancel(self, e):
        self.consult.visible = True
        self.form.visible = False
        self.update()


def main_menu(page: ft.Page):

    def tabs_changed(e):
        print(filter.selected_index)

        tasks.controls.clear()
        if filter.selected_index == 0:
            tasks_append(0)
        elif filter.selected_index == 1:
            tasks_append(1)

        page.update()

    page.title = "To-Do App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    new_task = ft.TextField(hint_text="What's needs to be done?")
    page.add(new_task, ft.FloatingActionButton(icon=ft.icons.ADD))

    filter = ft.Tabs(
        selected_index=0,
        on_change=tabs_changed,
        tabs=[
            ft.Tab(text="Events with deadline"),
            ft.Tab(text="Events without deadline"),
        ],
    )

    page.add(filter)

    tasks = ft.Column()
    page.add(tasks)

    def tasks_append(index):
        if index == 0:
            for ocurrence in Occurrence.all():
                ocurrence: Occurrence
                event: Event

                event = Event.find_by_id(ocurrence.Event_idEvent)

                task = TasksRow(event, ocurrence, page)

                tasks.controls.append(task)

                page.update()

        elif index == 1:
            for event in Event.all():
                if event.EventHasDeadline:
                    continue

                event: Event

                task = TasksRow(event, None, page)

                tasks.controls.append(task)
                page.update()

    tasks_append(0)
