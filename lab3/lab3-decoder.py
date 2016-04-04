import json
import sys # necessary to call read file
import md5
import os

def main():
    input_file = open(sys.argv[1], "rb")

    header = json.loads(input_file.readline())
    # print header['hash']
    # print header['size']
    # print header['type']
    print header['name']

    huffman_old = json.loads(input_file.readline())

    huffman = {}
    for key, value in huffman_old.iteritems():
        huffman[str(value)] = str(key)
    binary_data = input_file.read()
    binary_string = ""
    for byte in binary_data:
        binary_string += format(ord(byte), '08b')
    if len(binary_string) % 8 != 0:
        raise ValueError('The length of this file is not a multiple of 8bits. Corrupted file.')
    decoded_data = ""
    while len(decoded_data) != header['size']:
        progress = 100 * round(float(len(decoded_data))/float(header['size']), 2)
        sys.stdout.write("\r"+ str(progress) + "% completed" )
        sys.stdout.flush()
        sub_str = ""
        i = 0
        while sub_str not in huffman:
            sub_str = binary_string[0:i]
            i += 1
        if sub_str != '':
            decoded_data += chr(int(huffman[sub_str]))
            binary_string = binary_string[i-1:] # because of the while loop
    m = md5.new(decoded_data)
    checksum = m.hexdigest()
    if checksum == header['hash']:
        w = open(header['name']+"-decode"+header['type'], "wb")
        w.write(decoded_data)
        w.close
        print ""
        print 'Files Match'
    else:
        raise ValueError('Files Do Not Match')

if __name__ == '__main__':
    main()
