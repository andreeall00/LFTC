from FiniteAutomaton import FiniteAutomaton

fa = FiniteAutomaton("FA.in")
while True:
    print(
        "0.Exit\n1.Show all states\n2.Show alphabet\n3.Show transitions\n4.Show initial state\n5.Show final states\n6.Verify sequence")
    choice = int(input(">>"))
    if choice == 0:
        break
    elif choice == 1:
        print(fa.Q)
    elif choice == 2:
        print(fa.E)
    elif choice == 3:
        print(fa.delta)
    elif choice == 4:
        print(fa.q0)
    elif choice == 5:
        print(fa.F)
    elif choice == 6:
        sequence = input(">>>")
        print(fa.isAccepted(sequence))
