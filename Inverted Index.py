import os
import csv
from functools import reduce
import time

#TODO - Optimizations
#TODO - decrease for loops used somehow
#TODO - try applying map and reduce


def createDictionary(directory):

    wordsAdded = {}

    #getting the current directory
    #this is to keep record of where the user was initially
    cwd = os.getcwd()

    #changing the directory to the one passed as argument to make referencing files easier
    #I won't have to write their entire path
    os.chdir(directory)

    #getting the files in the directory
    fileList = os.listdir(directory)

    for file in fileList:

        with open(file, 'r') as f:

            #getting all the words in the file in lowercase
            #also, getting rid of any trailing punctuation
            #removing repetitions of a word in the file
            words = set(map(lambda x: x[:-1] if x[-1] in [',', '!', '?', '.'] else x, f.read().lower().split()))

            for word in words:

                #checking whether the current word is new or not
                if word not in wordsAdded.keys():

                    #if new, creating a new entry for the word in the dictionary
                    wordsAdded[word] = {}
                    wordsAdded[word]['fileNames'] = []
                    wordsAdded[word]['filePaths'] = []

                #adding the file and its path to the dictionary
                wordsAdded[word]['fileNames'] += [f.name]
                wordsAdded[word]['filePaths'] += [(directory[:-1] if directory[-1] == '\\' else directory) + "\\" + f'{f.name}']

    #changing the directory back to the initial one
    os.chdir(cwd)
    return wordsAdded


def writeToFile(words):
    with open('index-file.csv', 'w') as indexFile:

        #declaring the fieldnames for the CSV file
        fieldNames = ['word', 'fileNames', 'filePaths']

        #creating a DictWriter object
        csvWriter = csv.DictWriter(indexFile, fieldnames= fieldNames)

        #writing the header
        csvWriter.writeheader()

        for word, fileDetails in words.items():

            #creating a string of all the file names and file paths
            fileNameString = reduce(lambda x, y: x + ", " + y, fileDetails['fileNames'])
            filePathString = reduce(lambda  x, y: x + ", " + y, fileDetails['filePaths'])

            #writing the row
            csvWriter.writerow({'word': word, 'fileNames': fileNameString, 'filePaths': filePathString})


def main():
    start = time.clock()
    directory = 'G:\\Coding\\Python\\Inverted Index\\text-files'
    writeToFile(createDictionary(directory))
    print("Finished")
    print(time.clock() - start)

if __name__ == '__main__':
    main()
