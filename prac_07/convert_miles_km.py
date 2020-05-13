"""
Author: Han Su
Date: 10/05/2020
https://github.com/HanSu52/cp1404practicals
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class ConvertMilesToKmApp(App):
    """ ConvertMilesToKmApp is a Kivy App for converting miles to kilometres """

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (500, 280)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, value):
        """ handle calculation (could be button press or other call), output result to label widget """
        result = float(value) * 1.609344
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        value = self.handle_invalid_inputs() + change
        self.root.ids.input_number.text = str(value)
        self.handle_calculate(value)

    def handle_invalid_inputs(self):
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0


ConvertMilesToKmApp().run()
