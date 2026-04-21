# class complex:
#     def __init__(self, real, imag):
#         self.real = real
#         self.imag = imag
#
#     def display(self):
#         # Using an f-string for cleaner formatting
#         print(f"{self.real} + i{self.imag}")
#
#     def add(self, C):
#         self.real += C.real
#         self.imag += C.imag
#
# # Testing the code
# c1 = complex(10, 20)
# c1.display()
#
# c2 = complex(20, 30)
# c2.display()
# c1.add(c2)
# c1.display()
# for x in range(50000):
#     print(x,end=",")
# s="h e l l o"
# l=s.split(" ")
# l[0]="g"
# print(" ".join(l))
# s="hello"
# print(s.count("l"))
# p=input().split(",")
# m=p[0]
# for x in p:
#     if len(x)<=len(m):
#         m=x
# print(m)
# import math
#
# p=input().split(",")
# l=[]
# s=0; c=0
# for k in p:
#     s+=len(k)
#     c+=1
# avg=s/c
# avg=math.ceil(avg)
# t=0
# for k in p:
#     if avg<len(k):
#         t+=1
# print(t)
# def has_duplicate(L):
#     print(not (len(L) == len(set(L))))
# L = eval(input())
# has_duplicate(L)

import networkx
import matplotlib.pyplot
import networkx as nx

# G=networkx.Graph()
# l=[1,2,3]
# G.add_nodes_from(l)
# G.add_edge(1,2)
# G.add_edge(2,3)
# G.add_edge(3,1)
# G=nx.complete_graph(6)
# print(G.edges())
# nx.draw(G)
# matplotlib.pyplot.show()

