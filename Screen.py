class Screen:

    def __init__(self, window, colorRGB):
        self.surface = window.screen
        self.elements = []
        self.color = colorRGB
        self.state = {}

    def elementsToDisplay(self):
        self.elements = []
    pass
    
    def elementsToDisplay(self):
        pass

    def update(self):
        self.elementsToDisplay()


    def display(self):
        self.elementsToDisplay()
        for e in self.elements:
            e.display(self.surface)
        
        
