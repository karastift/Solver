import pytesseract
from PIL import Image
from Sphere import Sphere#
import re

class Solver:

    def convertImage(self, path: str):
        pytesseract.pytesseract.tesseract_cmd = r'Tesseract-OCR\tesseract.exe'
        imageText = pytesseract.image_to_string(Image.open(path))
        return imageText
                    
    def convertString(self, text: str) -> dict:
        result = dict()
        string = text
        string = string.split(sep=' ')
        alphabet = 'qwertzuiopasdfghjklöäüyxcvbnm'
        for i in range(0, len(string), 2):
            result[string[i]] = dict()
            curr = result[string[i]]
            sweet = string[i+1]
            valueType = re.sub('0', 'o', re.sub('[=]', '', sweet[:2]).lower())
            value = re.sub('[,]', '.', re.sub('[oO]', '0', sweet[sweet.index('=')+1:])).lower()
            if value[-3] in alphabet:
                value = value[:len(value) - 3]
            elif value[-2] in alphabet:
                value = value[:len(value) - 2]
            elif value[-1] in alphabet:
                value = value[:len(value) - 1]
            else: pass
            
            result[string[i]] = {
                valueType: value
            }

        return result

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

    def printSolution(self, solution: dict):
        OKBLUE = '\033[94m'
        OKCYAN = '\033[96m'
        ENDC = '\033[0m'
        space = ' ' * 4
        for key in list(solution.keys()):
            vals = solution[key]
            print(f'{OKBLUE}{key}){ENDC}')
            for key2 in list(vals.keys()):
                print(f'{space}{OKCYAN}{key2}:{ENDC} {vals[key2]}')