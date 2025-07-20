from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import StringProperty
MILES_TO_KM = 1.60934

class ConvertMilesApp(App):
    """Kivy app for converting miles to kilometers."""
    convert_result = StringProperty()
    def build(self):
        """Build the kivy app GUI and initialize default values."""
        Window.size = (400, 250)
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file("convert_miles_km.kv")
        self.convert_result = "0.0"
        return self.root

ConvertMilesApp().run()

