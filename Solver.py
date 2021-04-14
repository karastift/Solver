import pytesseract
from PIL import Image
from Sphere import Sphere
from re import sub
from os import name
from cv2 import imread

class Solver:

    def convertImage(self, path: str, option: int):
        if name == 'posix':
            pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'
        else:
            pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
        if option == 1:
            imageText = pytesseract.image_to_string(Image.open(path))
        elif option == 2:
            imageText = pytesseract.image_to_string(imread(path, 0))
        else:
            imageText = pytesseract.image_to_string(Image.open(path))

        return imageText
                    
    def convertString(self, text: str) -> dict:
        result = dict()
        string = text.replace('\n', ' ')
        string = string.split(sep=' ')
        alphabet = 'qwertzuiopasdfghjklöäüyxcvbnm'
        for i in range(0, len(string), 2):
            result[string[i]] = dict()
            sweet = string[i+1]
            try:
                valueType = sub('0', 'o', sub('[=]', '', sweet[:2]).lower())
                value = sub('[,]', '.', sub('[oO]', '0', sweet[sweet.index('=')+1:])).lower()
                if value[-3] in alphabet:
                    value = value[:len(value) - 3]
                elif value[-2] in alphabet:
                    value = value[:len(value) - 2]
                elif value[-1] in alphabet:
                    value = value[:len(value) - 1]
                else: pass
            except:
                valueType = 'ERROR'
                value = 0
            
            result[string[i]] = {
                valueType: float(value)
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
            
            elif valueType == 'ERROR':
                S.error = True

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
            print(f'{OKBLUE}{key}{ENDC}')
            for key2 in list(vals.keys()):
                print(f'{space}{OKCYAN}{key2}:{ENDC} {vals[key2]}')