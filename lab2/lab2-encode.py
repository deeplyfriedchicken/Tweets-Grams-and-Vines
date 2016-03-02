# Kevin Cunanan
# username: kcunanan
# Lab2
# encoder

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
    f = open('compressed.bin', 'wb')
    MAX_SEARCH = int(sys.argv[2])
    N = MAX_SEARCH
    shift = 0
    for i in range (0, 17):
        if (65536 >> i) <= MAX_SEARCH:
            shift = i
            break
    print i
    M = 65536 - MAX_SEARCH
    shift_l = 16 - shift
    MAX_LOOKAHEAD = M >> shift_l
    print MAX_LOOKAHEAD
    if MAX_LOOKAHEAD <= 0:
        raise ValueError('Value of MAX_SEARCH too large')
    else:
        f.write(pack('>H', shift)) # put N into header of file for decoder
        f.write(pack('>H', MAX_SEARCH)) # put N into header of file for decoder
    r = open(str(sys.argv[1]) ,"rb")
    inputme = r.read(MAX_SEARCH + MAX_LOOKAHEAD)
    search_idx = 0
    lookahead_idx = 0
    while lookahead_idx < len(inputme):
        search = inputme[search_idx:lookahead_idx]
        lookahead = inputme[lookahead_idx:lookahead_idx + MAX_LOOKAHEAD]
        (offset, length, char) = LZ77_search(search, lookahead)
        shifted_offset = offset << shift
        print shifted_offset
        offset_and_length = shifted_offset + length
        ol_bytes = pack('>H', offset_and_length)
        f.write(ol_bytes)
        f.write(char)
        print (offset, length, char)
        inputme = inputme + r.read(MAX_LOOKAHEAD)
        lookahead_idx += length + 1
        search_idx = lookahead_idx - MAX_SEARCH
        if search_idx < 0:
            search_idx = 0
    f.close
main()
