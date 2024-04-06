import numpy as np
import matplotlib.pyplot as plt

# S = {r, w, e, s}
P =np.array([ [0.5,0.3, 0, 0.2],
              [0.2, 0.5, 0.1, 0.2],
              [0.1,0.3, 0.3, 0.3],
              [0, 0.2, 0.3, 0.5]])

def markov_chain_evolution(numSteps, initialStateDistribution, transititonProbabilityMatrix):
  #TPM of the markov process is given by the matrix transititonProbabilityMatrix
  #pi(0) is the initialStateDistribution
  #pi(numSteps) is the finalStateDistribution after executing numSteps on the pi(0)

  #we start at pi(0)
  currentStateDistribution = initialStateDistribution
  for i in range(numSteps):
    currentStateDistribution = np.dot(currentStateDistribution, transititonProbabilityMatrix)
  mat = transititonProbabilityMatrix
  for i in range(numSteps-1):
    mat = np.dot(mat, transititonProbabilityMatrix)
  print(f"P{numSteps}={mat}")
  return currentStateDistribution

print("Part-a\n\n")
#To see the evolution after 20 min we observe pi(20)
numSteps = 20
#Assuming equally probable distribution for initialStateDistribution
initialDistribution = np.array([0.25, 0.25,0.25,0.25])

#Distribution after 20 steps
DistributionAfter20 = markov_chain_evolution(numSteps,initialDistribution, P)
print("Distribution after 20 steps", DistributionAfter20)


#For P(X20=s|X0=r) we can take the initial distribution as [1,0,0,0]
initialDistribution = np.array([1,0,0,0])
#Distribution after 20 steps
DistributionAfter20 = markov_chain_evolution(numSteps,initialDistribution, P)
print("Distribution after 20 steps", DistributionAfter20)
print("P(X20=s|X0=r)",DistributionAfter20[3])

print("\n\npart-b\n\n")

#To see the evolution after 25 min we observe pi(25)
numSteps = 25
#Assuming equally probable distribution for initialStateDistribution
initialDistribution = np.array([0.25, 0.25,0.25,0.25])

#Distribution after 25 steps
DistributionAfter25 = markov_chain_evolution(numSteps,initialDistribution, P)
print("Distribution after 25 steps", DistributionAfter25)

#For P(X25=s|X20=s)=P(X5=s|X0=s) we can take the initial distribution as [0,0,0,1]
initialDistribution = np.array([0,0,0,1])
#Distribution after 5 steps
numSteps=5
DistributionAfter5 = markov_chain_evolution(numSteps,initialDistribution, P)
print("Distribution after 5 steps", DistributionAfter5)
print("P(X25=s|X20=s)",DistributionAfter5[3])

print("\n\npart-c\n\n")

def computingStationaryDistribution(P):
  PT=np.transpose(P)

  # Eigenvalues and eigenvectors of the transpose
  eigenvalues, eigenvectors = np.linalg.eig(PT)

  # Find the eigenvector corresponding to eigenvalue 1 to obtain the relevant stationary distribution
  stationary_distri = eigenvectors[:,np.where(np.isclose(eigenvalues, 1))[0][0]]

  # Normalize the stationary distribution to 0-1 scale
  stationary_distri /= np.sum(stationary_distri)

  return stationary_distri

StationaryDistri = computingStationaryDistribution(P)
print(f"Stationery Distribution obtained is{StationaryDistri}")

print("\n\npart-d\n\n")

def limitingDistribution(initialDistribution):
  currentDistribution = initialDistribution
  iter=0
  while(np.dot(currentDistribution, P)[0]!=currentDistribution[0] or np.dot(currentDistribution, P)[1]!=currentDistribution[1] or np.dot(currentDistribution, P)[2]!=currentDistribution[2] or np.dot(currentDistribution, P)[3]!=currentDistribution[3]):
    iter+=1
    currentDistribution=np.dot(currentDistribution, P)
    # print(currentDistribution,np.dot(currentDistribution, P))
  print(f"Convergence obtained after iter {iter} for initialDistribution:{initialDistribution}")
  print("limiting Distribution:",currentDistribution,"product of limiting Distribution with P: for check",np.dot(currentDistribution, P))

initialDistribution1 = np.array([0.25,0.25,0.25,0.25])
initialDistribution2 = np.array([1,0,0,0])
initialDistribution3 = np.array([0,0,0,1])
initialDistribution4 = np.array([0.5,0,0,0.5])
limitingDistribution(initialDistribution1)
limitingDistribution(initialDistribution2)
limitingDistribution(initialDistribution3)
limitingDistribution(initialDistribution4)