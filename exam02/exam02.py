import matplotlib.pyplot as plt

import numpy as np

import serial

import time


Fs = 300.0  # sampling rate

 # sampling interval

t = np.arange(0,10,0.1) # time vector; create Fs samples between 0 and 1.0 sec.

b = 0
a = np.arange(0,10,0.1)
datax = np.arange(0,10,0.1)
datay = np.arange(0,10,0.1) # signal vector; create Fs samples
dataz = np.arange(0,10,0.1)
xx = 0
yy = 0
zz = 0
result = np.arange(0,10,0.1)
data = np.arange(0,10,0.1)
u = len(datax)
n = len(datay) # length of the signal
m = len(dataz)
j = np.arange(u)
k = np.arange(n)
l = np.arange(m)
T = n/Fs
cos=np.arange(0,10,0.1)
frq = k/T # a vector of frequencies; two sides frequency range 

frq = frq[range(int(n/2))] # one side frequency range


serdev = '/dev/ttyACM0'

s = serial.Serial(serdev)

for a in range(0, int(Fs)):

    line=s.readline() # Read an echo string from K66F terminated with '\n'

    # print line
    
    if a%3==1:
        datax[xx]=float(line)
        xx=xx+1
    elif a%3==2:
        datay[yy]=float(line)
        yy=yy+1  
    else:
        dataz[zz]=float(line)
        zz=zz+1
for b in range(0, 100):
    cos[b] =float((datax[b]*datax[0])+(datay[b]*datay[0])+(dataz[b]*dataz[0]))/((((datax[b])**2)+((datay[b])**2)+((dataz[b])**2))**(1/2))*((((datax[0])**2)+((datay[0])**2)+((dataz[0])**2))**(1/2))

    if cos[b]<=(1/2)**(1/2):
        result[b]=1
        b=b+1
    else:
        result[b]=0
        b=b+1





# Y = np.fft.fft(y)/n*2 # fft computing and normalization

# Y = Y[range(int(n/2))] # remove the conjugate frequency parts


fig, ax = plt.subplots(2, 1)

ax[0].plot(t,datax,label='x')
ax[0].plot(t,datay,label='y')
ax[0].plot(t,dataz,label='z')

ax[0].set_xlabel('Time')

ax[0].set_ylabel('Acc Vector')
ax[0].legend

ax[1].stem(t,result) # plotting the spectrum

ax[1].set_xlabel('Time')

ax[1].set_ylabel('Tilt')

plt.show()

s.close()