# #Define timer variables
# #value = 60
# #active = True

# def reset():
#     value = 60

class Timer:
    def __init__(self, initial_value):
        self.initial_value = initial_value
        self.value = initial_value
        self.active = False

    def start(self):
        self.active = True

    def stop(self):
        self.active = False

    def reset(self):
        self.value = self.initial_value
        self.active = False