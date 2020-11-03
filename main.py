from model.finiteAutomata import FiniteAutomata


def menu(self):
    exit = True
    while (exit):
        print(
            "1 - print alphabet"
            "\n2 - print transitions\n"
            "3 - print initial state\n"
            "4 - print final states\n"
            "5 - print states\n"
            "6 - test"
            "\n7 - exit\n")
        comm = int(input())
        if (comm == 1):
            print(self.E)
        if (comm == 2):
            print(self.S)
        if (comm == 3):
            print(self.q0)
        if (comm == 4):
            print(self.F)
        if (comm == 5):
            print(self.Q)
        if (comm == 6):
            seq = input()
            print(self.check(seq))
        if (comm==7):
            exit=False


if __name__ == '__main__':


    finiteAutomata = FiniteAutomata.fromFile('fa1.txt')
    print(finiteAutomata)
    menu(finiteAutomata)









