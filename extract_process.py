import pandas as pd
import glob as glob
import numpy as np


path = r''

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
x = data[:,0]
y = data[:,1]
u = data[:,2]
v = data[:,3]

y = y[0:106]*-1


u = np.reshape(u,(T,l))
v = np.reshape(v,(T,l))

U = np.mean(u,axis = 0)
V = np.mean(v,axis = 0)

var = np.mean(u**2,axis = 0)


U_un = np.ones([T,l])
V_un = np.ones([T,l])


for i in range(0,T):
    U_un[i,:] = U

for i in range(0,T):
    V_un[i,:] = V


u_fluc = u - U_un
v_fluc = v - V_un

uu = u_fluc*u_fluc
vv = v_fluc*v_fluc
uv = v_fluc*u_fluc

uu = np.reshape(uu,(T,l))
vv = np.reshape(vv,(T,l))
uv = np.reshape(uv,(T,l))

rey_uu = np.mean(uu,axis = 0)
rey_uv = np.mean(uv,axis = 0)
rey_vv = np.mean(vv,axis = 0)

# x has 188
# y has 106

U = np.reshape(U,(188,106))
V = np.reshape(V,(188,106))
rey_uu = np.reshape(rey_uu,(188,106))
rey_uv = np.reshape(rey_uv,(188,106))
rey_vv = np.reshape(rey_vv,(188,106))


np.savetxt("U.csv", U, delimiter=",")
np.savetxt("V.csv", V, delimiter=",")
np.savetxt("rey_uu.csv", rey_uu, delimiter=",")
np.savetxt("rey_vu.csv", rey_uv, delimiter=",")
np.savetxt("rey_vv.csv", rey_vv, delimiter=",")
np.savetxt("y.csv", y, delimiter=",")
