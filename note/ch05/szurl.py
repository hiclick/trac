# -*- coding:utf-8 -*-
__author__ = 'Christen'

with open("url.txt") as f:
    out = open("results.txt", "w")
    for line in f:
        out.write("'" + line.rstrip("\n\r") + "',\n")
    out.close()


def delblankline(infile, outfile):
    infp = open(infile, "r")
    outfp = open(outfile, "w")
    lines = infp.readlines()
    for li in lines:
        if li.split():
            outfp.writelines(li)
    infp.close()
    outfp.close()


# if __name__ == "__main__":
    # delblankline("urls.txt", "url.txt")
