from PyUI.Screen import Screen #will need a screen object to extend
from PyUI.PageElements import * #will need the base element classes to extend

##create the custom screen class
class ExampleScreen(Screen):
    def __init__(self, window):
        super().__init__(window, (0,0,0)) ##use the parents constructor
        ##give the screen a state for updating values and labels----
        self.state = {
            "status": "onGoing"
        }
        ##----------------------------------------------------------

    def elementsToDisplay(self): #defines what elements will be on the page
        self.elements = [
            Label((300, 200), 100, 100, self.state["status"], 14, (255,255,255)), #dynamic element needs arguments
            HelloButton(), #static elements can be defined without arguments
            WorldButton()
        ]
        

##Add custom page elements
class HelloButton(Button): #each new element should extend an element type from PyUI
    def __init__(self):
        super().__init__((200, 200), 100, 100, "Hello") #call the constructor of the parent

    def onClick(self, screen): #override the onClick method to do our bidding, MUST TAKE SCREEN AS ARGUMENT
        screen.state["status"] = "Hello" #modifies the state of the screen

class WorldButton(Button):
    def __init__(self):
        super().__init__((50, 200), 100, 100, "World")

    def onClick(self, screen):
        screen.state["status"] = "World"