from kivy.app import App
from kivy.lang import Builder


class DynamicLabelsApp(App):
    """Dynamic Labels is a kivy app for show the names by name list"""
    def __init__(self, **kwargs):
        """Main program - Kivy app to demo dynamic label creation."""
        super().__init__(**kwargs)
        self.name_list = ["Bob", "Marry", "Alex", "David"]

    def build(self):
        """Build the Kivy app GUI."""
        self.title = "Name Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root



