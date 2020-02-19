from pathlib import Path

def smallestVillage(villages):
    answer = -1
    for i in range(1,len(villages)-1):
        size = (villages[i]-villages[i-1])/2 + (villages[i+1]-villages[i])/2
        if(answer == -1):
            answer = size
        elif(answer >= size):
            answer = size

    return answer

villages = []

file = open("windows_data\S1\s1.15.in",'r')
lines = file.readlines()[1:]

for line in lines:
    villages = villages + [int(line)]

villages.sort()
print(smallestVillage(villages))
