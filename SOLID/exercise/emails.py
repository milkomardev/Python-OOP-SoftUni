from abc import ABC, abstractmethod


class IEmail(ABC):

    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


class IContent(ABC):

    def __init__(self, content):
        self.content = content

    @abstractmethod
    def format(self):
        ...


class MyContent(IContent):

    def format(self):
        return ''.join(['<myML>', self.content, '</myML>'])


class IProtocol(ABC):

    def __init__(self, text):
        self.text = text

    @abstractmethod
    def format(self):
        ...


class MyProtocol(IProtocol):

    def format(self):
        return ''.join(["I'm ", self.text])


class NameProtocol(IProtocol):

    def format(self):
        return ''.join(["My name is ", self.text])


class Email(IEmail):

    def __init__(self, protocol):
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender):
        self.__sender = sender.format()

    def set_receiver(self, receiver):
        self.__receiver = receiver.format()

    def set_content(self, content):
        self.__content = content.format()

    def __repr__(self):
        return f"Sender: {self.__sender}\nReceiver: {self.__receiver}\nContent:\n{self.__content}"


email = Email('IM')

sender = MyProtocol('gmal')
email.set_sender(sender)

# receiver = NameProtocol('james')
receiver = MyProtocol('james')
email.set_receiver(receiver)

content = MyContent('Hello, there!')
email.set_content(content)

print(email)