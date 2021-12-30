
import numpy as np
import matplotlib.pyplot as plt
cos = np.cos
sin = np.sin
pi = np.pi


n = 45  # you choose  , how many cycles
Upeak = 12  # you choose, voltage peak
phi_u = 0.4  # you choose, voltage phase
phi_i = 0.3  # you choose, current phase
Ipeak = 0.4  # you choose, current peak


Fs = 10000  # sample rate
x = np.arange(n)
t = n*x/Fs
y = Upeak*sin((100*pi*t)+phi_u)  # voltage eq
current = Ipeak*sin((100*pi*t)+phi_i)  # current eq
average_power = (0.5*(Upeak*Ipeak)*cos(phi_u-phi_i))  # av power
av = []  # array just to live with the plt bull§h
for g in range(1, n):
    av.append(average_power)  # I^
momentry_power = y*current  # mom power
fig, axs = plt.subplots(2)
# title to say the ave power
fig.suptitle(f"Average power is {average_power:.3f}W")
axs[0].plot(x, y, label='voltage', color='b')
# votlage and current 1st subplot
axs[0].plot(x, current, label='current', color="red")
axs[1].plot(av, label='average power', color='g')
axs[1].plot(momentry_power, label='momentary power',
            color='orange')  # ave and mom power 2nd subplpt
axs[0].legend()
axs[1].legend()

axs[0].set_ylabel('voltage (V), current(A)')
axs[1].set_ylabel('Power (W)')
fig.text(0.5, 0.04, 'Sample(n)', ha='center',
         va='center')  # common x axis title
plt.show()
