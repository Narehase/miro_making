import numpy as np
import matplotlib.pyplot as plt
import cv2

import numba
k = np.random.randn(4,4,3)

@numba.jit  
def trejer(mas):
    na = np.zeros((mas.shape[0]*2-1,mas.shape[1]*2-1))
    for i in range(len(mas)):
        for j in range(len(mas[0])):
            na[i*2, j*2] = mas[i, j]
    return na

# @numba.jit
def loads(maps, mos, st = (0,0), runs = 1):
    run = st
    we = st
    l = True
    ios = 0
    asas = []
    # qe = (0, 0)
    # for isss in range(runs):
    isss = 0
    while True:
        if np.max(maps) == 0:
            break
        isss+= 1
        if isss % 200 == 0:
            if isss % 800 == 0:
                print(isss)
                print("**",len(asas))
            asia = cv2.resize(mos, (800,800))
            cv2.imshow("aa", asia)
            cv2.waitKey(2)
        l2c = False
        a = [[np.array([st[0]+2,st[1]]), np.array([st[0]+1,st[1]])], [np.array([st[0],st[1]+2]), np.array([st[0],st[1]+1])], [np.array([st[0]-2,st[1]]), np.array([st[0]-1,st[1]])], [np.array([st[0],st[1]-2]), np.array([st[0],st[1]-1])]]
        p = 1
        lc = 0
        pizza = []
        for ip in a:
            i = ip[0]
            w = ip[1]
            # print(i)
            ass = 0
            # print(len(mos))
            # print(i, "**")
            # print(np.min(i < len(mos)), "##")
            if np.min(i >= 0) and  np.min(i < len(mos)):
                ass = maps[i[0], i[1]]
                pizza.append(ass)
                n = np.random.rand(1)
                if n < 0.006 and len(asas) > 4 or (len(pizza) == 4 and np.max(pizza) == 0):
                # if (len(pizza) >= 4 and np.max(pizza) == 0):
                    # print(np.max(pizza))
                    if len(asas) > 0:
                        ps = np.random.randint(0, len(asas))
                        st = asas[ps]
                        del asas[ps]
                        l2c = True
                    break
                
                if abs(ass - lc) < p and ass > 0:
                    l = False
                    # print(w, "**")
                    we = [w[0],w[1]]
                    qe = [i[0],i[1]]
                    p = abs(ass - lc)
                    run = i
        pizza.clear()
        if l2c:
            continue
        if l:
            ios+=1
            l = True
            af = st
        else:
            mos[we[0],we[1]] = 1
            mos[qe[0], qe[1]] = 1
            maps[qe[0],qe[1]] = 0
            maps[we[0],we[1]] = 0
        if ios == 5:
            break
        st = qe
        asas.append(st)
    return mos, maps

def miros(size = (100,100), s = (0,0), run = 30000):
    global k
    news = [int((size[0]/2)), int((size[1]/2))]
    # monarija = np.ones((news[0],news[1]))
    monarija = np.random.rand(news[0],news[1])
    # monarija[10:-10, 10:-10]*=(monarija[10:-10, 10:-10]>0.3)
    # monarija[20:-20, 20:-20] = np.random.rand(monarija[20:-20, 20:-20].shape[0], monarija[20:-20, 20:-20].shape[1])
    # print(f[:,:,0].shape)
    # plt.figure(4)
    # plt.imshow(np.abs(monarija[:,:,0]))
    # monarija = 1/np.abs(monarija[:,:,0])
    # print(np.max(monarija))

    # monarijaz -= monarija*(np.round(monarija,1) ==  0.5)
    monarija = trejer(monarija)
    # monarija = trejer(monarija)
    print(monarija.shape)
    mas = np.zeros(monarija.shape)

    a, _ = loads(monarija, mas.copy(), s, runs= run)
    
    # mas[1:-1,1:-1] = a
    # mas[0,1] = 1
    # mas[-1,-2] = 1.1
    # mas[-1:-3,-2] = 1
    return a

# mas = np.zeros([201,201])

# s = [0,1]
# s = [11,10]

# mozaik = np.random.rand(100,100)
# mozaik = trejer(mozaik)z``

# plt.figure(1)
# plt.imshow(mozaik.copy())

# maps = np.ones([len(mozaik)+2,len(mozaik[0])+2])
# mos = np.zeros(mozaik.shape)
# a, _ = loads(mozaik, mos.copy(), (0,0), runs= 30000)

# mas[1:-1,1:-1] = a
# mas[0,1] = 1
# mas[-1,-2] = 1.1
# mas[-1:-3,-2] = 1
mas = miros((500,500),(0, 0), 150000)
plt.figure(4)
plt.imshow(mas)
# cv2.imwrite("miro.png",mas*255)
plt.show()
