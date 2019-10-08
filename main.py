from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.logger import Logger


class GameWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.hello_message = Label(text='Olá, bedescoso!', pos=(350, 500), font_size=40)
        self.add_widget(self.hello_message)
        self.exit_button = Button(text='Sair dessa demência', font_size=15, pos=(300, 70), size=(200, 100))
        self.columba = Button(text='Clique aqui para obter uma columba deliciosa...',
                              font_size=15, pos=(150, 250), size=(500, 100))
        self.add_widget(self.columba)
        self.exit_button.bind(on_press=self.exitfunc)
        self.add_widget(self.exit_button)


    def exitfunc(self, obj):
        App.get_running_app().stop()
        Window.close()


class DumbGame(App):
    def on_stop(self):
        Logger.critical('Adeus.')

    def build(self):
        return GameWidget()


if __name__ == '__main__':
    app = DumbGame()
    app.run()
