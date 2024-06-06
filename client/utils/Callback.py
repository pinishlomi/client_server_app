"""
Entry claim: gets callback_function
Exit claim: object for data structure - building the callback object.
"""

class Callback:

    """
    Entry claim: gets callback function
    Exit claim: resets type and data
    and activates the callback function in ClientApp.
    """
    def __init__(self, callback_func):
        self.type = None
        self.data = None
        self.function = callback_func   # holding the function to run in ClientApp when we have trigger in the screen

    def __str__(self):
        return f'type: {self.type}, data: {self.data}'