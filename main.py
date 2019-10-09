from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.logger import Logger
from kivy.graphics import Rectangle
from kivy.uix.screenmanager import ScreenManager, Screen


class InitialPage(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.hello_message = Label(text='Olá, bedescoso!', pos=(350, 500), font_size=40)
        self.add_widget(self.hello_message)
        self.exit_button = Button(text='Sair dessa demência', font_size=15, pos=(300, 70), size=(200, 100))
        self.columba = Button(text='Clique aqui para obter uma columba deliciosa...',
                              font_size=15, pos=(150, 250), size=(500, 100))
        self.columba.bind(on_press=self.columba_button)
        self.add_widget(self.columba)
        self.exit_button.bind(on_press=self.exitfunc)
        self.add_widget(self.exit_button)

    def exitfunc(self, obj):
        App.get_running_app().stop()
        Window.close()

    def columba_button(self, instance):
        app.game_page.__init__()
        app.screen_manager.current = 'Game'


class GamePage(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.worked = Label(text='Voe com w,a,s,d...', pos=(120, 500), font_size=20)
        self.add_widget(self.worked)
        self._keyboard = Window.request_keyboard(self._on_keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_key_down)

        with self.canvas:
            self.player = Rectangle(source='columba.png', pos=(0, 0), size=(100, 100))

    def _on_keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_key_down)
        self._keyboard = None

    def _on_key_down(self, keyboard, keycode, text, modifiers):
        currentx = self.player.pos[0]
        currenty = self.player.pos[1]

        if text == 'w':
            currenty += 10
        if text == 's':
            currenty += -10
        if text == 'd':
            currentx += 10
        if text == 'a':
            currentx += -10

        self.player.pos = (currentx, currenty)


class DumbGame(App):
    def on_stop(self):
        Logger.critical('Adeus.')

    def build(self):
        self.screen_manager = ScreenManager()

        self.initial_page = InitialPage()
        screen = Screen(name='Initial')
        screen.add_widget(self.initial_page)
        self.screen_manager.add_widget(screen)

        self.game_page = GamePage()
        screen = Screen(name='Game')
        screen.add_widget(self.game_page)
        self.screen_manager.add_widget(screen)

        return self.screen_manager


if __name__ == '__main__':
    app = DumbGame()
    app.run()
