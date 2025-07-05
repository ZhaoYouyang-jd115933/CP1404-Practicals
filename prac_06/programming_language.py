class ProgrammingLanguage:
    def __init__(self, name="", typing="", reflection="", year=0):
        """Initialise ProgrammingLanguage instance"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determine if typing is Dynamic or not"""
        if self.typing == "Dynamic":
            return True
        else:
            return False
