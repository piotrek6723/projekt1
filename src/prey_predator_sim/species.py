"""Module with definitions of considered species"""
import random

class Creature:

    alive: bool = True

    def __init__(self, p_death: float, p_reproduce: float):
        self.p_death = p_death
        self.p_reproduce = p_reproduce

    def kill(self):
        """Kills (i.e. alive=False) the creature with probability p_death"""
        if random.random() < self.p_death:
            self.alive = False

    def reproduce(self):
        """Returns new instance of Creature with probability p_reproduce (otherwise None)"""

        if self.alive and (random.random() < self.p_reproduce):

            # 1. Consider changing p_death, p_reproduce to have instances different from the parent
            return self.__class__(p_death=self.p_death, p_reproduce=self.p_reproduce)

        return None

    # TODO: Implement it as descriptors
    @property
    def p_death(self):

        return self.__p_death

    @p_death.setter
    def p_death(self, value):

        # Makes sure that 0 <= value <= 1
        value = min(1.0, max(0.0, value))

        self.__p_death = value

    @property
    def p_reproduce(self):

        return self.__p_reproduce

    @p_reproduce.setter
    def p_reproduce(self, value):

        # Makes sure that 0 <= value <= 1
        value = min(1.0, max(0.0, value))

        self.__p_reproduce = value


class Prey(Creature):
    name = "Prey"

    def __init__(self, p_death: float, p_reproduce: float, p_hunt: float):
        super().__init__(p_death, p_reproduce)
        self.p_hunt = min(1.0, max(0.0, p_hunt))

    def reproduce(self):
        if self.alive and random.random() < self.p_reproduce:
            return Prey(self.p_death, self.p_reproduce, self.p_hunt)
        return None


class Predator(Creature):
    name = "Predator"
    p_death_hungry = 0.9

    def __init__(self, p_death: float, p_reproduce: float):
        super().__init__(p_death, p_reproduce)
        self.hungry = True

    def hunt(self, prey):
        if self.alive and self.hungry and prey.alive:
            if random.random() < prey.p_hunt:
                prey.alive = False
                self.hungry = False
                return True
        return False

    def kill(self):
        if self.hungry:
            if random.random() < self.p_death_hungry:
                self.alive = False
        else:
            super().kill()