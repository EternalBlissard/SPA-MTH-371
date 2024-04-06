import numpy as np
import matplotlib.pyplot as plt

def randomWalkProbability(numSteps,p):
  mat = np.zeros((2*numSteps+1,2*numSteps+1))
  #matrix of random walk probability where p is the probability of moving forward while 1-p is the probability of moving back by a step

  #2*numSteps is the num of possible steps numSteps being max steps that can be forward and numSteps being max steps that can be backward
  for i in range(2*numSteps+1):
    if(i>0):
      mat[i][i-1]=1-p
    if(i<2*numSteps):
      mat[i][i+1]=p

  #Since we start at the ith state, I have assume state of index numSteps to be i for simplicity
  start_state = np.zeros(2*numSteps+1)
  start_state[numSteps]=1 #as we start here

  for i in range(numSteps):
      start_state = np.dot(start_state, mat)

  return start_state

def RandomWalkSimulator(numSteps,p):
  currPosition = 0
  positions = np.zeros(numSteps + 1)
  positions[0]=currPosition
  for i in range(numSteps):
    if np.random.rand() < p:
      currPosition += 1
    else:
      currPosition -= 1
    positions[i + 1] = currPosition
  return positions

val = np.arange(0,1001)-500

print("\n\npart-a\n\n")

WalkProbability = randomWalkProbability(500,0.5)
plt.plot(val,WalkProbability)
plt.xlabel("Position")
plt.ylabel("Prob")
plt.title("Mathematical Model for 1-D Random Walk (p = 0.5) for 500 steps ")
plt.show()

positionsarr = RandomWalkSimulator(500,0.5)
plt.plot(positionsarr)
plt.xlabel("Step")
plt.ylabel("Position")
plt.title("1-D Random Walk (p = 0.5) for 500 steps ")
plt.show()

simulatedProbability = np.mean(positionsarr == positionsarr[-1])
print("Simulated probability obtained:", simulatedProbability)
print("Expected probability obtained:", WalkProbability[int(positionsarr[-1])+500])

print("\n\npart-b\n\n")

WalkProbability = randomWalkProbability(500,0.8)
plt.plot(val,WalkProbability)
plt.xlabel("Position")
plt.ylabel("Prob")
plt.title("Mathematical Model for 1-D Random Walk (p = 0.8) for 500 steps ")
plt.show()

positionsarr = RandomWalkSimulator(500,0.8)
plt.plot(positionsarr)
plt.xlabel("Step")
plt.ylabel("Position")
plt.title("1-D Random Walk (p = 0.8) for 500 steps ")
plt.show()

simulatedProbability = np.mean(positionsarr == positionsarr[-1])
print("Simulated probability obtained:", simulatedProbability)
print("Expected probability obtained:", WalkProbability[int(positionsarr[-1])+500])

print("\n\npart-c\n\n")

randomWalk = np.zeros(1001)
p=0.5
for i in range(1000):
  positions = RandomWalkSimulator(500,p)
  plt.plot(positions)
  randomWalk[int(positions[-1])+500]+=1

plt.xlabel("Step")
plt.ylabel("Position")
plt.title("1-D Random Walk (p = 0.5) for 500 steps ")
plt.show()

plt.plot(val,randomWalk)
plt.xlabel("Position")
plt.ylabel("Prob")
plt.title("Simulated Model for 1-D Random Walk (p = 0.5) for 500 steps ")
plt.show()

randomWalk = np.zeros(1001)
p=0.8
for i in range(1000):
  positions = RandomWalkSimulator(500,p)
  plt.plot(positions)
  randomWalk[int(positions[-1])+500]+=1

plt.xlabel("Step")
plt.ylabel("Position")
plt.title("1-D Random Walk (p = 0.8) for 500 steps ")
plt.show()

plt.plot(val,randomWalk)
plt.xlabel("Position")
plt.ylabel("Prob")
plt.title("Simulated Model for 1-D Random Walk (p = 0.8) for 500 steps ")
plt.show()

