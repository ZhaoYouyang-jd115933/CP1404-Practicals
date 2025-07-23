from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicLabelsApp(App):
    """Dynamic Labels is a kivy app for show the names by name list"""
    def __init__(self, **kwargs):
        """Main program - Kivy app to demo dynamic label creation."""
        super().__init__(**kwargs)
        self.names = ["Bob", "Marry", "Alex", "David"]

    def build(self):
        """Build the Kivy app GUI."""
        self.title = "Name Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from data and add them to the GUI."""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)

DynamicLabelsApp().run()









