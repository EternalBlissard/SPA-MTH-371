import math
import random
import matplotlib.pyplot as plt
import matplotlib

#Made by Chaitanya Garg 2021248
def Poisson(lam, t):
    arrivals = []
    lamt = lam*t
    sim=1000
    for i in range(sim):
        n = 0
        start = 0
        while start < t:
            start += -math.log(1 - random.random()) / lam #Adding delta t
            if start < t:
                n += 1
        arrivals.append(n)

    # Plot the simulated density
    plt.hist(arrivals, bins=range(max(arrivals) + 2), density=True)
    plt.xlabel('Number of arrivals')
    plt.ylabel('Density(Weight/{})'.format(sim))
    plt.title('Density of arrivals until time t = {} Mean={}'.format(t,sum(arrivals)/sim))
    plt.show()
    # Calculate the mean value of arrivals
    mean_arrivals = lam * t

    print('The mean value of arrivals is {}.'.format(mean_arrivals))


def PoissonFirstArrival(lam, t):
    arrivals = []
    lamt = lam*t #Mean
    index=[]
    for i in range(1000):
        index.append(i+1)
        n = 0
        start = 0
        while start < t:
            start += -math.log(1 - random.random()) / lam #Calculating delt
            if start < t:
                n += 1
                break
        arrivals.append(start) #Appending it to array/list
    # plt.hist(arrivals, bins=range(max(arrivals) + 2), density=True)
    return arrivals,index 
    

Poisson(5,10) #2.a
Poisson(15,10) #2.b
Arrivals1,Index1=PoissonFirstArrival(5, 10)
plt.scatter(Index1, Arrivals1)
plt.xlabel('Number of arrivals')
plt.ylabel('Time of first arrival (in hour)')
plt.title('Time until First Arrival for t= {} Mean={}'.format(10,sum(Arrivals1)/1000))
plt.show()
plt.hist(Arrivals1,bins=int(max(Arrivals1)*10), density=True)
plt.xlabel('Number of arrivals')
plt.ylabel('Time of first arrival (in hour)')
plt.title('Time until First Arrival for t= {} Mean={}'.format(10,sum(Arrivals1)/1000))
plt.show()

Arrivals2,Index2=PoissonFirstArrival(15, 10)
plt.scatter(Index2, Arrivals2)
plt.xlabel('Number of arrivals')
plt.ylabel('Time of first arrival (in hour)')
plt.title('Time until First Arrival for t= {} Mean={}'.format(10,sum(Arrivals2)/1000))
plt.show()
plt.hist(Arrivals2,bins=int(max(Arrivals2)*30), density=True)
plt.xlabel('Number of arrivals')
plt.ylabel('Time of first arrival (in hour)')
plt.title('Time until First Arrival for t= {} Mean={}'.format(10,sum(Arrivals2)/1000))
plt.show()
