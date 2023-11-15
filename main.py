from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import math

class CalculatorApp(App):
    def build(self):
        self.equation = ""

        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.text_input = TextInput(halign="right", multiline=False, readonly=False, font_size=55, input_filter="float")
        layout.add_widget(self.text_input)

        buttons = [
            ["sqr", "sqrt", "cos", "sin"],
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "^", "+"],
            ["C", "="]
        ]

        for row in buttons:
            button_row = BoxLayout()
            for label in row:
                button = Button(text=label, pos_hint={"center_x": 0.5, "center_y": 0.5}, font_size=32)
                button.bind(on_press=self.on_button_press)
                button_row.add_widget(button)
            layout.add_widget(button_row)

        return layout
    def on_button_press(self, instance):
        if instance.text == '=':
            try:
                self.equation = str(eval(self.equation))
            except Exception as e:
                self.equation = "Error"
        elif instance.text == 'sqrt':
            try:
                self.equation = str(math.sqrt(float(self.equation)))
            except Exception as e:
                self.equation = "Error"
        elif instance.text == 'sqr':
            try:
                self.equation = str(math.pow(float(self.equation.split('^')[0]), float(self.equation.split('^')[1])))
            except Exception as e:
                self.equation = "Error"
        elif instance.text == 'sin':
            try:
                self.equation = str(math.sin(float(self.equation)))
            except Exception as e:
                self.equation = "Error"
        elif instance.text == 'cos':
            try:
                self.equation = str(math.cos(float(self.equation)))
            except Exception as e:
                self.equation = "Error"
        elif instance.text == 'C':
            try:
                self.equation = ""
            except Exception as e:
                self.equation = ""
        else:
            self.equation += instance.text

        self.text_input.text = self.equation


if __name__ == '__main__':
    CalculatorApp().run()as
