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