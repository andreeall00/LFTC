from grammar import Grammar

gr = Grammar("g2.in")

while True:
    print(
        "0.Exit\n1.Show all nonterminals\n2.Show all terminals\n3.Show productions\n4.Show productions of non-terminal\n5.Check")
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






##


