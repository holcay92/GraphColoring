if __name__ == '__main__':
    # Take the input file into variable
    f = open("sample3.txt", encoding='utf-8-sig')

    file = open("testsample3.txt", "a")
    file.write(str(f.read()))
    file.close()


