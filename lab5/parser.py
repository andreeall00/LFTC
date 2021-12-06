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


def recursiveDescendent(grammar, sequence):
    config = Config(grammar.S)
    while config.s != FINAL_STATE and config.s != ERROR_STATE:
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
    prodRules = []
    if config.s == ERROR_STATE:
        return False, []
    else:
        for prod in config.alpha:
            if len(prod) > 1:
                if (prod[0], prod[1]) in grammar.P:
                    prodRules.append(prod)
    return True, prodRules
