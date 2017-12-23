import os

#TODO - Optimizations
#TODO - decrease for loops used somehow
#TODO - try applying map and reduce
#TODO - make directory user-selected


def createDictionary():

    wordsAdded = {}
    cwd = os.getcwd()
    os.chdir('G:\\Coding\\Python\\Inverted Index\\text-files')
    fileList = os.listdir(os.getcwd())

    for file in fileList:

        with open(file, 'r') as f:

            words = f.read().lower().split()

            for word in words:

                if word[-1] in [',', '!', '?', '.']:
                    word = word[:-1]
                if word not in wordsAdded.keys():
                    wordsAdded[word] = [f.name]

                else:
                    if file not in wordsAdded[word]:
                        wordsAdded[word] += [f.name]

    return wordsAdded, cwd


def writeToFile(words, cwd):
    os.chdir(cwd)
    with open('index-file.txt', 'w') as indexFile:

        for word, files in words.items():
            indexFile.write(word + " ")
            for file in files:
                indexFile.write(file[:file.find(".txt")] + " ")

            indexFile.write(f'{len(files)}\n')


writeToFile(*createDictionary())
