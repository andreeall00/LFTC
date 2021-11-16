class Grammar:
    def __init__(self, fileName):
        self.__file = fileName
        self.N = []  # set of non-terminal symbols
        self.E = []  # set of terminal symbols
        self.P = {}  # set of productions
        self.S = []  # start symbol
        self.__readFromFile()

    def check(self):
        if self.S not in self.N:
            return False
        for key in self.P.keys():
            if key not in self.N or len(key) > 1:
                return False
            for value in self.P[key]:
                for char in value:
                    if char not in self.N and char not in self.E:
                        return False
        return True

    def show(self, symbol):
        return self.P[symbol]

    def __readFromFile(self):
        with open(self.__file) as file:
            self.__setNonTerminalSymbols(file.readline())
            self.__setTerminalSymbols(file.readline())
            self.__setProductions(file.readline())
            self.__setStartSymbol(file.readline())

    def __setNonTerminalSymbols(self, line):
        self.N = line.strip().split(",")

    def __setTerminalSymbols(self, line):
        self.E = line.strip().split(",")

    def __setProductions(self, line):
        transitions = line.strip().split(",")
        for transition in transitions:
            terms = transition.split("->")
            self.P[terms[0]] = []
            for innerTerms in terms[1].split("|"):
                self.P[terms[0]].append(innerTerms)

    def __setStartSymbol(self, line):
        self.S = line.strip()
