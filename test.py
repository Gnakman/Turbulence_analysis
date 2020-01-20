import pandas as pd
import glob as glob
import numpy as np


path = r'C:\Users\Nam\Desktop\ANAL_TURB\Data_for_Dr_Balachandar\Data_for_Dr_Balachandar'

all_files = glob.glob(path + "/*.txt")
li=[]

for filenames in all_files:
    df = pd.read_csv(filenames, skiprows = (3), header = None)
    li.append(df)

frame = pd.concat(li, axis=0 )


data1 = pd.read_csv('WOFT_II_135mm___0001.txt',skiprows =(3),header=None)
l = len(data1) 
T = len(all_files) 

data= frame.to_numpy()
u = data[:,2]
v = data[:,3]

u = np.reshape(u,(l,T))
v = np.reshape(v,(l,T))

U = u.sum(axis = 1)/T
V = v.sum(axis = 1)/T

U_un = np.ones([l,T])
V_un = np.ones([l,T])

for i in range(0,500):
    U_un[:,i] = U

for i in range(0,500):
    V_un[:,i] = V

u_fluc = u - U_un
v_fluc = v - V_un

uu = u_fluc*u_fluc
vv = v_fluc*v_fluc
uv = v_fluc*u_fluc

uu = np.reshape(uu,(l,T))
vv = np.reshape(vv,(l,T))
uv = np.reshape(uv,(l,T))

rey_uu = uu.sum(axis = 1)/T
rey_uv = uv.sum(axis = 1)/T
rey_vv = vv.sum(axis = 1)/T











