class Animai(object):
    def __init__(self):
        self.can_fly = False
        self.can_run = False

    def print_abilities(self):
        print(type(self).__name__ + ':')
        print('Can run: ', self.can_run)
        print('Can fly:', self.can_fly)
        print()


class Horse(Animai):
    def __init__(self):
        super().__init__()
        self.can_run = True


class Bird(Animai):
    def __init__(self):
        super().__init__()
        self.can_fly = True


class Pegasus(Horse, Bird):
    pass


if __name__ == '__main__':
    horse = Horse()
    horse.print_abilities()