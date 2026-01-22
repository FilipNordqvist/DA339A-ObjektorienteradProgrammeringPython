class Rectangel:
    def __init__(self, width, height):
        self._width = width
        self._height = height
        
    @property
    def width(self):
        return f"{self._width:.1f}cm"
    
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater then zero")
    
    @property
    def height(self):
        return f"{self._height:.1f}cm"
    
    @height.setter
    def height(self,new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater then zero")
            
    @width.deleter
    def width(self):
        del self._width
        print("width deleted")
        
    @height.deleter
    def height(self):
        del self._height
        print("height deleted")


rectangel = Rectangel(3, 4)

rectangel.width = 5
rectangel.height = 6

del rectangel.width
del rectangel.height
