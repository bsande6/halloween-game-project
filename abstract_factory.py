import abc

from zombie import LargeZombie, RunningZombie, RandomZombie

# i thnik we should jusst make this a factory pattern instead of abstract factory, not really sure how much that changes  

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
    def create_zombie(self, zombie_type, canvas, hero):
        if zombie_type == "large":
            return LargeZombie(canvas)
        elif zombie_type == "random":
            return RandomZombie(canvas)
        elif zombie_type == "running":
            return RunningZombie(canvas, hero)

