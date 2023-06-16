import random
import struct
import math

def makexycoord(filename, n=10000):
    fd = open(filename, 'wb')
    for _ in range(n):
        databytes = struct.pack('>ff', random.uniform(0,1), random.uniform(0,1))
        fd.write(databytes)
    fd.close()

def readxycoord(filename):
    data = []
    try:
        fd = open(filename, 'rb')
        datalength = struct.calcsize('>ff')
        while True:
            datum = fd.read(datalength)
            if len(datum) != datalength:
                break
            data.append(struct.unpack('>ff', datum))
        fd.close()
    except FileNotFoundError:
        print('File Not Found')
    return data

def getlength(xy):
    return math.sqrt(xy[0]**2 + xy[1]**2)

if __name__ == '__main__':
    makexycoord('xycoord.tmp', 100)
    data = readxycoord('xycoord.tmp')
    print(data[0], data[1])