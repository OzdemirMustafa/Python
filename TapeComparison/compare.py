

with open('cl2_cache_nisan20-1.csv', 'r') as t1, open('cl3_cache_nisan20-1.csv', 'r') as t2:
    fileone = t1.readlines()
    filetwo = t2.readlines()

with open('diff.csv', 'w') as outFile:
    for line in filetwo:
        if line not in fileone:
            outFile.write(line)
