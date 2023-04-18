import numpy as np

file1=open('data1lenghts.txt','r')
lenghts=file1.readlines()

file2=open('data2angles.txt','r')
angles=file2.readlines()

a1=float(lenghts[0])
a2=float(lenghts[1])
a3=float(lenghts[2])
T1deg=float(angles[0])
T2deg=float(angles[1])
d3=3

T1=(T1deg/180)*np.pi
T2=(T2deg/180)*np.pi

table=[[T1,(1/2)*np.pi,0,a1],[T2+(1/2)*np.pi,(1/2)*np.pi,0,0],[0,0,0,a2+a3+d3]]

i=0
H01 = [[np.cos(table[i][0]),-np.sin(table[i][0])*np.cos(table[i][1]),np.sin(table[i][0])*np.sin(table[i][1]),table[i][2]*np.cos(table[i][0])],
       [np.sin(table[i][0]),np.cos(table[i][0])*np.cos(table[i][1]),-np.cos(table[i][0])*np.sin(table[i][1]),table[i][2]*np.sin(table[i][0])],
       [0,np.sin(table[i][1]),np.cos(table[i][1]),table[i][3]],[0,0,0,1]]

i=1
H12 = [[np.cos(table[i][0]),-np.sin(table[i][0])*np.cos(table[i][1]),np.sin(table[i][0])*np.sin(table[i][1]),table[i][2]*np.cos(table[i][0])],
       [np.sin(table[i][0]),np.cos(table[i][0])*np.cos(table[i][1]),-np.cos(table[i][0])*np.sin(table[i][1]),table[i][2]*np.sin(table[i][0])],
       [0,np.sin(table[i][1]),np.cos(table[i][1]),table[i][3]],[0,0,0,1]]

i=2
H23 = [[np.cos(table[i][0]),-np.sin(table[i][0])*np.cos(table[i][1]),np.sin(table[i][0])*np.sin(table[i][1]),table[i][2]*np.cos(table[i][0])],
       [np.sin(table[i][0]),np.cos(table[i][0])*np.cos(table[i][1]),-np.cos(table[i][0])*np.sin(table[i][1]),table[i][2]*np.sin(table[i][0])],
       [0,np.sin(table[i][1]),np.cos(table[i][1]),table[i][3]],[0,0,0,1]]

H02= np.dot(H01,H12)
H03= np.dot(H02,H23)

print("The final matrix representing rotation and displacement vectors of end effector wrt frame 0 is :")
print(" ")
print(H03)

