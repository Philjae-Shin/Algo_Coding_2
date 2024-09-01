while True:
    # Use try to Handle expections
    try:
        print(input())
    # if there is no input -> EOF (End Of File) -> EOFError -> go to expect scope -> break
    except EOFError:
        break
    