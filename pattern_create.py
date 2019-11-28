'''
Create a pattern of input text for use in memory corruption        
Obviously inspired by metasploit's pattern_create.rb
I dislike ruby so here is this in current python
                          
Happy Hunting,
                                         
acow 
'''

import sys


def ensure_int(fn):
    def wrapper(num):
        return fn(int(num))
    return wrapper

@ensure_int
def spit(length):
    out = ""
    # sets of chars to be appended
    caps =   list(range(0x41, 0x5B))
    lowers = list(range(0x61, 0x7B))
    digits = list(range(0x30, 0x40))
    
    last_cap = 0x00
    last_low = 0x00
    last_dig = 0x00

    for i in range(length):
        if len(out) > 0:
            end = out[-1]
        else:
            out += chr(caps[0])
            last_cap = ord(out[-1])
            continue

        if ord(end) in caps:
            if last_low == 0x00 or (last_low == 0x7A and last_dig == 0x39):
                out += chr(lowers[0])
            elif last_dig != 0x39:
                out += chr(last_low)
            else:
                out += chr(last_low+1)

            last_low = ord(out[-1])
            continue

        elif ord(end) in lowers:
            if last_dig == 0x39 or last_dig == 0x00:
                out += chr(digits[0])
            else:
                out += chr(last_dig+1)

            last_dig = ord(out[-1])
            continue

        elif ord(end) in digits:
            if last_cap == 0x5A:
                out += chr(caps[0])
            elif last_low != 0x7A or last_dig != 0x39:
                out += chr(last_cap)
            else:
                out += chr(last_cap+1)

            last_cap = ord(out[-1])
            continue

    return out



if __name__ == '__main__':
    length = sys.argv[1]
    if isinstance(int(length), int):
        print(spit(length)) 
                


