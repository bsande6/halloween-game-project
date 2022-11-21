import abc

from zombie import BasicZombie, RunningZombie

class AbstractFactory(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def create_zombie(self):
        pass

class BasicZombieFactory(AbstractFactory):
    def create_zombie(self):
        return BasicZombie()


class RunningZombieFactory(AbstractFactory):
    def create_zombie(self):
        return RunningZombie()

class RandomZombieFactory(AbstractFactory):
    def create_zombie(self):
        return RandomZombie()
