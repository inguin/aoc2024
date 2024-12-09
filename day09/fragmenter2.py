#! /usr/bin/python

import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
line = open(filename).read().strip()

gap = False
files = []
gaps = []
blockaddr = 0
fileid = 0

for digit in line:
    if not gap:
        files.append((blockaddr, int(digit), fileid))
    else:
        gaps.append((blockaddr, int(digit)))
        fileid += 1
    blockaddr += int(digit)
    gap = not gap

fileidx = len(files) - 1

while fileidx >= 0:
    fileaddr, filesize, fileid = files[fileidx]
    for gapidx, (gapaddr, gapsize) in enumerate(gaps):
        if gapaddr < fileaddr and gapsize >= filesize:
            print(f"Moving file {fileid} (size {filesize}) from {fileaddr} to {gapaddr}")
            files[fileidx] = (gapaddr, filesize, fileid)
            gaps[gapidx] = (gapaddr + filesize, gapsize - filesize)
            break
    fileidx -= 1

checksum = 0
for (blockaddr, size, fileid) in files:
    checksum += sum(a * fileid for a in range(blockaddr, blockaddr + size))
print(checksum)
