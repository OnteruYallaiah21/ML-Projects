"""
*numpy is  defined as numarical python
*numpy is open source library that is widely used in the science and engineering
*numpy arry contains the multidimensiona arry dataa structure
*such as n dimensional ndaary
*fundamental arry is called ndarry,it represents  n dimensional arry
*all elemnts in a array is must be same data type
*one array is created total size of array can`t change
*the array is mutable
*two and highr dimensional array can be intilalized from nested python
*in numpy the dimensio some tiimes referred as axis 
*this terminology may be use ful in to distguish between the dimensionality of an aray
*for instance arry could reprsent in threee points each laying within a four dimentional space but a has only two axis
*another defference is between the arry and list of list i that element of the arry can be accesed by squrae brackets saparated by commans 

"""
import numpy as np
a1=np.array([2,3,4,5,6,6])
print(f"accsing aary is =>{a1}")
print(f"the accsing the specifi elemyt isn arrya=>{a1[0]}")
print(f"accsing elemts with slice notationb=>{a1[:3]}")
print(f"accsing the right side numbers in arry=>{a1[3:]}")
a2dime=np.array([[3,4,5,6],[56,56,43,56],[98,78,67,56]])
print(f"how to access the element in two dimensional array=>{a2dime[2,3]}")
#********Basic Attritubutes ***********
#0 dimensional array can be sonsderes as scaler
#1 dimensional array as vector
#2-d array canm be considered as matrix
#IF THE DIMESION OI an array is more then 2 then that can be considered as tensor
#tensor is fundamental data structure if a pytorch
#Array attritubves(ndim,shape,size,dtype)
#the number of dimesional of aarry is stored in ndime
print(f"the dimesionality of any arry is=> {a2dime.ndim}")
print(f"the shape of the rray is=> {a2dime.shape}")
print(f"the size of array is number of elemnts in array=>{a2dime.size}")
print(f"the data type of an arry is=> {a2dime.dtype}")
#**************Creation Of Basic Array***********
#np.zeros(),np.ones(),np.empty(),np.arrange(),np.linspace()
azeros=np.zeros(5)
print(f"azeros=np.zeros(5) is meaning=>{azeros}")
aones=np.ones(6)
print(f"aones=np.ones(6)is maening create an arry with ones{aones}")
arrange=np.arange(4)
print(f"arrange=np.arange(4) this array create the range of elemnts up to 4=>{arrange}")
arrange1=np.arange(2,9,1)
print(f"arrange1=np.arange(2,9,1)this type syntax create the range of elements from the lower limit to upper limit with step size=>{arrange1}")
#and also we can explicitly mention the data type of 
a2data=np.ones(2,dtype=np.int64)
print(f"we can set up the data type of a any thing explicitly ")
# Adding,Removing, and sorting elemts
a3=np.array([2,7,865,65,67657,547657,3653645])
a3sort=np.sort(a3)
print(f"the printinmg the elements can be done by np.sort(arrayreference=>{a3sort})")
a31=np.array([435,55,35,5463,45654365524,5636])
a32=np.array([435252,5435432,525,4354325,31254326,4535432])
a3Concatenate=np.concatenate((a31,a32))
print(f"the two array is {a31,a32}")
print(f"thje concateenate of two marry results is =>{a3Concatenate}")
#4 ndarry.ndim,ndarray.size(),ndarray.shepe
a4=np.array([[[1,2,3,4],
              [7,5,4,3]],
             [[947,53,3,2],
              [43,5,3,4]],
             [[3,434,453,34],
              [3,4535,2,543]]])
print(f"the array is =>{a4}")
print(f"the dimension of ayya is =>{a4.ndim}")
print(f"the size of the arry is =>{a4.size}")
print(f"the shape of the arry is =>{a4.shape}")
#a5 Reshaping the array a5.reshape()
a5=np.arange(6)
print(a5)
a5reshape=a5.reshape(2,3)
print(f"printh the reshaping the array{a5reshape}")
#a6Coversion 1 d array to 2 d array
#np.newaxis,np.expand_dims
a6=np.arange(6)
print(f"printthe array=>{a6},{a6.shape}")
#we can explisitlu converting the array in to row vector or column vector
a6Axis=a6[np.newaxis,:]
print(f"a6Axis=a6[np.newaxis,: as =>{a6Axis}]")
a6axisCol=a6[:,np.newaxis]
print(f"the a6axisCol=a6[:,np.axis] is =>{a6axisCol}")
#aIndex here we are going to learn about indexing and slicing techniquies
aIndex1=np.array([1,2,3,44,5])
print(f"the indexing example array is =>{aIndex1}")
print(f"here we are pring the array with slicing technque=>{aIndex1[0:1],aIndex1[0:2],aIndex1[2:4]}")
print(f"pring the array with slicing technique=>{aIndex1[1:],aIndex1[:3]}")
#here we are going to discuss some importanmat topics about the numpy with some conditions
aIndex2=np.array([[2,344,5,6,7],[443,554325,656,453,565],[546,645654,6453,4365,43654]])
#some arthamatics and soem other lofical functions in array
a_SevenUp=aIndex2[aIndex2>7]
a_SevenGreaterTheN=aIndex2[aIndex2>=7]
a_divisabl_two=aIndex2[aIndex2%2==0]

print(f"the array Indexing Techniquesis  a_SevenUp=>{a_SevenUp}\na_SevenGreaterTheN=>{a_SevenGreaterTheN}\n a_divisabl_two=>{a_divisabl_two}")



