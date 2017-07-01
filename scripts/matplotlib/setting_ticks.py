#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Kushal Keshavamurthy Raviprakash
"""

import numpy as np
import  matplotlib.pyplot sa plt

x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
S, C = np.sin(x), np.cos(x)

plt.figure(figsize=(10, 6), dpi=80)

plt.plot(x, C, color="blue", linewidth=2.5, linestyle="-")
plt.plot(x, S, color="red", linewidth=2.5, linestyle="-")

plt.xlim(x.min()*1.1, x.max()*1.1)
plt.ylim(C.min()*1.1, C.max()*1.1)

plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
plt.yticks([-1, 0, +1])
plt.show()
