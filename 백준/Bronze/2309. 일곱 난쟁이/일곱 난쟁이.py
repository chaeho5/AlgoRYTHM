import sys
from array import array
input = sys.stdin.readline

arr = array('i', [])

for i in range(9):
   arr.append(int(input()))


nanjangE = sum(arr)

found = False
jjob = []

for i in range(9):
   for j in range(i + 1, 9):
      if nanjangE - arr[i] - arr[j] == 100:
         jjob = [arr[i], arr[j]]
         found = True
         break
      if found:
         break
      
arr.remove(jjob[0])
arr.remove(jjob[1])

sorted_arr = array(arr.typecode, sorted(arr))

for nanjang in sorted_arr:
    print(nanjang)