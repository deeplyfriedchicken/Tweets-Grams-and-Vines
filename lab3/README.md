# Lab3 CMC-CS181
## March 5, 2016
## Kevin Cunanan

## How to Use
* Run `python lab3.py filename`
* This generates the JSON and Huffman code in pretty json.
* Check *huffpressed.txt* for the compressed file.

* To *decode* use `python lab3-decode.py filename`
* The decoder will append "decode" to the finished file.

## Analysis
* Despite inputting two dictionaries, the compressed file is considerably smaller (from 45K to 24K).
* Compression time is reasonably fast even with printing on the terminal.

# Lab 3C
## Analysis
* Time: The compressor is actually considerably slow. This is especially noticeable when the files are larger. Even with a 675kb file, the compressor took minutes. The RAW image is still converting possibly never.
* Compared to LZ77 at 4096, the Huff compresses slightly worse. LZ77 compressed to 21K whereas Huffman compressed 23K (base 36K).
* Compression: The files I could compress were around 1.8 times compressed.
* OVERALL. Large files could not compress effectively. I stopped the WAV file after about 2 hours and it had only finished 15%.
