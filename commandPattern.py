#편집기 기능: 추갸, 삭제, 실행
from abc import abstractmethod, ABCMeta

class Command(metaclass=ABCMeta):   #Receiver 메서드를 실행함(각 메서드들은 Concrete Command Class로 분리됨(캡슐화됨)
    def __init__(self, receiver):
        self.receiver = receiver
    
    @abstractmethod
    def execute(self):
        pass
    
class Receiver:     #모든 기능들은 여기서 구현함
    def add(self):
        print("추가 기능")
        
    def delete(self):
        print("삭제 기능")
        
    def run(self):
        print("실행 기능")
        
class addCommand(Command):      #Receiver들의 독립된 메서드들을 캡슐화 함: Receiver class 생성 -> execute를 오더라이드해서 특정한 한 개의 메서드만 실행
    def __init__(self, receiver):
        self.receiver = receiver
        
    def execute(self):
        self.receiver.add()
        
class deleteCommand(Command):
    def __init__(self, receiver):
        self.receiver = receiver
        
    def execute(self):
        self.receiver.delete()
        
class runCommand(Command):
    def __init__(self, receiver):
        self.receiver = receiver
        
    def execute(self):
        self.receiver.run()
        
class Invoker:      #대행사 역할, 큐를 만듬 -> 받은 Concrete Command 객체 변수들을 큐에 추가하고 해당 객체 변수들의 메서드를 실행
    def __init__(self):
        self.__Queue = []
        
    def runEditor(self, command):
        self.__Queue.append(command)
        command.execute()
        
rsv = Receiver()
addCmd = addCommand(rsv)
deleteCmd = deleteCommand(rsv)
runCmd = runCommand(rsv)
invoker = Invoker()
invoker.runEditor(addCmd)
invoker.runEditor(deleteCmd)
invoker.runEditor(runCmd)