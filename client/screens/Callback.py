class Callback:
    def __init__(self, callback):
        self.type = None
        self.data = None
        self.function = callback

    def __str__(self):
        return f'type: {self.type}, data: {self.data}'