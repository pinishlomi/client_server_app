class Callback:
    def __init__(self, callback_func):
        self.type = None
        self.data = None
        self.function = callback_func

    def __str__(self):
        return f'type: {self.type}, data: {self.data}'