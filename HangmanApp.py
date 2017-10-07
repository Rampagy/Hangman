from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget


class HangmanGame(Widget):

    def check_in_word(self, btn):
        print(btn.text)
        btn.disabled = True # True is synonymous with 1

class HangmanApp(App):
    def build(self):
        return HangmanGame()


if __name__ == "__main__":
    HangmanApp().run()


