import re
from SymbolTable import SymbolTable


class Scanner:
    def __init__(self):
        self.reservedWords = ["cst", "verify", "yes", "no", "print", "var", "read", "return", "list", "go", "as",
                              "with"]
        self.operators = ["+", "-", "*", "div", "mod", "=", "is", ">", ">=", "<", "<=", "and", "or", "not", "."]
        self.separators = [":", ";", " ", "[", "]"]
        self.identifierRegex = "^[a-zA-Z]([a-zA-Z]|_|[0-9])*$"
        self.integerRegex = "^(([+-]?[1-9][0-9]*)|0)$"
        self.characterRegex = "^'([a-zA-Z]|[0-9])'$"
        self.stringRegex = "^\"([a-zA-Z]|[0-9])([a-zA-Z]|[0-9])*\"$"
        self.booleanRegex = "^(T|F)$"
        self.pif = []
        self.__pifFile = "./results/PIF.out"
        self.st = SymbolTable()
        self.__stFile = "./results/ST.out"

    def scan(self, programFile):
        errors = False
        with open(programFile) as pf:
            lineNr = 0
            for line in pf:
                lineNr += 1
                line = line.strip()

                tokens = self.getTokens(line)
                for token in tokens:
                    if token in self.reservedWords or token in self.operators or token in self.separators:
                        self.pif.append((token, -1))
                    elif re.search(self.identifierRegex, token):
                        self.pif.append(("id", self.st.add(token)))
                    elif re.search(self.integerRegex, token) or re.search(self.characterRegex, token) or re.search(
                            self.stringRegex, token) or re.search(self.booleanRegex, token):
                        self.pif.append(("const", self.st.add(token)))
                    else:
                        errors = True
                        print("Lexical error at line", lineNr, ": " + token)
        pf.close()
        if not errors:
            print("Lexically correct")

        pifFile = open(self.__pifFile, "w+")
        for pair in self.pif:
            pifFile.write(str(pair) + "\n")
        pifFile.close()

        stFile = open(self.__stFile, "w+")
        stFile.write("--- represented as a binary search tree ---\n")
        stFile.write(str(self.st))
        stFile.close()

    def getTokens(self, line):
        characters = list(line)
        tokens = []
        token = ""
        pos = 0

        while pos < len(characters):
            if characters[pos] in self.separators:
                if len(token) > 0:
                    tokens.append(token)
                    token = ""
                if characters[pos] != " ":
                    tokens.append(characters[pos])
                pos += 1
            elif (characters[pos] == "<" or characters[pos] == ">") and characters[pos + 1] == "=":
                if len(token) > 0:
                    tokens.append(token)
                    token = ""
                tokens.append(characters[pos] + characters[pos + 1])
                pos += 2
            elif characters[pos] in self.operators:
                if len(token) > 0:
                    tokens.append(token)
                    token = ""
                tokens.append(characters[pos])
                pos += 1
            elif characters[pos] == "\"":
                if len(token) > 0:
                    tokens.append(token)
                token = characters[pos]
                pos += 1
                while pos < len(characters) and characters[pos] != "\"":
                    token += characters[pos]
                    pos += 1
                if pos < len(characters):
                    token += characters[pos]
                    pos += 1
                tokens.append(token)
                token = ""
            elif characters[pos] == "\'":
                if len(token) > 0:
                    tokens.append(token)
                token = characters[pos]
                pos += 1
                while pos < len(characters) and characters[pos] != "\'":
                    token += characters[pos]
                    pos += 1
                if pos < len(characters):
                    token += characters[pos]
                    pos += 1
                tokens.append(token)
                token = ""
            else:
                token += characters[pos]
                pos += 1
        if len(token) > 0:
            tokens.append(token)

        return tokens
