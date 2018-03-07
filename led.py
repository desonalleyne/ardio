from digitalOut import DigitalOut

class Led(DigitalOut):
    def __init__(self, pin, name="Unnamed"):                              
        pinType = self.__class__.__name__
        super(Led, self).__init__(pin, name, pinType)

    def get_classname(self):
        return 

   
