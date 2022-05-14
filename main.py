from gui import *


def main():

    window = Tk()
    widgets = GUI(window)
    window.geometry('625x200')
    window.resizable(False, False)
    window.title('Daily Tips')
    window.mainloop()


if __name__ == '__main__':
    main()
