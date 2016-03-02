# Lab2 CMC-CS181
## February 22, 2016
## Kevin Cunanan

## Compression Results w/ N = 1024, M = 64
### Book 1
* Entropy: **4.72271916074**
* Entropy after Compression: **7.14226785559**

### Book 2
* Entropy: **4.46061169039**
* Entropy after: **7.09011495039**

### Book 3
* Entropy before: **4.64214241863**
* Entropy after: **7.14721625525**

### 1M
* Entropy before: **8.18468347865**
* Entropy after: **7.05253754819**

### 1.1M High Resolution Image
* Entropy before: **8.15170985354**
* Entropy after: **7.06173557714**

## Pick a file that might compress well
* Even an old mp4 voice memo didn't compress well even though it was 11M. Entropy before was **8.14236679042**. After it was **7.05859500942**. However, the file size was 7M larger...I think the big problem is our M and N are not large enough (I didn't do the extra step and make it customizable). We would need a very large file that has lots of repeats to compress the file well.

## BONUS
I figured why not do the extra credit so I implemented the ability to change M and N at runtime by the command `python lab2-encode.py filename N`. I did the following changes on book1.txt.
File Size is compared to 46K.
### 256
* Speed: Fast
* File size: 127K
### 512
* Speed: Slightly slower, no difference on decode
* File size: 110K
### 2048
* Speed: Significantly slower on compression, still just as fast as 256 on decompression
* File size: 86K
### 4096
* Speed: Around 10 seconds, definitely slower than 2048
* File size: 78K

So file size continuously went down!

## OVERALL
* Small files like the books, and 1M or 11M files ultimately ended up not getting compressed efficiently. File sizes were sometimes 3x as large as the original file. The entropy of each file was always lower than the original file size. I think Zip, gzip, and other algorithms do a second pass because the data becomes more homogenous and easier to compress the second time around. The first time reduces the amount of new characters, and the second compress actually compresses.
