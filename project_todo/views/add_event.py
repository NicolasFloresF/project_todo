# importing project modules
from project_todo.entities.event import Event
from project_todo.entities.occurrence import Occurrence
from project_todo.entities.event_category import EventCategory
from project_todo.entities.category import Category

# importing third-party modules
import datetime
import flet as ft


# class CategoryRow(ft.Column):
#    def __init__(self, category: Category, page: ft.Page):
#        super().__init__()
#
#        self.exp = ft.ExpansionTile(
#            title=ft.Checkbox(label=f"{category.categoryName}", value=category.CategoryStatus),
#            maintain_state=True,
#        )
#
#        self.consult = ft.Column(
#            controls=[
#                ft.ListTile(
#                    title=ft.Text(
#                        f"Description: {category.categoryDescription}",
#                    )
#                ),
#                ft.ListTile(title=ft.Text(f"Creation date: {category.CategoryCreationDate}")),
#                ft.ListTile(
#                    trailing=ft.Row(
#                        alignment=ft.MainAxisAlignment.END,
#                        controls=[
#                            ft.IconButton(ft.icons.CREATE, on_click=self.edit_clicked),
#                            ft.IconButton(ft.icons.DELETE),
#                        ],
#                    )
#                ),
#            ],
#        )
#
#        self.form = ft.Column(
#            visible=False,
#            controls=[
#                ft.TextField(label="Description", value=category.categoryDescription),
#                ft.Dropdown(
#                    width=200,
#                    options=[
#                        ft.dropdown.Option("Low"),
#                        ft.dropdown.Option("Medium"),
#                        ft.dropdown.Option("High"),
#                    ],
#                    label="Priority",
#                    value=category.categoryPriority,
#                ),
#                ft.Checkbox(label="Status", value=category.CategoryStatus),
#                ft.Row(
#                    controls=[
#                        ft.ElevatedButton(
#                            text="Save",
#                            on_click=lambda e: self.save_clicked(category, page),
#                        ),
#                        ft.ElevatedButton(
#                            text="Cancel",
#                            on_click=lambda e: self.cancel_clicked(category, page),
#                        ),
#                    ]
#                ),
#            ],
#        )
#
#        self.add(self.exp, self.consult, self.form)
#
#    def edit_clicked(self, e):
#        self.exp.visible = False
#        self.consult.visible = False
#        self.form.visible = True
#        e.control.page.update()
#
#    def save_clicked(self, category: Category, page: ft.Page):
#        category.categoryDescription = self.form.controls[0].value
#        category.categoryPriority = self.form.controls[1].value
#        category.CategoryStatus = self.form.controls[2].value
#        category.update()
#        self.exp.visible = True
#        self.consult.visible = True
#        self.form.visible = False
#        page.update()
#
#    def cancel_clicked(self, category: Category, page: ft.Page):
#        self.exp.visible = True
#        self.consult.visible = True
#        self.form.visible = False
#        page.update


# é muita meteção de louco passar uma função como parametro pro construtor de uma classe
# que será usado pra remover a classe que a chamou,
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


def add_event(page: ft.Page):
    page.title = "Add Event"
    page.update()

    def submit():
        if not eventName.value or not eventDate or not eventDescription.value or not eventPriority[0].value:
            page.dialog = dlg_modal
            dlg_modal.open = True
            page.update()
            return

        print(
            f"{eventName.value} {eventDate} {eventDescription.value} {eventPriority[0].value} {eventHasDeadline.value}"
        )
        Ev = Event(
            eventName.value,
            eventDate,
            eventDescription.value,
            eventPriority[0].value,
            eventHasDeadline.value,
            False,
        )
        print(f"Event added, {Ev.id}")

        # add event occurrences
        if eventHasDeadline.value == True:
            if not deadlinePicker.value:
                page.dialog = dlg_modal
                dlg_modal.open = True
                page.update()
                return

            print(deadlinePicker.value)
            Occurrence(deadlinePicker.value, datetime.datetime.now().strftime("%H:%M:%S"), Ev.id, False)

            if repeat.value and radioRepeat.value:
                print(radioRepeat.value)
                currDate = deadlinePicker.value
                for _ in range(3):
                    if radioRepeat.value == "daily":
                        currDate = currDate + datetime.timedelta(days=1)
                    elif radioRepeat.value == "weekly":
                        currDate = currDate + datetime.timedelta(weeks=1)
                    elif radioRepeat.value == "monthly":
                        currDate = currDate + datetime.timedelta(weeks=4)
                    elif radioRepeat.value == "annually":
                        currDate = currDate + datetime.timedelta(weeks=52)

                    Occurrence(currDate, datetime.datetime.now().strftime("%H:%M:%S"), Ev.id, False)

                    print(currDate)

        # event categories
        for cat in cats.controls:
            print(cat.id)
            EventCategory(cat.id, Ev.id)

        page.update()

    def HasDeadline(e):
        print(eventHasDeadline.value)
        if eventHasDeadline.value == True:
            deadlineDateCol.visible = True
        else:
            deadlineDateCol.visible = False
        page.update()

    def DeadlineChanged(e):
        deadlineButton[0].text = deadlinePicker.value.strftime("%d/%m/%Y")
        page.update()

    def Repeat(e):
        print(repeat.value)
        if repeat.value == True:
            radioRepeat.visible = True
        else:
            radioRepeat.visible = False
        page.update()

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

    eventName = ft.TextField(label="Event Name")
    eventDate = datetime.date.today()
    eventDescription = ft.TextField(label="Event Description")
    eventPriority = (
        ft.Dropdown(
            width=200,
            options=[
                ft.dropdown.Option("Low"),
                ft.dropdown.Option("Medium"),
                ft.dropdown.Option("High"),
            ],
            label="Priority",
            value="",
        ),
    )

    eventHasDeadline = ft.Checkbox(label="Deadline", on_change=HasDeadline)

    # if eventHasDeadline.value == True

    deadlinePicker = ft.DatePicker(
        value=datetime.date.today(),
        on_change=DeadlineChanged,
    )
    deadlineText = ft.Text("Deadline Date:")
    deadlineButton = (
        ft.ElevatedButton(
            text=datetime.date.today().strftime("%d/%m/%Y"),
            icon=ft.icons.CALENDAR_MONTH,
            on_click=lambda e: page.open(deadlinePicker),
        ),
    )

    # if the event repeat

    repeat = ft.Checkbox(label="Repeat", value=False, on_change=Repeat)

    radioRepeat = ft.RadioGroup(
        visible=False,
        content=ft.Column(
            [
                ft.Radio(value="daily", label="daily"),
                ft.Radio(value="weekly", label="weekly"),
                ft.Radio(value="monthly", label="monthly"),
                ft.Radio(value="annually", label="annually"),
            ]
        ),
    )

    deadlineDateCol = ft.Column(visible=False, controls=[deadlineText, ft.Column(deadlineButton), repeat, radioRepeat])

    # category control

    # TODO: implement this when update is necessary
    # for cat in ev.categories:
    #    page.add(CategoriesRow(category, page))

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

    actions = [
        ft.TextButton("Save", on_click=lambda e: submit()),
        ft.TextButton("Cancel", on_click=lambda e: page.update()),
    ]

    page.add(
        eventName,
        eventDescription,
        ft.Column(eventPriority),
        eventHasDeadline,
        deadlineDateCol,
        catsDropdown[0],
        cats,
        ft.Row(actions),
    )
    page.update()
