import abc

from zombie import BasicZombie, RunningZombie

class AbstractFactory(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def create_zombie(self):
        pass

# class BasicZombieFactory(AbstractFactory):
#     def create_zombie(self):
#         return BasicZombie()


# class RunningZombieFactory(AbstractFactory):
#     def create_zombie(self):
#         return RunningZombie()

# class RandomZombieFactory(AbstractFactory):
#     def create_zombie(self):
#         return RandomZombie()


# I think one factory is probably easier
# I dont think we actually even need the abstract factory
class ZombieFactory(AbstractFactory):
    def create_zombie(self, zombie_type):
        if zombie_type == "basic":
            return BasicZombie()
        elif zombie_type == "random":
            return RandomZombie()
        elif zombie_type == "running":
            return RunningZombie()

