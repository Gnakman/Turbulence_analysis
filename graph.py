import numpy as np
import matplotlib.pyplot as py

U = np.loadtxt('U.csv', delimiter=',')
V = np.loadtxt('V.csv', delimiter=',')
rey_uu= np.loadtxt('rey_uu.csv', delimiter=',')
rey_vu = np.loadtxt('rey_vu.csv', delimiter=',')
rey_vv = np.loadtxt('rey_vv.csv', delimiter=',')
y = np.loadtxt('y.csv', delimiter=',')

U_avg = np.mean(U,axis=0)
#U_avg_5=(U[1,:]+U[50,:]+U[150,:]+U[100,:]+U[180,:])/5
rey_vu_avg = np.mean(rey_vu,axis=0)
rey_vv_avg = np.mean(rey_vv,axis=0)
rey_uu_avg = np.mean(rey_uu,axis=0)


fig, ax = py.subplots()
ax.plot(U_avg[4:106],y[4:106])

ax.set(xlabel='Streamwise Velocity', ylabel='y)',
       title='Time and Spatial Averaged')


fig.savefig("time_n_space.png")
py.show()
"""
fig, axs = py.subplots(3, 2)
axs[0, 0].plot(rey_uu[1,4:106],y[4:106],'tab:blue')
axs[0, 0].set_title('X = 1/5')
axs[0, 1].plot(rey_uu[50,4:106],y[4:106], 'tab:orange')
axs[0, 1].set_title('X = 2/5')
axs[1, 0].plot(rey_uu[100,4:106],y[4:106], 'tab:green')
axs[1, 0].set_title('X = 3/5')
axs[1, 1].plot(rey_uu[150,4:106],y[4:106], 'tab:red')
axs[1, 1].set_title('X = 4/5')
axs[2, 0].plot(rey_uu[180,4:106],y[4:106], 'tab:grey')
axs[2, 0].set_title('X = 5/5')
axs[2, 1].plot(rey_uu_avg[4:106],y[4:106])
axs[2, 1].set_title('Average')

for ax in axs.flat:
    ax.set(xlabel='Reynolds Stress uu', ylabel='y')
for ax in fig.get_axes():
    ax.label_outer()
for ax in axs.flat:
    ax.label_outer()
py.show()
"""
#py.plot(rey_uu[1,3:106],y[3:106])
#py.plot(rey_uu[187,4:106],y[4:106])
#py.plot(rey_uu[50,4:106],y[4:106])
#py.plot(rey_uu[100,4:106],y[4:106])
#py.plot(rey_uu[150,4:106],y[4:106])
#py.show()

#py.plot(rey_vu[1,4:106],y[4:106])
#py.show()

#py.plot(rey_vv[1,4:106],y[4:106])
#py.show()



#py.plot(V[1,4:106],y[4:106])
#py.show()

