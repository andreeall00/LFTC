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
            if key not in self.N:
                return False
            for value in self.P[key]:
                tokens = value.split(" ")
                for token in tokens:
                    if token not in self.N and token not in self.E:
                        return False
        return True

    def show(self, symbol):
        return self.P[symbol]

    def __readFromFile(self):
        with open(self.__file) as file:
            self.__setNonTerminalSymbols(file.readline())
            self.__setTerminalSymbols(file.readline())
            self.__setStartSymbol(file.readline())
            self.__setProductions(file.readlines())

    def __setNonTerminalSymbols(self, line):
        self.N = line.strip().split(",")

    def __setTerminalSymbols(self, line):
        self.E = line.strip().split(",")

    def __setStartSymbol(self, line):
        self.S = line.strip()

    def __setProductions(self, lines):
        transitions = []
        for trans in lines:
            transitions.append(trans.replace('\n', ''))
        for transition in transitions:
            terms = transition.split("->")
            key = terms[0].strip()
            self.P[key] = []
            for productions in terms[1].split("|"):
                productions = productions.strip().split(" ")
                self.P[key].append(productions)
