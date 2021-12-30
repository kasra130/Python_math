import cheby
import numpy as np
cos=np.cos
pi=np.pi
c = cheby.Cheby.fit(cos, -1, 1, 4)
print(c)
