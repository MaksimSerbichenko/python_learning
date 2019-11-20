class Singlton:
    _insteance = None

    def __new__(cls):
        if cls._insteance is None:
            cls._insteance = object.__new__(cls)

        return cls._insteance

    def __init__(self):
        self.value = "some value"