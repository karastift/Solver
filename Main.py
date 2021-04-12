from Solver import Solver
import pprint

tasks = {
    'a': {
        'r': 39
    },
    'b': {
        'Ao': 260
    },
    'c': {
        'V': 980
    },
    'd': {
        'Ao': 1985.96
    },
    'e': {
        'Ao': 60000
    },
    'f': {
        'r': 0.71
    },
    'g': {
        'Ao': 36
    },
    'h': {
        'V': 36
    }
}

def main():
    S = Solver()
    
    # print(S.convertImage('example.png'))
    convertedString = S.convertString('a) r=39cm c) V=980cm3 e) A0=5oooodm2 g) AO=35m2 b) AO=26OCm2 d) Ao=1985,96m2 f) r=O,71m h) V=36m3')
    solution = S.calculateSphere(tasks)
    S.printSolution(solution)

if __name__ == '__main__':
    main()