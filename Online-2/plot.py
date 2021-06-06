import matplotlib.pyplot as plt
import LagrangeMethod as LM
import numpy as np
v1 = [22, 25, 27, 30]
v2 = [30, 31, 35, 37]
p1 = [44, 43, 42, 40]
p2 = [40, 35, 30, 25]

V1 = np.arange(22,30.5,.5)
P1 = []
for i in range(0, len(V1)):
    P1.append(LM.lagrangeMethod(V1[i], 3, v1, p1 ))

plt.plot(V1, P1)

V2 = np.arange(30,35,.5)
P2 = []
for i in range(0, len(V2)):
    P2.append(LM.lagrangeMethod(V2[i], 3, v2, p2 ))

plt.plot(V2, P2)


