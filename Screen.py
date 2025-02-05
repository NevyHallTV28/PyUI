class Screen:

    def __init__(self, window, colorRGB):
        self.surface = window.screen
        self.elements = []
        self.color = colorRGB
        self.state = {}

    def elementsToDisplay(self):
        #override this with the elements to render
        #attach the elements as a list to the screen object
        #example:
        #self.elements = [
            #Button(),
            #Label()
        #]
        pass

    def update(self):
        self.elementsToDisplay()


    def display(self):
        for e in self.elements:
            e.display(self.surface)
        
        
