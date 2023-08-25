class Hotelier(object): #서브시스템 1
    
    def __init__(self):
        print("Arranging the Hotel for  Marraige? --")
        
    def __isAvailable(self):
        print("Is the Hotel free for the event on given day?")
        return True
    
    def bookHotel(self):
        if self.__isAvailable():
            print("Registered the Booking\n\n")
            
class Florist(object): #서브시스템 2
    
    def __init__(self):
        print(" Flower Decorations for the Event? --")
        
    def setFlowerRequirements(self):
        print("Carnations, Roses and Lilies would be used for Deocrations\n\n")
        
class Caterer(object): #서브시스템 3
    
    def __init__(self):
        print("Food Arrangements for the Event? --")
        
    def setCuisine(self):
        print("Chinese & Continental Cusine to be served \n\n")
        
class Musician(object): #서브시스템 4
    
    def __init__(self):
        print("Musical Arrangements for the Marriage --")
        
    def setMusicType(self):
        print("Jazz and Classical will be played \n\n")
        
class EventManager(object): #퍼사드, 준비과정 간소화 전달
    
    def __init__(self):
        print("Event Manager:: Let me talk to the folks \n")
        
    def arrange(self): 
        self.hotelier = Hotelier() #서비시스템 객체 생성
        self.hotelier.bookHotel()
        
        self.florist = Florist()
        self.florist.setFlowerRequirements()
        
        self.caterer = Caterer()
        self.caterer.setCuisine()
        
        self.musician = Musician()
        self.musician.setMusicType()
        
class You(object): #클라이언트
    
    def __init__(self):
        print("You:: Whoa! Marriage Arrangements??!!")
        
    def askEventManager(self):
        print("You:: Let's Contact the Event Manager\n\n")
        em = EventManager() #퍼사드 인스턴스화
        em.arrange() #퍼사드에 특정 서비스 요청
        
    def __del__(self):
        print("You:: Thanks to Event Manager, all preparations done! Phew!")
        
you = You()
you.askEventManager()