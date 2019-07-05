from insertionSort import insertionSort
from randomizeVector import randomize
from time import time
import signal
A=[]
n=int(input("Hey,how much numebers? "))
randomize(A,n)
print("generic case...")
print("sorting...")
signal.alarm(120)
t0=time()
insertionSort(A)
t1=time()
print("this case takes %f seconds" % (t1 - t0))
print(A)
print("done!")


