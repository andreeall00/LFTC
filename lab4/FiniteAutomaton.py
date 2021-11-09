import re


class FiniteAutomaton:
    def __init__(self, fileName):
        self.__file = fileName
        self.Q = []  # finite set of states
        self.E = []  # finite alphabet
        self.delta = {}  # transition functions
        self.q0 = None  # initial state
        self.F = []  # set of final states
        self.__readFromFile()

    def isAccepted(self, sequence):
        currentState = self.q0
        for character in sequence:
            if (currentState, character) in self.delta.keys():
                currentState = self.delta[(currentState, character)]
            else:
                return False
        return currentState in self.F

    def __readFromFile(self):
        with open(self.__file) as file:
            self.__setAllStates(file.readline())
            self.__setAlphabet(file.readline())
            self.__setTransitions(file.readline())
            self.__setInitialStates(file.readline())
            self.__setFinalStates(file.readline())

    def __setAllStates(self, line):
        self.Q = line.strip().split(",")

    def __setAlphabet(self, line):
        self.E = line.strip().split(",")

    def __setTransitions(self, line):
        transitions = line.strip().split(",")
        for transition in transitions:
            element0 = transition[0]
            element1 = transition[2]
            element2 = transition[4]
            self.delta[(element0, element1)] = element2

    def __setInitialStates(self, line):
        self.q0 = line.strip()

    def __setFinalStates(self, line):
        self.F = line.strip().split(",")
