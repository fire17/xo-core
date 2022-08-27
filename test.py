# from cmath import exp
# import expando
# xo = expando.Expando()

from expando import *

xo.name.first = "tami"
xo.name.last = "bar"
xo.fullname = "???????"


# print()
# print("@@@@@",xo.GetXO("name.first"))


xo.nice = lambda x : " @ @ @ @ @ @ NICE!!!!!"+str(x)
# xo.show()
# xo.formula @= xo.nice
print()
# xo.show()

xo.fullname = "cool"
xo.fullname <<= lambda : xo.name.first + ", " +  xo.name.last
print(" ::: FULL NAME ",xo.fullname())
xo.fullname @= lambda x: print(xo.nice(x))
xo.name.first = "yooooooooo"
xo.show()
exit(0)
print("____________________________")
xo.fullname()
print()
print("FULL NAME IS ",xo.fullname())
print()
xo.show()
print(xo.fullname._subscribers)


pass