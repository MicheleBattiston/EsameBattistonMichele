#!/usr/bin/python3.4

def openFile():
    with open('data.txt', 'r') as f:
        return f.readlines()

def getData(x):
    for line in x:
        i = line.split(';')
        print i[0].strip() + "\t" + i[1].strip() + "\t" + i[2].strip() + "\t" + i[3].strip()

if __name__ == "__main__":
    x = openFile()
    getData(x)
    # closeFile(x)
 
