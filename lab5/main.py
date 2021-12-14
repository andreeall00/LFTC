from copy import deepcopy

from grammar import Grammar

NORMAL_STATE = "q"
BACK_STATE = "b"
FINAL_STATE = "f"  # successful - w part of L(G)
ERROR_STATE = "e"  # unsuccessful - w not part of L(G)


class Config:
    def __init__(self, startSymbol):
        self.s = NORMAL_STATE  # state of parsing
        self.i = 0  # position of current symbol in input sequence
        self.alpha = []  # working stack - stores the way the parse is build
        self.beta = [startSymbol]  # input stack - part of tree to be build

    def __str__(self):
        return "State: " + self.s + ", position of symbol in sequence: " + str(self.i) + ", working stack: " + str(
            self.alpha) + ", input stack " + str(self.beta)


def recursiveDescendent(grammar, sequence):
    config = Config(grammar.S)
    while config.s != FINAL_STATE and config.s != ERROR_STATE:
        # print(config)
        if config.s == NORMAL_STATE:
            if config.i == len(sequence) and len(config.beta) == 0:
                # SUCCESS
                config.s = FINAL_STATE
                # END SUCCESS
            elif len(config.beta) == 0:
                config.s = BACK_STATE
            else:
                if config.beta[0] in grammar.N:
                    # EXPAND
                    symbol = config.beta[0]
                    y1 = grammar.P[symbol][0]
                    config.alpha.append((symbol, y1))
                    config.beta = y1 + config.beta[1:]
                    # END EXPAND
                else:
                    if config.i == len(sequence):
                        config.s = BACK_STATE
                    elif config.beta[0] == sequence[config.i]:
                        # ADVANCE
                        config.i += 1
                        config.alpha.append(config.beta[0])
                        config.beta = config.beta[1:]
                        # END ADVANCE
                    else:
                        config.s = BACK_STATE
        else:
            if config.s == BACK_STATE:
                if config.alpha[-1] in grammar.E:
                    # BACK
                    config.i -= 1
                    term = config.alpha.pop(-1)
                    config.beta = [term] + config.beta
                    # END BACK
                else:
                    # ANOTHER TRY
                    lastProduction = config.alpha[-1]
                    productions = grammar.P[lastProduction[0]]
                    prods = []
                    for p in productions:
                        prods.append((lastProduction[0], p))
                    nextProduction = getNext(lastProduction, prods)
                    if nextProduction:
                        config.s = NORMAL_STATE
                        config.alpha.pop(-1)
                        config.alpha.append((nextProduction[0], nextProduction[1]))
                        config.beta = config.beta[len(lastProduction[1]):]
                        config.beta = nextProduction[1] + config.beta
                    elif config.i == 0 and lastProduction[0] == grammar.S:
                        config.s = ERROR_STATE
                    else:
                        config.alpha.pop(-1)
                        config.beta = [lastProduction[0]] + config.beta[len(lastProduction[1]):]
                    # END ANOTHER TRY
    # print(config)
    if config.s == ERROR_STATE:
        return "Syntax error", []
    else:
        prods = []
        for prod in config.alpha:
            if type(prod) is tuple:
                if prod[1] in grammar.P[prod[0]]:
                    prods.append(prod)
        print("Productions", prods)
    return "No error", prods


def getNext(lastProduction, productions):
    for i in range(len(productions)):
        if lastProduction == productions[i] and i < len(productions) - 1:
            return productions[i + 1]
    return None


class Row:
    def __init__(self, index, info, parent, rightSibling):
        self.index = index
        self.info = info
        self.parent = parent
        self.rightSibling = rightSibling

    def __str__(self):
        return self.format(str(self.index), 8) + self.format(str(self.info), 15) + self.format(str(self.parent), 9) + \
               self.format(str(self.rightSibling), 8)

    def format(self, text, nrSpaces):
        while len(text) != nrSpaces:
            text += " "
        return text


class Table:
    def __init__(self):
        self.rows = []

    def add(self, row):
        self.rows.append(row)

    def getIndexOfInfo(self, symbol):
        for row in self.rows:
            if row.info == symbol:
                return row.index

    def __str__(self):
        result = "Index   Info           Parent   RightSibling\n"
        for r in self.rows:
            result += str(r) + "\n"
        return result


class ParserOutput:
    def __init__(self, productions):
        self.productions = productions
        self.table = Table()

    def parseProductions(self):
        index = 1
        terms = []
        for production in self.productions:
            current = production[0]
            children = production[1]
            if len(self.table.rows) == 0:
                parentIndex = index
                self.table.add(Row(index, current, 0, 0))
                terms.append(current)
                index += 1
            else:
                parentIndex = self.table.getIndexOfInfo(current)
            pos = 0
            for child in children:
                if pos == 0:
                    self.table.add(Row(index, child, parentIndex, 0))
                else:
                    self.table.add(Row(index, child, parentIndex, self.table.getIndexOfInfo(children[pos - 1])))
                terms.append(current)
                index += 1
                pos += 1
        return self.table

    def __str__(self):
        return str(self.table)


def readSequence(lines):
    seq = []
    for line in lines:
        elms = line.split("'")
        seq.append(elms[1])
    print("Sequence", seq)
    return seq


if __name__ == "__main__":
    # gr = Grammar("g1.in")
    gr = Grammar("g2.in")

    while True:
        print(
            "0.Exit\n1.Show all nonterminals\n2.Show all terminals\n3.Show productions\n4.Show productions of non-terminal\n5.Check\n6.Parse")
        choice = int(input(">>"))
        if choice == 0:
            break
        elif choice == 1:
            print(gr.N)
        elif choice == 2:
            print(gr.E)
        elif choice == 3:
            print(gr.P)
        elif choice == 4:
            symbol = input(">>>")
            print(gr.show(symbol))
        elif choice == 5:
            print(gr.check())
        elif choice == 6:
            # with open("seq.txt") as file:
            #     lines = file.readlines()
            #     seq = readSequence(lines)
            # response, prods = recursiveDescendent(gr, seq)
            response, prods = recursiveDescendent(gr, ["var", "a", ";", "a", "=", "1", "+", "2", "+", "3", ";"])
            # response, prods = recursiveDescendent(gr, ["var", "a", ";", "a", "=", "1", "+", "2", "+", "3"])
            print("Result", response)
            print("Productions", prods)
            table = ParserOutput(prods).parseProductions()
            print(str(table))
            # f = open("out1.txt", "w")
            f = open("out2.txt", "w")
            # f = open("parsingTable.txt", "w")
            f.write(str(table))
            f.close()
