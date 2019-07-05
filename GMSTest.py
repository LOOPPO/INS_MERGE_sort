from mergeSort import mergeSort
from randomizeVector import randomize
import signal
from time import time
A=[]
n=int(input("Hey,how much numebers? "))
randomize(A,n)
print("generic case ~ best case ~ worst case")
print("sorting...")
signal.alarm(120)
t0=time()
mergeSort(A)
t1=time()
print("this case takes %f seconds" % (t1 - t0))
print(A)
print("done!")
