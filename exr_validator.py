import os
import OpenEXR
import math

# Input folder path and create a list of the files
inputFolderPath = input("Type the path to the folder containing the files...\n")
filesList = sorted(os.listdir(inputFolderPath))

# Creating the variables to store the results
validFiles = 0
invalidFiles = []
suspiciousFiles = []
filesSize = 0.0

# Check if the files are valid EXR files and calculate the total size
for i in filesList:
    try:
        exr = OpenEXR.InputFile(os.path.join(inputFolderPath, i))
        filesSize += os.path.getsize(os.path.join(inputFolderPath, i))
    except Exception as e:
        invalidFiles.append(i)
        continue

# Create a function to get the average size of the files in a readable format
def getReadableAverageSize(size):
    if size == 0 or not filesList:
        return "0B"
    sizeName = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    avgSize = size / len(filesList)
    i = int(math.floor(math.log(avgSize, 1024)))
    p = math.pow(1024, i)
    s = round(avgSize / p, 2)
    return [s, sizeName[i]]

# Defines the window neighbour numbers to check for suspicious files
window = 10

# Check for suspicious files based on the average size of the neighbors
for i in range(len(filesList)):
    neighborSizes = [
        os.path.getsize(os.path.join(inputFolderPath, filesList[j]))
        for j in range(max(0, i - window), min(len(filesList), i + window + 1)) if j != i
    ]
    avgNeighbors = sum(neighborSizes) / len(neighborSizes)
    currentSize = os.path.getsize(os.path.join(inputFolderPath, filesList[i]))

    if abs(currentSize - avgNeighbors) > (avgNeighbors * 0.2):
        suspiciousFiles.append(filesList[i])
        suspiciousFiles = list(set(suspiciousFiles) - set(invalidFiles))

# Print the results
print("Analyse complete.")
print(f"Total files: {len(filesList)}")
print(f"Valid files: {len(filesList) - len(invalidFiles)}")
if len(invalidFiles) > 0:
    print("Invalid files:")
    for i in invalidFiles:
        print(f" - {i}")
if len(suspiciousFiles) > 0:
    print("Suspicious files:")
    for i in suspiciousFiles:
        print(f" - {i}")

if len(suspiciousFiles) and len(invalidFiles) == 0:
    print("No problems found.")
print(f"Average size: {getReadableAverageSize(filesSize)[0]} {getReadableAverageSize(filesSize)[1]}")

