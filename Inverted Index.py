import os
import csv
from functools import reduce

#TODO - Optimizations
#TODO - decrease for loops used somehow
#TODO - try applying map and reduce


def createDictionary(directory):

    wordsAdded = {}
    cwd = os.getcwd()
    os.chdir(directory)
    fileList = os.listdir(directory)

    for file in fileList:

        with open(file, 'r') as f:

            words = f.read().lower().split()

            for word in words:

                if word[-1] in [',', '!', '?', '.']:
                    word = word[:-1]
                if word not in wordsAdded.keys():
                    wordsAdded[word] = {}
                    wordsAdded[word]['fileNames'] = [f.name]
                    wordsAdded[word]['filePaths'] = [(directory[:-1] if directory[-1] == '\\' else directory) + "\\" + f'{f.name}']
                else:
                    if file not in wordsAdded[word]['fileNames']:
                        wordsAdded[word]['fileNames'] += [f.name]
                        wordsAdded[word]['filePaths'] += [(directory[:-1] if directory[-1] == '\\' else directory) + "\\" + f'{f.name}']

    os.chdir(cwd)
    return wordsAdded


def writeToFile(words):
    with open('index-file.csv', 'w') as indexFile:
        fieldNames = ['word', 'fileNames', 'filePaths']
        csvWriter = csv.DictWriter(indexFile, fieldnames= fieldNames)

        csvWriter.writeheader()

        for word, fileDetails in words.items():
            fileNameString = reduce(lambda x, y: x + ", " + y, fileDetails['fileNames'])
            filePathString = reduce(lambda  x, y: x + ", " + y, fileDetails['filePaths'])
            csvWriter.writerow({'word': word, 'fileNames': fileNameString, 'filePaths': filePathString})



directory = input("Enter the directory whose files you'd like to index: ")
writeToFile(createDictionary(directory))
