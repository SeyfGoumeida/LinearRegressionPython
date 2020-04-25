import pandas as pd
import numpy as np
data = pd.read_csv('C:\\\\Users\\cars.csv')
data = (data - data.mean()) / data.std()


def h(x, p0, p1):
    return p0+p1*x


def J(data, p0, p1):
    n = data['dist'].count()
    x = data['speed']
    y = data['dist']
    try:
        return (1/(2*n))*sum((h(x, p0, p1)-y)**2)
    except:
        print('m=n=0')


def CalcP0(data, p0, p1, alpha):
    n = data['dist'].count()
    m = data['speed'].count()
    x = data['speed']
    y = data['dist']
    try:
        return p0-(alpha*(1/m)*sum(h(x, p0, p1)-y))
    except:
        print('m=n=0')


def CalcP1(data, p0, p1, alpha):
    n = data['dist'].count()
    m = data['speed'].count()
    x = data['speed']
    y = data['dist']
    try:
        return p1-(alpha*(1/m)*sum((h(x, p0, p1)-y)*x))
    except:
        print('m=n=0')


i = 0
p0 = p1 = 0
err2 = 0
err1 = -1
eps = 0.01
while i <= 60 or abs(err2-err1) > eps:
    p0_temp = p0
    p0 = CalcP0(data, p0, p1, 0.01)
    p1 = CalcP1(data, p0_temp, p1, 0.01)
    err1 = err2
    err2 = J(data, p0, p1)
    print('Iteration numero : ', i, ' P0 =',
          p0, 'et  P1=', p1, ' Erreur =', err2)
    i += 1
