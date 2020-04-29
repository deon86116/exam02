import matplotlib.pyplot as plt

import numpy as np

import serial

import time


Fs = 100.0  # sampling rate
distance=0
 # sampling interval

t = np.arange(0,10,0.1) # time vector; create Fs samples between 0 and 1.0 sec.

b = 0
a = np.arange(0,10,0.1)
datax = np.arange(0,10,0.1)
datay = np.arange(0,10,0.1) # signal vector; create Fs samples
dataz = np.arange(0,10,0.1)
xx = 0
yy = 0
hh = 0
result = np.arange(0,10,0.1)
data = np.arange(0,10,0.1)
u = len(datax)
n = len(datay) # length of the signal
m = len(dataz)
j = np.arange(u)
k = np.arange(n)
l = np.arange(m)
T = n/Fs
totalvecx=0
totalvecy=0
lildistance=np.arange(0,10,0.1)
frq = k/T # a vector of frequencies; two sides frequency range 

frq = frq[range(int(n/2))] # one side frequency range


serdev = '/dev/ttyACM0'

s = serial.Serial(serdev)

for a in range(0, 200):

    line=s.readline() # Read an echo string from K66F terminated with '\n'

    # print line
    
    if a%2==1:
        datax[xx]=float(line)
        xx=xx+1
    elif a%2==0:
        datay[yy]=float(line)
        yy=yy+1  
for b in range(0, 100):
    totalvecx=totalvecx+((1/2)*(9.8)*(datax[b])*(0.1)*(0.1))
    totalvecy=totalvecy+((1/2)*(9.8)*(datay[b])*(0.1)*(0.1))
    lildistance[b] =float(((((totalvecx)**(2))+((totalvecy)**(2)))**(1/2)))
    if (lildistance[b]-lildistance[0])>=0.05:
        result[b]=1
        b=b+1
    else:
        result[b]=0
        b=b+1





# Y = np.fft.fft(y)/n*2 # fft computing and normalization

# Y = Y[range(int(n/2))] # remove the conjugate frequency parts


fig, ax = plt.subplots(2, 1)

ax[0].plot(t,dataz,label='z')

ax[0].set_xlabel('Time')

ax[0].set_ylabel('Z Acc Vector')
ax[0].legend

ax[1].stem(t,result) # plotting the spectrum

ax[1].set_xlabel('Time')

ax[1].set_ylabel('Displacement')

plt.show()

s.close()