from grammar import Grammar

NORMAL_STATE = "q"
BACK_STATE = "b"
FINAL_STATE = "f"  # successful - w part of L(G)
ERROR_STATE = "e"  # unsuccessful - w not part of L(G)


def getNext(lastProduction, productions):
    for i in range(len(productions)):
        if lastProduction == productions[i] and i < len(productions) - 1:
            return productions[i + 1]
    return None


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
        print(config)
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
    if config.s == ERROR_STATE:
        return False
    else:
        prodRules = []
        for prod in config.alpha:
            if type(prod) is tuple:
                if prod[1] in grammar.P[prod[0]]:
                    prodRules.append(prod)
        print("Production Rules", prodRules)
    return True


if __name__ == "__main__":
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
            print(recursiveDescendent(gr, ["var", "a", ";", "a", "=", "1", ";"]))
