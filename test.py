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
xo.name.first = "yooooooooo"
xo.show()
xo.fullname @= lambda x: print(xo.nice(x))
xo.name.first = " awesome"
xo.show()
print("FULL NAME IS ",xo.fullname())
print("FULL NAME IS ",xo.fullname)
print(str(xo.fullname))
print("____________________________")
xo.name.first = " final "
# print("FULL NAME IS ",xo.fullname)
xo.show()
print(xo.name.first +"!!!"+xo.name.last+"@@"+xo.name)
exit(0)
print()
print()
xo.show()
print(xo.fullname._subscribers)


pass