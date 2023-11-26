from googletrans import Translator
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import pyttsx3

translator = Translator()
engine = pyttsx3.init()
class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)

        self.cols = 1

        self.inside_grid = GridLayout()
        self.inside_grid.cols = 2

        self.input = TextInput(multiline=False, hint_text="Text you want to translate" )
        self.add_widget(self.input)
        
        self.button = Button(text ="Translate", font_size=40)
        self.button.bind(on_press=self.translate)
        self.inside_grid.add_widget(self.button)

        self.add_widget(self.inside_grid)
        self.output = Button(text='', font_size=40)
        self.add_widget(self.output)


    def translate(self, instance):
        input_text = self.input.text
        translation = translator.translate(input_text, dest='en').text
        self.output.text = translation


class MyApp(App):

    def build(self):
        return MyGrid()


MyApp().run()