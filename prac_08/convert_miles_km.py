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

    def handle_calculate(self):
        """Calculate kilometers from the input miles and update the result label."""
        number = self.get_valid_miles()
        km_result = number * MILES_TO_KM
        self.root.ids.convert_result.text = str(km_result)

    def handle_increment(self, change):
        """Handler for pressing up or down button."""
        new_number = self.get_valid_miles() + change
        self.root.ids.input_number.text = str(new_number)
        self.handle_calculate()

    def get_valid_miles(self):
        """Validate miles input and convert it to float."""
        try:
            input_mile = float(self.root.ids.input_number.text)
            return input_mile
        except ValueError:
            return 0

ConvertMilesApp().run()

