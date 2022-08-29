# from cmath import exp
# import expando
# xo = expando.Expando()

from operator import ge
# from expando import *
# import expando
import xo
xo = xo.xo

# import re
# given = '''xo.fullname <<= lambda : +xo.name.a.b.c.first._val._cal + ", " +  xo.name.last'''
# def getAllObjects(given):
#     given = given.split('<<=')[-1]
#     regex = re.compile(r'(?P<xo>xo(\.\w+)*)')
#     # regex = re.compile(r'(?P<name>xo.name\.[a-zA-Z]+)')
#     # regex = re.compile(r'\\w+(?:\\.\\w+)+')
#     def removeHiddenAtEnd(s):
#         end = s.split('.')[-1]
#         if not end.startswith('_'):
#             return s
#         else:
#             return removeHiddenAtEnd('.'.join(s.split('.')[:-1]))
    
#     return [ removeHiddenAtEnd(x[0].lstrip("xo.")) for x in re.findall(regex, given) ]


# getAllObjects(given)
# output = ["xo.name.first", "xo.name.last"]
# Regex should match output
# regex = re.compile(r'(?P<name>xo.name\.[a-zA-Z]+)')
# re.findall(regex, given)


# # Regex to return all of the paths like this: x.y.z.a.b.c
# import re
# regex = re.compile(r'([a-zA-Z0-9_]+\.)*[a-zA-Z0-9_]+')
# print(regex.findall(input))

# re.findall(r'(?<=\.)\w+', input)
# re.findall(r'path\.[a-zA-Z0-9_\.]*', input)
# xo = expando.Expando()
xo.name.first = "tami"
xo.name.last.nickname = "d. po"
xo.name.last = "bar"
# print(xo.name.last() is None)
# print(xo.a.b.c() is None)
# xo.a.b.c = True
# print(xo.a.b.c == True)
xo.fullname @= xo.nice
xo.nice = lambda x : print(" @ @ @ @ @ @ NICE!!!!! "+str(x))
xo.fullname = "cool"
xo.show()
print("____________________________")
xo.fullname <<= lambda: f"{xo.name.first} {xo.name.last.nickname} {xo.name.last}"
print("____________________________")
print("____________________________")
xo.show()
xo.name.first = "!"
xo.name.last.nickname = "!!"
xo.name.last = "!!!"
xo.show()
exit(1)
xo.show()
print("____________________________")
xo.fullname = "cool"
exit(0)
# xo.fullname = "???????"


# print()
# print("@@@@@",xo.GetXO("name.first"))


# xo.formula @= xo.nice
print()
# xo.show()

# xo.fullname = "cool"
# xo.fullname @= lambda x: xo.nice(x)
# TODO:

xo.name.first = "yooooooooo"
xo.show()
xo.name.first = " awesome"
print(" ::: FULL NAME ",xo.fullname())
xo.show()
print("FULL NAME IS ",xo.fullname())
print("FULL NAME IS ",xo.fullname)
print(str(xo.fullname))
xo.name.first = " final "
# print("FULL NAME IS ",xo.fullname)
xo.show()
print(xo.name.first +"!!!"+xo.name.last+"@@"+xo.name)
print()
print()
xo.show()
print(xo.fullname._subscribers)


pass