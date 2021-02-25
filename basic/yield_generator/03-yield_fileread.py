from typing import Any

def file_read(filename: Any) -> Any :
    with open(filename) as file :
        while True :
            line = file.readline()
            if line == '':
                break
            yield line.strip('\n')




if __name__ == '__main__' :
    for i in file_read('words.txt') :
        print(i)

    g = file_read('words.txt')

    print(g)

    while True :
        try :
            print(next(g))
        except :
            print('Done')
            break
        
