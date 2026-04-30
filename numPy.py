import numpy as np
        #1D Array
arr=np.array(['Hello', 'Hi','Yes'])
for word in arr:
   if 'e' in word:
      print(word)
        #2D Array
arr1=np.array([['Hello', 'Hi','Yes'],['How are you?', 'hello', 'No']])
query=input()
length=len(arr1[0])
for row in range(length):
   if query==arr1[0][row]:
      print(arr1[1][row])

        #3D Array
arr2=np.array([[[2,1,3],[3,2,1]],[[4,5,6],[1,3,2]]])
print(arr2)