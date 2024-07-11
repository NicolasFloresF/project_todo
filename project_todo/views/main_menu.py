# importing modules from the project
from project_todo.entities.event import Event
from project_todo.entities.occurrence import Occurrence
from project_todo.entities.event_category import EventCategory
from project_todo.entities.category import Category

# importing third-party modules
import datetime
import flet as ft


class CategoriesRow(ft.Column):
    def __init__(self, id: int, catDelete, catUpdate):
        super().__init__()

        category = Category.find_by_id(id)
        self.id = id
        self.name = ft.Text(
            category.categoryName, style=ft.TextStyle(color=category.categoryColor)
        )
        self.color = category.categoryColor
        self.cat_delete = catDelete
        self.cat_update = catUpdate

        self.row = ft.Column(
            controls=[
                ft.Container(
                    content=ft.Row(
                        controls=[
                            self.name,
                            ft.Text(self.color),
                        ],
                        alignment=ft.MainAxisAlignment.START,
                    ),
                ),
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.IconButton(ft.icons.CREATE, on_click=self.update_cat),
                            ft.IconButton(ft.icons.DELETE, on_click=self.remove_cat),
                        ],
                        alignment=ft.MainAxisAlignment.END,
                    ),
                ),
            ]
        )

        self.controls = [self.row]

    def remove_cat(self, e):
        self.cat_delete(self)

    def update_cat(self, e):
        self.cat_update(self)


class TasksRow(ft.Column):
    def __init__(
        self, eventId: int, ocurrenceId: int, evntDelete, evntUpdate, checkEvent
    ):
        super().__init__()
        occurrence: Occurrence
        event: Event

        occurrence = Occurrence.find_by_id(ocurrenceId)
        event = Event.find_by_id(eventId)

        self.event_check = checkEvent
        self.event_delete = evntDelete
        self.event_update = evntUpdate

        if occurrence:
            self.id = occurrence.id
            status = occurrence.OccurrenceStatus
        else:
            self.id = event.id
            status = event.EventStatus

        self.hasDeadline = event.EventHasDeadline
        self.exp = ft.ExpansionTile(
            title="",
            maintain_state=True,
        )

        self.Title = ft.Checkbox(
            label=f"{event.eventName}", value=status, on_change=self.check_event
        )

        self.subTitle = ft.Text()
        for cat in event.categories:
            txt = ft.TextSpan(
                text=cat.categoryName, style=ft.TextStyle(color=cat.categoryColor)
            )
            self.subTitle.spans.append(txt)
            if cat != event.categories[-1]:
                self.subTitle.spans.append(ft.TextSpan(text=", "))

        self.consult = ft.Column()
        self.ltDesc = (
            ft.ListTile(
                title=ft.Text(
                    f"Description: {event.event_description}",
                )
            ),
        )

        self.ltDate = (
            ft.ListTile(
                title=ft.Text(f"Creation date: {event.eventDate.strftime('%d/%m/%Y')}")
            ),
        )
        self.ltPriority = (
            ft.ListTile(title=ft.Text(f"Priority: {event.eventPriority}")),
        )
        self.ltDeadlineDate = (
            ft.ListTile(
                title=ft.Text(
                    f"Deadline Date: {occurrence.OccurrenceDeadlineDate.strftime('%d/%m/%Y') if occurrence else ''}"
                )
            ),
        )
        self.ltButtons = (
            ft.ListTile(
                trailing=ft.Row(
                    alignment=ft.MainAxisAlignment.END,
                    controls=[
                        ft.IconButton(ft.icons.CREATE, on_click=self.update_event),
                        ft.IconButton(ft.icons.DELETE, on_click=self.remove_event),
                    ],
                )
            ),
        )

        self.exp.title = self.Title
        self.exp.subtitle = self.subTitle
        self.consult.controls.append(self.ltDesc[0])
        self.consult.controls.append(self.ltDate[0])
        self.consult.controls.append(self.ltPriority[0])

        if occurrence:
            self.consult.controls.append(self.ltDeadlineDate[0])

        self.consult.controls.append(self.ltButtons[0])

        self.exp.controls.append(self.consult)
        self.controls = [self.exp]

    def remove_event(self, e):
        self.event_delete(self)

    def update_event(self, e):
        self.event_update(self)

    def check_event(self, e):
        self.event_check(self)


confirmation: bool = False


