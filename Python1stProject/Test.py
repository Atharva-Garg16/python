# # for x in range(50,0,-1):
# #     # if x%6!=0:
# #         print(x,end=",")
# #         # print(x,end=",")
# s="hello"
# print(s.count('l'))
# print("geeksforgeeks".count('e',1,13))
# def fun(lis):
#     eve=[]; odd=[]
#     for x in lis:
#         if x%2==0:
#             eve.append(x)
#         else:
#             odd.append(x)
#     return eve,odd
# li=[1,2,3,4,5,6,7,8,9,10,11]
# even,odd=fun(li)
# print(even)
# print(odd)
# print(len(set(li)))

# print(sum(li)/len(li))
# li=[]
# b=True
# for x in range(1,len(li)):
#     if li[x - 1]>li[x]:
#         b=False
#         break
# if b:
#     print("sorted")
# else:
#     print("not sorted")
# class Employee:
#     compName="gfg"
#     def __init__(self,id):
#         self.id=id
# e=Employee(1001)
# print(Employee.compName)
# print(e.id)
# print(e.compName)
class Animal:
    sound="bho-bho"
    def fun(self):
        print(" m")

lion = Animal()
lion.fun()
print(type(lion))
