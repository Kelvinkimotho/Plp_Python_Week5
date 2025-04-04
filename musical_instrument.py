class MusicalInstrument:
    """
    Represents a musical instrument.
    """
    def __init__(self, name, instrument_type, sound):
        # Initializing the attributes of the instrument
        self.name = name
        self.instrument_type = instrument_type
        self.sound = sound
    
    def play(self):
        # This smethpd prints the sound made by the instrument
        print(f"The {self.name} ({self.instrument_type}) makes a {self.sound} sound.")

class Guitar(MusicalInstrument):
    """
    Represents a Guitar, a type of string instrument.
    """
    def __init__(self, name, instrument_type, sound, strings):
        # Initializing the guitar with additional attribute for the number of strings
        super().__init__(name, instrument_type, sound)
        self.strings = strings
    
    def play(self):
        # Overriding play method to specify strumming the guitar with the number of strings
        print(f"Strumming the {self.name} with {self.strings} strings, producing a {self.sound} sound!")

#testing the program
# Creating a Guitar object and call the play method
guitar = Guitar("Acoustic Guitar", "String", "melodious", 6)
guitar.play()
