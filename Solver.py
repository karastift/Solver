import pytesseract
from PIL import Image
from Sphere import Sphere

exampleTasks = {
    'a': {
        'r': 3
    },
    'b': {
        'Ao': 50
    }
}

class Solver:

    def convertImage(self, path: str):
        pytesseract.pytesseract.tesseract_cmd = r'Tesseract-OCR\tesseract.exe'
        string = pytesseract.image_to_string(Image.open(path))
        string = "".join(string.split())
        print(string)
        finalDict = dict()

        alphabet = 'qwertyuiopasdfghjklzxcvbnm'
        curr = 0
        for char in string:
            print(char)
            if char in alphabet:
                valueType = string[string.index(char)+2]
                value = str()
                for nextChar in string[string.index(valueType)+2:]:
                    
                    print("nextchar", nextChar)
                    try:
                        int(nextChar)
                        value += nextChar
                    except:
                        value = float(value)
                        break
                finalDict[char] = {
                    valueType: value
                }
        return finalDict
                    


    def calculateSphere(self, problems: dict) -> dict:
        
        S = Sphere()
        solutionDict = {}

        for key in list(problems.keys()):
            task = problems[key]
            valueType = next(iter(task.keys()))
            value = next(iter(task.values()))
            
            if valueType == 'r':
                S.radius = value

            elif valueType == 'Ao':
                S.Ao = value

            else:
                S.volume = value

            solutionDict[key] = S.getValues()
      
        return solutionDict
