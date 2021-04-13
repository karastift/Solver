import os
import time
import imghdr

class Menu:
    # general vars
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    WAITTIME = 3
    # first menu vars
    ABOVEFIRSTMENUTEXT = f'{BOLD}General options:{ENDC}\n'
    FIRSTMENUTEXT = f'{BOLD}0.{ENDC} Exit.\n\n{BOLD}1.{ENDC} Calculate sphere values.\n\n{BOLD}2.{ENDC} Coming soon.\n\n'
    INVALIDOPTIONTEXT = f'{FAIL}The chosen option is invalid. Please just type integers: {BOLD}\'<option>\'{ENDC}'
    GOODBYETEXTERROR = f'\n\n{BOLD}Goodbye.{ENDC}\nPlease open an {BOLD}issue{ENDC} on {BOLD}Github{ENDC} if you have any problem with the software.{ENDC}\n\n{UNDERLINE}https://github.com/karastift/Solver.git\n'
    GOODBYETEXT = f'{BOLD}Goodbye.{ENDC}'
    exited = False
    # sphere menu vars
    imagePath = str()
    noneText = imagePath if imagePath else f'{WARNING}None{ENDC}'
    imageText = f'{OKGREEN}selected image{ENDC}' if imagePath else f'{WARNING}image required{ENDC}'
    ABOVEMENUTEXT = f'{BOLD}Sphere options:{ENDC}\n\nSelected image: {noneText}\n\n'
    SPHEREMENUTEXT = f'{BOLD}0.{ENDC} Return.\n\n{BOLD}1.{ENDC} Enter path to image of tasks.\n\n2.{ENDC} Get values {imageText}.\n\n'
    VALIDIMAGEEXT = ['png', 'jpg', 'jpeg']

    def __init__(self):
        self.firstMenu()
    
    def refreshVariables(self):
        self.noneText = f'{self.OKGREEN}{self.imagePath}{self.ENDC}' if self.imagePath else f'{self.WARNING}None{self.ENDC}'
        self.imageText = f'{self.OKGREEN}selected image{self.ENDC}' if self.imagePath else f'{self.WARNING}Image required{self.ENDC}'
        self.ABOVEMENUTEXT = f'{self.BOLD}Sphere options:{self.ENDC}\n\nSelected image: {self.noneText}\n\n'
        self.SPHEREMENUTEXT = f'{self.BOLD}0.{self.ENDC} Return.\n\n{self.BOLD}1.{self.ENDC} Enter path to image of tasks.\n\n2.{self.ENDC} Get values ({self.imageText}).\n\n'

    def firstMenu(self):
        try:
            self.screenClear()
            print(self.ABOVEFIRSTMENUTEXT)
            print(self.FIRSTMENUTEXT)
            option = input('What do you want to do?\n: ')
            if option == '0':
                self.exited = True
                exit()
            elif option == '1':
                self.sphereMenu()
            else:
                print(self.INVALIDOPTIONTEXT)
                time.sleep(self.WAITTIME)
                self.firstMenu()
        except:
            if self.exited:
                print(self.GOODBYETEXT)
            else:
                print(self.GOODBYETEXTERROR)

    def sphereMenu(self):
        try:
            self.refreshVariables()
            self.screenClear()
            print(self.ABOVEMENUTEXT)
            print(self.SPHEREMENUTEXT)
            option = input('Choose option\n: ')
            if option == '0':
                self.firstMenu()
            elif option == '1':
                self.screenClear()
                print(self.ABOVEMENUTEXT)
                print(self.SPHEREMENUTEXT)
                path = input('Enter path: ')
                if self.checkImagePath(path):
                    pass
                else:
                    print(f'{self.FAIL}\'{path}\' does not lead to a valid image.{self.ENDC}')
                    time.sleep(self.WAITTIME)
                self.sphereMenu()
            else:
                print(self.INVALIDOPTIONTEXT)
                time.sleep(self.WAITTIME)
                self.sphereMenu()
        except:
            self.firstMenu()

    def checkImagePath(self, imagePath):
        if os.path.isfile(f'./{imagePath}') and imghdr.what(f'./{imagePath}') in self.VALIDIMAGEEXT:
            self.imagePath = f'./{imagePath}'
            return True
        elif os.path.isfile(imagePath) and imghdr.what(f'{imagePath}') in self.VALIDIMAGEEXT:
            self.imagePath = imagePath
            return True
        else:
            return False

    def screenClear(self):
        if os.name == 'posix':
            os.system('clear')
        else:
            os.system('cls')
M = Menu()