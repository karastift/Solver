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
OKBLUE = '\033[94m'
FAIL = '\033[91m'
OKCYAN = '\033[96m'
ENDC = '\033[0m'
def main():
    S = Solver()
    # pprint.pprint(S.calculateSphere(tasks))
    solution = S.calculateSphere(tasks)
    space = ' ' * 4
    for key in list(solution.keys()):
        vals = solution[key]
        print(f'{OKBLUE}{key}){ENDC}')
        for key2 in list(vals.keys()):
            print(f'{space}{OKCYAN}{key2}:{ENDC} {vals[key2]}')
    
    
    # print(S.convertImage('example.png'))

if __name__ == '__main__':
    main()
    input()