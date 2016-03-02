# Kevin Cunanan
# username: kcunanan
# Lab2

from struct import *
import sys

def LZ77_search(search, look_ahead):
    ls = len(search)
    llh = len(look_ahead)

    if(ls == 0):
        return(0, 0, look_ahead[0])

    if(llh == 0):
        return(-1, -1, "")

    best_offset = 0
    best_length = 0

    buf = search+look_ahead

    search_pointer = ls

    for i in range (0, ls):
        offset = 0
        length = 0
        while buf[i+length] == buf[search_pointer+length]:
            length += 1
            if search_pointer + length == len(buf):
                length -= 1
                break
        if length > best_length:
            best_offset = i
            best_length = length
    return(best_offset, best_length, buf[search_pointer+best_length])

def main():
    MAX_SEARCH = 1024
    MAX_LOOKAHEAD = 64
    r = open(str(sys.argv[1]) ,"rb")
    inputme = r.read(MAX_SEARCH+MAX_LOOKAHEAD)
    search_idx = 0
    lookahead_idx = 0
    search = inputme[search_idx:lookahead_idx]
    lookahead = inputme[lookahead_idx:lookahead_idx+MAX_LOOKAHEAD]
    f = open('compressed.bin', 'wb')
    while len(lookahead) != 0:
        (offset, length, char) = LZ77_search(search, lookahead)
        lookahead_idx += length + 1
        shifted_offset = offset << 6
        offset_and_length = shifted_offset + length
        ol_bytes = pack('>H', offset_and_length)
        f.write(ol_bytes)
        f.write(char)
        print "<"+str(offset)+","+str(length)+","+str(char)+">"
        inputme = inputme + r.read(length+1)
        if (lookahead_idx - search_idx) > MAX_SEARCH:
            search_idx = lookahead_idx - MAX_SEARCH
        search = inputme[search_idx:lookahead_idx]
        lookahead = inputme[lookahead_idx:lookahead_idx+MAX_LOOKAHEAD]
    f.close
main()
