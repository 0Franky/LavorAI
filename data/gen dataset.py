from random import seed
from random import shuffle
import numpy as np

def rand():
  return np.random.randint(1, 6)


numSamples = 10
csv = str(numSamples) + ";10;L1;L2;L3;L4;L5;L6;L7;L8\n"

def getRow():
  r1 = rand()
  r2 = rand()
  r3 = rand()
  r4 = rand()
  r5 = rand()
  r6 = rand()
  r7 = rand()
  r8 = rand()
  r9 = rand()
  r10 = rand()


  # print(r1)
  # print(r2)
  # print(r3)
  # print(r4)
  # print(r5)
  # print(r6)
  # print(r7)
  # print(r8)
  # print(r9)
  # print(r10)
  # print("=======")


  d = np.zeros(6)
  d[r1] += 1
  d[r2] += 1
  d[r3] += 1
  d[r4] += 1
  d[r5] += 1
  d[r6] += 1
  d[r7] += 1
  d[r8] += 1
  d[r9] += 1
  d[r10] += 1

  cat = np.argmax(d)
  # d = d[1:6]
  risp = [r1, r2, r3, r4, r5, r6, r7, r8, r9, r10]


  # print(d)
  # print("=======")
  # print(cat)
  return (risp, cat)


for i in range(0, numSamples):
  row = getRow()
  lav = ((row[1] - 1 ) * 3) + np.random.randint(1, 4)
  csv += (';'.join(map(str, row[0])) + ";" + str(lav) + "\n").replace(".0", "")


f = open("data/ESEMPI_" + str(numSamples) + ".csv", "w")
f.write(csv.strip())
f.close()

# print(csv)
print("Generated!")