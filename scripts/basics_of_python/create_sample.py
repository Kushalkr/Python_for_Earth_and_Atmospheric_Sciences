import numpy as np

b=0.2
theta = np.linspace(0,4.5*np.pi, 100)
x = np.cos(theta)*np.exp(b*theta)
y = np.sin(theta)*np.exp(b*theta)
outstr = ['\n']*len(theta)
for i in range(len(theta)):
    outstr[i] = str(x[i]) + ',' + str(y[i]) + outstr[i]
print(outstr)
f = open('data/sample.txt','w')
f.writelines(outstr)
f.close()