def main_menu(page: ft.Page):
    from project_todo.common.routing import views_handler

    page.scroll = ft.ScrollMode.ALWAYS
    page.title = "To-Do App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    def tabs_changed(e):
        print(filter.selected_index)

        events.controls.clear()
        occurences.controls.clear()
        if filter.selected_index == 0:
            tab_selector(0)
        elif filter.selected_index == 1:
            tab_selector(1)
        elif filter.selected_index == 2:
            tab_selector(2)

        page.update()

    filter = ft.Tabs(
        selected_index=0,
        on_change=tabs_changed,
        tabs=[
            ft.Tab(text="Events"),
            ft.Tab(text="Occurences"),
            ft.Tab(text="Categories"),
        ],
    )

    page.add(filter)

    events = ft.Column()
    occurences = ft.Column()

    evntTasks = ft.Text("Events", visible=False, style=ft.TextThemeStyle.BODY_LARGE)
    page.add(evntTasks)
    page.add(events)

    occTasks = ft.Text(
        "Occurrence Events", visible=False, style=ft.TextThemeStyle.BODY_LARGE
    )

    appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.DONE_OUTLINE_ROUNDED),
        leading_width=40,
        title=ft.Text("Just TODOit"),
        center_title=True,
        bgcolor=ft.colors.BLUE_600,
        shape=ft.NotchShape.CIRCULAR,
        actions=[
            ft.IconButton(ft.icons.MENU_ROUNDED),
        ],
    )
    page.add(appbar)

    page.add(occTasks)
    page.add(occurences)

    def close_dlg(e):
        global confirmation
        dlg_modal_event.open = False
        dlg_modal_occurrence.open = False
        dlg_modal_category.open = False
        if e.control.text == "Yes":
            confirmation = True
        else:
            confirmation = False
        page.update()
        # await e.control.page.update_async()

    dlg_modal_event = ft.AlertDialog(
        modal=True,
        title=ft.Text("Delete Confirmation"),
        content=ft.Text(
            "Are you sure you want to delete this event? (this will delete all occurrences of this event)"
        ),
        actions=[
            ft.TextButton("Yes", on_click=close_dlg),
            ft.TextButton("No", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    dlg_modal_occurrence = ft.AlertDialog(
        modal=True,
        title=ft.Text("Delete Confirmation"),
        content=ft.Text("Are you sure you want to delete this occurrence?"),
        actions=[
            ft.TextButton("Yes", on_click=close_dlg),
            ft.TextButton("No", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    dlg_modal_category = ft.AlertDialog(
        modal=True,
        title=ft.Text("Delete Confirmation"),
        content=ft.Text(
            "Are you sure you want to delete this category? (this will delete all events that have this category)"
        ),
        actions=[
            ft.TextButton("Yes", on_click=close_dlg),
            ft.TextButton("No", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    def event_update(event):
        views_handler(page)["/alter_event"](page, event.id)
        page.update()

    def occurrence_update(occurrence):
        views_handler(page)["/alter_occurrence"](page, occurrence.id)
        page.update

    def event_delete(event: TasksRow):
        global confirmation
        dlg_modal_event.open = True
        page.dialog = dlg_modal_event
        page.update()

        while dlg_modal_event.open:
            pass

        if confirmation:
            toDelete: Event = Event.find_by_id(event.id)
            print(toDelete.EventHasDeadline)

            EventCategory.delete_by_event_id(toDelete.id)

            if toDelete.EventHasDeadline:
                Occurrence.delete_by_event_id(toDelete.id)
                occurences.controls.remove(event)
            else:
                events.controls.remove(event)

            Event.delete(toDelete.id)

        confirmation = False
        page.update()

    def occurrence_delete(occurrence: TasksRow):
        global confirmation
        dlg_modal_occurrence.open = True
        page.dialog = dlg_modal_occurrence
        page.update()

        while dlg_modal_occurrence.open:
            pass

        if confirmation:
            print(occurrence.hasDeadline)
            events.controls.remove(occurrence)
            Occurrence.delete(occurrence.id)

        confirmation = False
        page.update()

    def event_check(event: TasksRow):
        Event.update(event.id, {"EventStatus": event.Title.value})
        page.update()

    def occurrence_check(occurrence: TasksRow):
        Occurrence.update(occurrence.id, {"OccurrenceStatus": occurrence.Title.value})
        page.update()

    def cat_delete(cat):
        global confirmation
        dlg_modal_category.open = True
        page.dialog = dlg_modal_category
        page.update()

        while dlg_modal_category.open:
            pass

        if confirmation:
            EventCategory.delete_by_category_id(cat.id)
            Category.delete(cat.id)

        events.controls.remove(cat)
        page.update()

    def cat_update(cat):
        views_handler(page)["/alter_category"](page, cat.id)
        page.update()

    def tab_selector(index):
        # events
        if index == 0:
            evntTasks.visible = True
            occTasks.visible = True
            page.add(
                ft.Container(
                    ft.FloatingActionButton(
                        bgcolor=ft.colors.BLUE_600,
                        icon=ft.icons.ADD,
                        on_click=lambda e: views_handler(page)["/add_event"](page),
                        shape=ft.RoundedRectangleBorder(radius=40),
                    ),
                    alignment=ft.alignment.center,
                )
                # ft.FloatingActionButtonLocation.CENTER_DOCKED,
                # ft.FloatingActionButton(
                #    icon=ft.icons.ADD,
                #    on_click=lambda e: views_handler(page)["/add_event"](page),
                # )
            )

            for event in Event.all():
                event: Event

                task = TasksRow(event.id, None, event_delete, event_update, event_check)

                if event.EventHasDeadline:
                    occurences.controls.append(task)
                else:
                    events.controls.append(task)
                page.update()
        # occurences
        elif index == 1:
            evntTasks.visible = False
            occTasks.visible = False
            page.add(
                ft.FloatingActionButton(
                    icon=ft.icons.ADD,
                    on_click=lambda e: views_handler(page)["/add_event"](page),
                )
            )
            for ocurrence in Occurrence.all():
                ocurrence: Occurrence
                event: Event

                event = Event.find_by_id(ocurrence.Event_idEvent)

                task = TasksRow(
                    event.id,
                    ocurrence.id,
                    occurrence_delete,
                    occurrence_update,
                    occurrence_check,
                )

                events.controls.append(task)

                page.update()
        # categories
        elif index == 2:
            evntTasks.visible = False
            occTasks.visible = False

            page.add(
                ft.FloatingActionButton(
                    icon=ft.icons.ADD,
                    on_click=lambda e: views_handler(page)["/add_category"](page),
                    bgcolor=ft.colors.ORANGE_700,
                )
            )
            for category in Category.all():
                category: Category

                cat = CategoriesRow(category.id, cat_delete, cat_update)
                events.controls.append(cat)
                page.update()

    tab_selector(0)
