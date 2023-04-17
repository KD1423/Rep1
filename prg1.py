import numpy as np

file1=open('data1lenghts.txt','r')
lenghts=file1.readlines()
print(lenghts)

file2=open('data2angles.txt','r')
angles=file2.readlines()
print(angles)

a1=float(lenghts[0])
a2=float(lenghts[1])
a3=float(lenghts[2])
T1=float(angles[0])
T2=float(angles[1])
d3=3

r01=[[np.cos(T1),0,np.sin(T1)],[np.sin(T1),0,-np.cos(T1)],[0,1,0]]

r12=[[-np.sin(T2),0,np.cos(T2)],[np.cos(T2),0,np.sin(T2)],[0,1,0]]

r23=[[1,0,0],[0,1,0],[0,0,1]] 

r03=np.dot(r01,r12)

#displacement vectors
d01=[[0],[0],[a1]]
d12=[[0],[0],[0]]
d23=[[0],[0],[a2+a3+d3]]

#HMT
h01=np.concatenate((r01,d01),1)
h01=np.concatenate((h01,[[0,0,0,1]]),0)

h12=np.concatenate((r12,d12),1)
h12=np.concatenate((h12,[[0,0,0,1]]),0)

h23=np.concatenate((r23,d23),1)
h23=np.concatenate((h23,[[0,0,0,1]]),0)

h02=np.dot(h01,h12)

h03=np.dot(h02,h23)

print(h03)