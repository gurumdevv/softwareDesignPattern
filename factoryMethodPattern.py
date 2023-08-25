#큰 틀: Concrete creator class -> 필요한 기능들을 선택하여 객체를 생성하고 리스트에 담음
#필요한 기능: Concrete Product -> 필요한 기능을 Product 인터페이스를 상속받아서 구현함
from abc import abstractmethod, ABCMeta

class Section(metaclass=ABCMeta): #Product Interface
    
    @abstractmethod
    def describe(self):
        pass

class PersonalSection(Section): #ConcreteProdcut

    def describe(self):
        print("Personal Section")
        
class AlbumSection(Section):
    
    def describe(self):
        print("Album Section")
        
class PatentSection(Section):
    
    def describe(self):
        print("Patent Scection")
        
class PublicationSection(Section):
    
    def describe(self):
        print("Publication Sectino")
        
class Profile(metaclass=ABCMeta): #Creator 추상 클래스, Profile 추상클래스에는 각 프로필의 섹션에 대한 정보가 없음 -> 서브크랠스가 결정함
    
    def __init__(self):
        self.sections = []
        self.createProfile() #객체를 생성하는 메서드(단 추상메서드로 서브 클래스에서 실제로 객체 생성을 함)
        
    @abstractmethod
    def createProfile(self):
        pass
    
    def getSections(self):
        return self.sections
    
    def addSections(self, section):
        self.sections.append(section)
        
class linkedin(Profile): #Concrete Creator class
    
    def createProfile(self): #Prodcut 클래스에서 어떤 클래스를 만들지 결정한 후 객체 생성
        self.addSections(PersonalSection()) 
        self.addSections(PatentSection())
        self.addSections(PublicationSection())
        
class facebook(Profile):
    
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(AlbumSection())
        
if __name__ == '__main__':
    profile_type = input("어떤 프로파일을 만들기를 원하시나요? <LinkedIn or FaceBook>")
    profile = eval(profile_type.lower())() #ConcreteCreator 클래스 객체 생성
    print("Creating Profile..", type(profile).__name__)
    print("Profile has sections--", profile.getSections())