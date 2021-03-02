
def read_text(filename) :
    try :
        file = open(filename, 'r')
    except FileNotFoundError as e :
        print(e)

    else :
        s = file.read()
        file.close()

if __name__ == '__main__' :
    read_text('maria.txt')
