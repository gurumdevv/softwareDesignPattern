class Wizard():
    
    def __init__(self, src, rootdir):
        self.choices = []
        print("self.choices:", self.choices)
        self.rootdir = rootdir
        self.src = src
    
    def preferences(self, command):
        self.choices.append(command)
        
    def execute(self):
        for choice in self.choices:
            #print((list(choice.values())))
            if list(choice.values())[0]:
                print("Copying binaries --", self.src, "to ", self.rootdir)
            else:
                print("No Operation")
                
    def rollback(self):
        print("Deleting the unwanted...", self.rootdir)
        
if __name__ =="__main__":
    wizard = Wizard('python3.5.gzip', '/usr/bin')
    wizard.preferences({'python': True})
    wizard.preferences({'java':False})
    wizard.execute()