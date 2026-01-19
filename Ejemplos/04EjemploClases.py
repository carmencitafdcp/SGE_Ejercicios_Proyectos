class Droid:
    def __init__(self, name: str):
        self.name = name

    @property
    def name(self) -> str:
        return self.name
    
    @name.setter
    def name(self, name:str) -> None:
        self.name = name

    def switch_on(self):
        self.power_on = True
        print("Hi! I am Carmen, how can I help you?")
        
    def switch_off(self):
        self.power_on = False
        print("Bye bye!")


caca = Droid()
caca.switch_on()

droid = Droid('BB-8')
print(droid.name)
