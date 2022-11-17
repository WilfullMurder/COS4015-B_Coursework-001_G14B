from State import State


def main():
    s = State
    s.State(s, 0,0,0,0)
    print(s.toString(s))
    print(s.isValid(s))
    s.newState(s,"0111")
    print(s.toString(s))
    print(s.isValid(s))
    s.newState(s,"0101")
    print(s.toString(s))
    print(s.isValid(s))
    s.newState(s,"1012")
    print(s.toString(s))
    print(s.isValid(s))


main()