from Solver import Solver

def main():
    # create menu
    S = Solver()
    convertedImage = S.convertImage('example.png')
    convertedString = S.convertString(convertedImage)
    solution = S.calculateSphere(convertedString)
    S.printSolution(solution)

if __name__ == '__main__':
    main()