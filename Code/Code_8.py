import random 
import matplotlib.pyplot as plt

#Simulation
# 0 for red socks, 1 for green socks, 2 for blue socks
X=[0,0,0,1,1,1,1,2,2,2]
c=0
for i in range(1000):
    a=random.choice(X)
    b=random.choice(X)
    if a==b:
        c=c+1

prob=c/1000
print("Experimental probabity is :",prob)
print('Theortical result is : 0.278')


