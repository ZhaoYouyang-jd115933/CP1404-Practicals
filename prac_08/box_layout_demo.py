from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """BoxLayoutDemo is a kivy app for get name and display greet message"""
    def build(self):
        """Build the Kivy GUI by loading the KV layout file."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root
    def handle_greet(self):
        """Handle the greet button press by displaying a greeting message."""
        print("test")
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        """Handler for pressing the clear button."""
        self.root.ids.input_name.text = ''
        self.root.ids.output_label.text = ''
BoxLayoutDemo().run()
