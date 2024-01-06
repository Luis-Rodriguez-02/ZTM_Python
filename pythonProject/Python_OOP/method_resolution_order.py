# MRO - Method Resolution Order

class A:
  num = 10

class B(A):
  pass

class C(A):
  num = 1

class D(B, C):
  pass




print(D.num)  #  Method MRO - What is first in line D -> B -> C -> A
print(D.mro()) # tells the order

print(A.num)





# 
#        A
#      /   /
#     /      /
#    B       C
#     \     /
#      \  / 
#        D
# 

