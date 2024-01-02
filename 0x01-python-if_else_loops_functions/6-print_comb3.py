#!/usr/bin/python3
print(", ".join("{:02d}{:02d}".format(i,j) for i in range(10) for j in range(i+1, 10)))
