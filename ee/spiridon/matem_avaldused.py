'''
Created on 18. okt 2021

@author: spiridon
'''
1 + 2
print(1 + 2)
one = '4'
two = '26'
print(one + two)
penta = [1, 2, 3, 4, 5]
print(penta)
heksa = [1, 2, 3, 4, 5, 6]
print(heksa + penta)
penta1 = ('a', 'b', 'c', 'd', 'e')
heksa1 = ['f', 'g', 'h', 'i', 'j', 'k']
print(heksa1[3])
# heksa1 toon valja 4. elemendi , kasutan [ ] sulge , lugemine algab alati
# 0-st.
print(penta1[1])
# penta1,toon valja 1.elemendi,kasutan [ ]sulge .
print(2 * 2)
print(2 * '3')
# korrutasin arvu ja sone .
tetra = (2 * '3')
type(tetra)
print(type(tetra))
# kontrollisin ja sain vastuse , et on string tuupi sone.
print(penta * 2)
from inspect import currentframe
# rea tunnuse programmi kaivitamine ,votab teegi .
print(currentframe().f_lineno)
print("\n" + str(currentframe().f_lineno) +
      ": selle reaga kaivitan loend * arv")
# naitab - tekitab rea vahetuse ,+konventeerib arvu soneks ,(valjastab
# viite sellele failile kus oleme ,.f lineno naitab rea tunnust
print(penta * 2)
print(666/999)
print(6/3)
# jagamine , vastuseks murd arv
print(6//3)#2
print(666//999)#0
print(999//666)#1
print(666//333)#2
print(999//33)#30
print(33*30)#990
#tegelesin jagamisega , taisarvu jagamisega ja kontrollisin korrutuse labi .
print("\n" + str(currentframe().f_lineno) +
      ": selle reaga  arv/ arv")
print(666/999)#0,6666666666
