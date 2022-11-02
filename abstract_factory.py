
class AbstractFactory:
    @abstractmethod
    def create_zombie(self):
        pass

class BasicZombieFactory(AbstractFactory):
    def create_zombie(self):
        return BasicZombie()


class RunningZombieFactory(AbstractFactory):
    def create_zombie(self):
        return RunningZombie()
