class MyObject:
    def __init__(self):
        self.password = None

    def __getattribute__(self, item):
        if item == "secret_field" and self.password == "9qq21(":
            return "Secret value"
        else:
            return object.__getattribute__(self, item)
