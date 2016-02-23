# Lab2 CMC-CS181
## February 22, 2016
## Kevin Cunanan

## Compression Results
### Book 1
* Entropy: **4.72271916074**
* Entropy after Compression: **2.4925355543**

### Book 2
* Entropy: **4.59093557303**
* Entropy after: **2.44860769173**

### Book 3
* Entropy before: **4.63073054275**
* Entropy after: **2.46187268164**

### 1M
* Entropy before: **3.89849351986**
* Entropy after: **8.18468347865**

## Pick a file that wouldn't compress well.
* I chose a 4K 1.1M image since it would probably have a lot of differing bytes because each pixel consists of a slightly different color. The depth of the color would possibly be bad for a compressor?
* Result: Entropy before was **8.15170985354** and after it was **3.85498543336**. So it unfortunately still compressed poorly. There needs to be a lot of unique data that forces the algorithm to constantly repeat itself and somehow create a larger and less.
* Even an old mp4 voice memo didn't compress well even though it was 11M. I think the big problem is our M and N are not large enough (I didn't do the extra step and make it customizable). We would need a very large file that has lots of repeats to compress the file well.

## OVERALL
* Small files like the books, and 1M or 11M files ultimately ended up not getting compressed efficiently. File sizes were sometimes 3x as large as the original file. The entropy of each file was always lower than the original file size. I think Zip, gzip, and other algorithms do a second pass because the data becomes more homogenous and easier to compress the second time around. The first time reduces the amount of new characters, and the second compress actually compresses.
