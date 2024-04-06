import math
import random
import matplotlib.pyplot as plt
#Made by Chaitanya Garg 2021248
def Bernoulli(p):
    arrivals = []
    for i in range(1000):
      n=0
      iter = 0 
      while(iter < 20):
        iter+=1
        if(random.random()<=p):
          n+=1
      arrivals.append(n)
    plt.hist(arrivals, bins=range(min(arrivals)-2,max(arrivals) + 2), density=False)
    plt.xlabel('Number of arrivals (N20)')
    plt.ylabel('Times Observed')
    plt.title('Bernoulli Process for p = {}'.format(p))
    print("Mean Observation",(sum(arrivals)/1000))
    plt.show()

Bernoulli(0.8) #1.a
Bernoulli(0.5) #1.b
