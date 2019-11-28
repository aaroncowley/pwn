import sys


def read_pattern(pat):
    caps =   list(range(0x41, 0x5B))
    lowers = list(range(0x61, 0x7B))
    digits = list(range(0x30, 0x40))

    off = -1

    for i, char in enumerate(pat,start=0):
        if ord(char) in caps:
            try:
                pat = pat[i:i+3] 
                cap = char
                low = next(char)
                if low not in lowers:
                    raise Exception
                dig = next(char)
                if dig not in digits:
                    raise Exception
                off = i
            except:
                print('invalid pattern given')
                exit(1)
           
            print(pat)
            break

    if off == -1:
        print('invalid pattern')
        exit(1)
        
    cap = ord(pat[0]) - 0x41
    low = ord(pat[1]) - 0x61
    dig = ord(pat[2]) - 0x30

    return (dig + low * 10 + cap * 260)*3

if __name__ == '__main__':
    pattern = sys.argv[1]

    if len(pattern) < 3:
        print("need at least 3 characters")
        exit(1)

    print(read_pattern(pattern))
