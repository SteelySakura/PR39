from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder

KV = '''
BoxLayout:
    orientation: 'vertical'

    MDRaisedButton:
        text: "Выберите время"
        on_release: app.show_time_picker()
'''


class TimePickerApp(MDApp):
    def build(self):
        self.dialog = None
        return Builder.load_string(KV)

    def show_time_picker(self):
        if not self.dialog:
            self.dialog = MDDialog(title="Выберите время")

        self.dialog.open()


if __name__ == '__main__':
    TimePickerApp().run()