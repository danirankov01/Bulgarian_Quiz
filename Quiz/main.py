from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.config import Config

Config.set('graphics', 'Resizable', '0')
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '700')


class HomePage(Screen):
    pass


class Question1(Screen):
    pass


class Question2(Screen):
    pass


class Question3(Screen):
    pass


class Question4(Screen):
    pass


class Question5(Screen):
    pass


class Question6(Screen):
    pass


class Question7(Screen):
    pass


class Question8(Screen):
    pass


class Question9(Screen):
    pass


class Question10(Screen):
    pass


class FinalPage(Screen):
    pass


class ScreenManagement(ScreenManager):
    pass


file = Builder.load_file('file.kv')


class QuizApp(App):
    def build(self):
        return file


QuizApp().run()
