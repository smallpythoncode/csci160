"""Jahnke, Student ID: 0808831
kenny.jahnke@ndus.edu / greensaber77@gmail.com
CSCI 160, Spring 2022, Lecture Sect 02, Lab Sect L03
Program XX, Part X

0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
a b c d e g k l m n  q  r  s  t  w

# if value to the left of the mid, the next high is mid - 1
if value to the right of the mid, the next low is mid + 1

NOTE: if value is not mid, next set will have one value
stay the some and the other change based on mid

find b
0   14  7
0   6   3
1   3   2
# verify

find e
0   14  7
0   6   3
4   6   5
4   4   4

find r
low high    mid
0   14      7
8   14      11
11  11      11
verify?

find q
low high    mid
0   14      7
8   14      11
8   10      9
10  10      10


find o
low high    mid
0   14      7
8   14      11
8   10      9
10  10      10
10  9       XXX
"""


def main():
    pass


if __name__ == "__main__":
    main()

# All work and no play makes Jack a dull boy.
