import flet as ft

class TaskApp(ft.UserControl):
    def build(self):
        self.textField = ft.TextField(width=350)
        self.addButton = ft.FloatingActionButton(icon=ft.icons.ADD, on_click=self.AddClick)
        
        self.tasks = ft.Column()
        taskRow = ft.Column(controls=[ft.Row(alignment=ft.MainAxisAlignment.SPACE_EVENLY ,controls=[self.textField, self.addButton]), self.tasks])
        return taskRow
    
    def AddClick(self, UserControle):
        TheTask = Task(self.textField.value, self.Delete)
        self.tasks.controls.append(TheTask)
        self.textField.value = ""
        self.update()

    def Delete(self, TheTask):
        self.tasks.controls.remove(TheTask)
        self.update()


class Task(ft.UserControl):
    def __init__(self, TaskText, TaskDelete):
        super().__init__()
        self.taskName = TaskText
        self.taskDelete = TaskDelete

    def build(self):
        self.displayTask = ft.Checkbox(label=self.taskName, value=False)
        self.editName = ft.TextField()

        self.displayView = ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN ,controls=[self.displayTask, ft.Row(controls=[ft.IconButton(ft.icons.CREATE_OUTLINED, on_click=self.EditClick), ft.IconButton(ft.icons.DELETE_OUTLINED, on_click=self.DeleteClick)])])

        self.editView = ft.Row(alignment=ft.MainAxisAlignment.SPACE_AROUND ,visible=False, controls=[self.editName, ft.IconButton(ft.icons.DONE_OUTLINED, on_click=self.SaveClick)])

        return ft.Column(controls=[self.displayView, self.editView])

    def EditClick(self, UserControle):
        self.displayView.visible = False
        self.editView.visible = True
        self.editName.value = self.displayTask.label
        self.update()

    def SaveClick(self, UserControle):
        self.displayView.visible = True
        self.editView.visible = False
        self.displayTask.label = self.editName.value
        self.update()

    def DeleteClick(self, UserControle):
        self.taskDelete(self)
        self.update()


def main(page: ft.page):
    page.title = "Todo App"
    page.window_width = 500
    page.window_height = 680
    page.bgcolor = "#3A98B9"

    TaskingApp = TaskApp()
    page.add(TaskingApp)    

ft.app(target=main)