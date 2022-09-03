#! /usr/bin/env python3


import classes_prob3



print("TESTING A SIMPLE 3x5 GRID.  DO ALL OF THE LINKS POINT AS I EXPECT?")
print()



print("Calling build_grid(3,5)...")
sw_corner = classes_prob3.build_grid(3,5)
print()

print("Extracting all of the rooms into 15 different variables.  If any of these fail because of a None pointer, then it means that your grid is too small.")
print()

rm00 = sw_corner
rm01 = sw_corner.n
rm02 = sw_corner.n.n
rm03 = sw_corner.n.n.n
rm04 = sw_corner.n.n.n.n

rm10 = rm00.e
rm11 = rm01.e
rm12 = rm02.e
rm13 = rm03.e
rm14 = rm04.e

rm20 = rm10.e
rm21 = rm11.e
rm22 = rm12.e
rm23 = rm13.e
rm24 = rm14.e



print("Checking to make sure that all of the edge links are None.  These use assert statements ... so any failure here will be repored as an AssertionError; if you see that, then you should figure out which line failed, and look into that issue.")
print()

# west edge
assert rm00.w is None
assert rm01.w is None
assert rm02.w is None
assert rm03.w is None
assert rm04.w is None

# east edge
assert rm20.e is None
assert rm21.e is None
assert rm22.e is None
assert rm23.e is None
assert rm24.e is None

# north edge
assert rm04.n is None
assert rm14.n is None
assert rm24.n is None

# south edge
assert rm00.s is None
assert rm10.s is None
assert rm20.s is None



print("Checking the *internal* links, to ensure that they are all correct.  Just like the previous test, this uses assertions.")
print()

# all east-facing links, starting with first column
assert rm00.e is rm10
assert rm01.e is rm11
assert rm02.e is rm12
assert rm03.e is rm13
assert rm04.e is rm14

assert rm10.e is rm20
assert rm11.e is rm21
assert rm12.e is rm22
assert rm13.e is rm23
assert rm14.e is rm24

# all west-facing links, starting witht the first column.
assert rm10.w is rm00
assert rm11.w is rm01
assert rm12.w is rm02
assert rm13.w is rm03
assert rm14.w is rm04

assert rm20.w is rm10
assert rm21.w is rm11
assert rm22.w is rm12
assert rm23.w is rm13
assert rm24.w is rm14

# all north-facing links, starting with the bottom row
assert rm00.n is rm01
assert rm01.n is rm02
assert rm02.n is rm03
assert rm03.n is rm04

assert rm10.n is rm11
assert rm11.n is rm12
assert rm12.n is rm13
assert rm13.n is rm14

assert rm20.n is rm21
assert rm21.n is rm22
assert rm22.n is rm23
assert rm23.n is rm24

# all south-facing links, starting with the bottom row
assert rm01.s is rm00
assert rm02.s is rm01
assert rm03.s is rm02
assert rm04.s is rm03

assert rm11.s is rm10
assert rm12.s is rm11
assert rm13.s is rm12
assert rm14.s is rm13

assert rm21.s is rm20
assert rm22.s is rm21
assert rm23.s is rm22
assert rm24.s is rm23



print("No errors detectedd.")
print()

print("TESTCASE COMPLETED")

