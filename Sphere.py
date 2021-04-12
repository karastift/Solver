import math

class Sphere:

    radius = float()
    Ao = float()
    volume = float()

    def getValues(self):

        if self.radius:
            self.radToAoV()
        elif self.Ao:
            self.AoToRV()
        else:
            self.vToRAo()

        finalValues = {
            'r': self.radius,
            'Ao': self.Ao,
            'V': self.volume
        }
        
        self.resetValues()
        return finalValues

    def radToAoV(self):
        radius = self.radius
        volume = (4/3) * (radius ** 3.0) * math.pi
        area = 4 * (radius ** 2) * math.pi

        self.volume = volume
        self.Ao = area

    def vToRAo(self):
        V = self.volume
        radius = ((3 * V) / (4 * math.pi)) ** (1/3)
        area = 4 * math.pi * (radius ** 2)

        self.radius = radius
        self.Ao = area

    def AoToRV(self):
        Ao = self.Ao
        radius = (Ao / (4 * math.pi)) ** (1/2)
        volume = (4/3) * math.pi * (radius ** 3)

        self.radius = radius
        self.volume = volume

    def resetValues(self):

        self.radius = float()
        self.Ao = float()
        self.volume = float()