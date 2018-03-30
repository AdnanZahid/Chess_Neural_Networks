from abc import abstractmethod


class InputHandlerDelegate:
    @abstractmethod
    def didTakeInput(self, move):
        pass

    @abstractmethod
    def setupNewGame(self):
        pass


class InputHandler:

    @abstractmethod
    def input(self):
        pass


class OutputHandler:

    @abstractmethod
    def setup(self):
        pass

    @abstractmethod
    def output(self):
        pass

    @abstractmethod
    def cancelMove(self):
        pass
