"""
Author: Han Su
Date: 10/05/2020
https://github.com/HanSu52/cp1404practicals
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty


class DynamicLabels(App):

    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Adrian", "Mary", "Alex", "Chloe", "Lucas"]

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        for name in self.names:
            label = Label(text=name, id=name)
            self.root.ids.entries_box.add_widget(label)


DynamicLabels().run()
