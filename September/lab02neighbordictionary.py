'''
#------------------------------------------------------------------------------------------------------------------
                                                 #--------------------------------
                                                 Lab02- Dictionary of Neighbors
                                                 Sweta Karlekar
                                                 Pd 4
                                                 9/8/14
                                                 #--------------------------------
    Objective: Create a dictionary with words.txt as keys and neighbors as values. Write this dictionary
    to an outfile and then read the dictionary back in to print. 
#------------------------------------------------------------------------------------------------------------------
'''
def main():
    dictionary = createAndFillDictionary()
    printDictionaryToOutfile(dictionary)
    dictionary = getDictionaryFromOutfile()
    printDictionary(dictionary)

#------------------------------------------------------------------------------------------------------------------

def printDictionaryToOutfile(dict):
    outfile = open('output.txt', 'wb') 
    pickle.dump(dict, outfile)
    outfile.close()

#------------------------------------------------------------------------------------------------------------------

def getDictionaryFromOutfile():
    outfile = open('output.txt', 'rb')
    dict = pickle.load(outfile)
    outfile.close()
    return dict

#------------------------------------------------------------------------------------------------------------------

def printDictionary(dict):
    numkeys = 0
    numvalues = 0
    for k, v in dict.items():
        numkeys = numkeys + 1
        numvalues = numvalues + len(dict[k])
        print('{0}: {1}'.format(k, v))
    print('Number of Keys: ' + str(numkeys))
    print('Number of Values: ' + str(numvalues))

#------------------------------------------------------------------------------------------------------------------

def createAndFillDictionary():
    dict = {}
    for n in range(len(lst)):
        dict[lst[n]] = neighbors(lst[n])
    return dict

#------------------------------------------------------------------------------------------------------------------

def neighbors(myword):
    temp = []
    for n in range(len(lst)):
        diff = 0
        for i in range(6):
            if lst[n][i] != myword[i]:
                diff = diff + 1
        if diff == 1: 
            temp.append(lst[n])
    return temp
 
#------------------------------------Global Variables--------------------------------------------------------------
filename = open('words.txt', 'rb')
lst = filename.read().split('\n')
#------------------------------------------------------------------------------------------------------------------
import pickle
if __name__ == '__main__': main()
#------------------------------------------------------------------------------------------------------------------
