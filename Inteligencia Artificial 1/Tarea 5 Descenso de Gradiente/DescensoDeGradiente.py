
import numpy
import math

e = .001

def Sphere(arr):
    return numpy.dot(arr,arr)

def Rosenbrock(arr):
    sizee = len(arr)
    summ = 0
    for i in range(0, sizee-1):
        summ += 100*(arr[i+1] - arr[i]**2)**2 + (arr[i]-1)**2
    return summ

def Ackley(val):
    X = numpy.array(val)
    Scos = 0
    n = X.size
    Sx2 = numpy.dot( X,X )
    Scos = sum(numpy.cos( 2*math.pi*X ))

    fun = 20+math.exp(1)
    fun -= 20*math.exp( -0.2*math.sqrt((1/n*Sx2) ))
    fun -= math.exp( (1/n) *Scos )
    return fun

def Gradiente(funct,X):
    sizee = len(X)
    result = numpy.zeros((sizee),float)
    aux = numpy.zeros((sizee),float)
    for i in range(sizee):
        aux[i] = e
        result[i] = (funct(aux+X)-funct(X))/e
        aux[i] = 0
    return result

def Hessiano(funct,X):
    sizee = len(X)
    result = numpy.zeros((sizee,sizee),float)
    aux = numpy.zeros((sizee),float)
    for i in range(sizee):
        aux[i] = e
        result[i,:] = (Gradiente(funct,aux+X)-Gradiente(funct,X))/e
        aux[i] = 0
    return result

def GradientePorVector(funct,X,D):
    Xx = numpy.array(X)
    Dd= numpy.array(D)
    aux = Dd * e
    return (funct(aux+Xx)-funct(Xx))/e

def HessianoPorVector(funct,X,D):
    Xx = numpy.array(X)
    Dd = numpy.array(D)
    aux = Dd * e
    return ((Gradiente(funct,aux+Xx)-Gradiente(funct,Xx))/e)

def PasoFijo(xk,pk,funcion):
    return 0.1

def PasoNewton(xk,pk,funcion):
    return .1 #((-numpy.dot(Gradiente(funcion,xk),pk))/(numpy.dot(pk,numpy.matmul(Hessiano(funcion,xk),xk))))

def Backtracking(xk,pk,funcion):
    return 0

def obtenerDireccion(xk,funcion):
    return ((-Gradiente(funcion,xk))/math.sqrt(numpy.dot(Gradiente(funcion,xk),Gradiente(funcion,xk))))

def DescensoDelGradiente(x0,functTamano,funcion):
    maxIte = 100000
    xk = x0
    k = 0
    direccion = numpy.zeros(len(x0))
    tamano = 0
    while(k < maxIte and math.sqrt(numpy.dot(Gradiente(funcion,xk),Gradiente(funcion,xk))) > e):
        tamano = functTamano(xk,direccion,funcion)
        direccion = obtenerDireccion(xk,funcion)
        xk = xk + tamano * direccion
        k += 1
    return xk

vec = [5,6]
print(DescensoDelGradiente(vec,PasoNewton,Ackley))

