# Hashing Algorithm Experiment II

import cmath
import pprint

# Accept arbitrary message length
givenMessage = input("What shall we hash today? ")
preOrdImage = 0
# Length of 4 assigned if input = ''
messageLength = 4
asciiMessage = []
asciiMessageTwo = []
binaryHash = []
hashPadValue = []
hashDictionary = {}
padDictionary = {}
finalDictionary = {}
finalHash = ''

# Convert message to ASCII
def createAsciiMessage():
    global asciiMessage, givenMessage, preOrdImage, asciiMessageTwo
    for c in givenMessage:
        preOrdImage = ord(c)
        asciiMessage.append(preOrdImage)
    asciiMessage = ''.join(map(str, asciiMessage))
    asciiMessageTwo = ''.join(map(str, asciiMessage))
    print("ASCII Digest: " + asciiMessage)

# Append the binary of each ASCII character
def createBinaryHash():
    global asciiMessage
    for c in asciiMessage:
        asciiMessage = ord(c)
        asciiMessage = bin(asciiMessage)[2:].zfill(8)
        binaryHash.append(asciiMessage)

# Create message blocks
def createMessageBlock(givenList, blockSize):
    blockSize = max(1, blockSize)
    for i in range(0, len(givenList), blockSize):
       hashDictionary["messageBlock_{0}".format(i)] = (givenList[i:i+blockSize])

# Create value to pad hash regardless of len(input)
def createPadValue():
    global givenMessage, asciiMessage, padValue, asciiMessageTwo, messageLength
    padValue = 0
    if asciiMessage != '':
        messageLength = len(givenMessage)
        asciiValue = int(asciiMessageTwo)
        padValue = (abs((asciiValue ** 2) + cmath.sqrt((asciiValue * messageLength))))
        padValue = int(padValue) ** 64
    else:
        # Produce value at length zero
        padValue = 794839138932842334414846966981417223553 ** 8

# Isolate intergers from padValue for later mutations
def isolatePadValues():
    global padValue, valueAtFour, valueAtTwentySeven, valueAtTwentyTwo, valueAtFortyThree
    valueAtFour = str(padValue)
    valueAtFour = int(valueAtFour[4:5])
    valueAtTwentyTwo = str(padValue)
    valueAtTwentyTwo = int(valueAtTwentyTwo[22:23])
    valueAtTwentySeven = str(padValue)
    valueAtTwentySeven = int(valueAtTwentySeven[27:28])
    valueAtFortyThree = str(padValue)
    valueAtFortyThree = int(valueAtFortyThree[43:44])

# Convert pad value into binary
def padValueBinaryHash():
    global padValue
    padValue = str(padValue)
    for c in padValue:
        padValue = ord(c)
        padValue = bin(padValue)[2:].zfill(8)
        hashPadValue.append(padValue)

# Create blocks based of off padValue
def createPadBlock(givenList, blockSize):
    blockSize = max(1, blockSize)
    for i in range(0, len(givenList), blockSize):
       padDictionary["messageBlock_{0}".format(i)] = (givenList[i:i+blockSize])

# Pad last messageBlock to 4 binary characters
def padMessageBlock(giveDictionary):
    blockLength = list(giveDictionary.values())
    for i in blockLength:
        while len(i) < 4:
            i.append('01010011')
            continue

# Merge dictionaries
def mergeDictionaries():
    global finalDictionary
    # messageBinaryBlocks will overwrite padMessageBlocks at corresponding block integer
    finalDictionary = {**padDictionary, **hashDictionary}

# Mutate Hash: Layer One
def mutateHashLayerOne():
    global finalDictionary, messageLength, valueAtTwentySeven, valueAtTwentyTwo
    dictionaryValues = list(finalDictionary.values())
    for i in dictionaryValues[messageLength:5:9]:
        i[1::] = ['{0}{3}{7}{2}{3}{5}{6}{4}'.format(*byteUnit) for byteUnit in i[1::]]
        i[2::] = ['{0}{3}{2}{1}{4}{7}{6}{5}'.format(*byteUnit) for byteUnit in i[2::]]
        i[2::3] = ['{0}{5}{2}{3}{4}{6}{7}{1}'.format(*byteUnit) for byteUnit in i[2::3]]
        i[3::4] = ['{0}{1}{2}{1}{4}{5}{6}{7}'.format(*byteUnit) for byteUnit in i[3::4]]
    for i in dictionaryValues[valueAtTwentySeven::7]:
        i[1::] = ['{0}{6}{2}{3}{4}{5}{1}{7}'.format(*byteUnit) for byteUnit in i[1::]]
        i[2::] = ['{0}{3}{5}{2}{4}{5}{4}{7}'.format(*byteUnit) for byteUnit in i[2::]]
        i[2::3] = ['{0}{1}{2}{3}{4}{5}{6}{7}'.format(*byteUnit) for byteUnit in i[2::3]]
        i[3::4] = ['{0}{3}{2}{3}{4}{5}{1}{7}'.format(*byteUnit) for byteUnit in i[3::4]]
    for i in dictionaryValues[valueAtTwentyTwo::15]:
        i[1::] = ['{0}{7}{4}{3}{1}{5}{6}{1}'.format(*byteUnit) for byteUnit in i[1::]]
        i[2::] = ['{0}{3}{2}{1}{4}{7}{6}{5}'.format(*byteUnit) for byteUnit in i[2::]]
        i[2::3] = ['{0}{4}{2}{3}{5}{6}{7}{1}'.format(*byteUnit) for byteUnit in i[2::3]]
        i[3::4] = ['{0}{3}{2}{1}{7}{5}{6}{4}'.format(*byteUnit) for byteUnit in i[3::4]]

def mutateHashLayerTwo():
    global finalDictionary, messageLength, valueAtFour, valueAtFortyThree
    dictionaryValues = list(finalDictionary.values())
    for i in dictionaryValues[valueAtFour::7]:
        i[1::] = ['{0}{5}{4}{3}{1}{2}{6}{7}'.format(*byteUnit) for byteUnit in i[1::]]
        i[2::] = ['{0}{3}{2}{1}{4}{7}{6}{5}'.format(*byteUnit) for byteUnit in i[2::]]
        i[2::3] = ['{0}{5}{2}{3}{4}{6}{7}{1}'.format(*byteUnit) for byteUnit in i[2::3]]
        i[3::4] = ['{0}{1}{2}{1}{4}{5}{6}{7}'.format(*byteUnit) for byteUnit in i[3::4]]
    for i in dictionaryValues[valueAtFortyThree::56]:
        i[1::] = ['{0}{2}{4}{3}{1}{5}{6}{1}'.format(*byteUnit) for byteUnit in i[1::]]
        i[2::] = ['{0}{3}{2}{1}{4}{7}{6}{5}'.format(*byteUnit) for byteUnit in i[2::]]
        i[2::3] = ['{0}{7}{6}{5}{4}{3}{1}{2}'.format(*byteUnit) for byteUnit in i[2::3]]
        i[3::4] = ['{0}{3}{2}{1}{7}{5}{6}{4}'.format(*byteUnit) for byteUnit in i[3::4]]
    for i in dictionaryValues[messageLength::4]:
        i[1::] = ['{0}{1}{2}{3}{4}{5}{6}{7}'.format(*byteUnit) for byteUnit in i[1::]]
        i[2::] = ['{0}{4}{5}{3}{2}{5}{4}{7}'.format(*byteUnit) for byteUnit in i[2::]]
        i[2::3] = ['{0}{1}{2}{3}{4}{5}{6}{7}'.format(*byteUnit) for byteUnit in i[2::3]]
        i[3::4] = ['{0}{3}{2}{3}{4}{5}{1}{7}'.format(*byteUnit) for byteUnit in i[3::4]]
       
# Convert Hash back to Unicode
def convertHash():
    global finalDictionary, finalHash
    finalDictionary = sum(finalDictionary.values(), [])
    for c in finalDictionary:
        finalHash += chr(int(c,2))

# Scramble the hash
def reOrderHash():
    global finalHash
    finalHash = finalHash[:256]
    reIndexHash = [36, 71, 125, 164, 42, 132, 188, 202, 239, 135, 9, 251, 147, 
    161, 233, 183, 60, 208, 242, 27, 96, 1, 177, 143, 22, 165, 121, 150, 232, 
    241, 194, 50, 140, 74, 138, 145, 186, 122, 151, 95, 158, 199, 171, 111, 47, 
    127, 21, 123, 200, 231, 221, 141, 193, 68, 48, 206, 4, 169, 53, 56, 167, 
    129, 119, 18, 162, 40, 182, 20, 109, 211, 51, 52, 157, 25, 209, 198, 214, 6, 
    64, 229, 98, 29, 215, 201, 82, 66, 159, 195, 160, 79, 131, 93, 30, 139, 49, 
    116, 69, 7, 191, 243, 234, 89, 130, 227, 247, 124, 75, 210, 99, 173, 120, 80, 
    63, 105, 148, 17, 115, 57, 252, 185, 180, 65, 172, 106, 34, 137, 90, 136, 
    113, 8, 187, 94, 219, 32, 43, 254, 39, 33, 250, 203, 152, 155, 5, 176, 222, 
    244, 59, 178, 19, 73, 46, 62, 16, 189, 77, 72, 207, 133, 92, 87, 225, 205, 
    37, 58, 97, 3, 26, 24, 220, 55, 196, 156, 163, 101, 15, 246, 213, 110, 108, 
    230, 38, 45, 190, 104, 204, 226, 103, 102, 88, 223, 11, 168, 235, 70, 237, 
    154, 85, 91, 117, 128, 67, 61, 134, 10, 13, 2, 170, 153, 179, 112, 31, 175, 28, 
    0, 224, 249, 81, 144, 228, 174, 240, 14, 192, 255, 126, 197, 84, 181, 35, 
    142, 78, 23, 245, 83, 253, 248, 216, 184, 86, 146, 149, 54, 12, 118, 44, 238, 
    100, 41, 218, 212, 166, 217, 76, 236, 114, 107]
    
    for i in range(64):
        finalHash = [finalHash[i] for i in reIndexHash]
        finalHash = finalHash[::-1]
    finalHash = ''.join(finalHash)

createAsciiMessage()
createBinaryHash()
print("Initial Message Bytes: " + str(len(binaryHash)))
createPadValue()
isolatePadValues()
createMessageBlock(binaryHash, 4)
padMessageBlock(hashDictionary)
padValueBinaryHash()
createPadBlock(hashPadValue, 4)
padMessageBlock(padDictionary)
mergeDictionaries()
mutateHashLayerOne()
mutateHashLayerTwo()
pprint.pprint(finalDictionary)
print("Message Length: " + str(messageLength))
convertHash()
reOrderHash()
print(len(finalHash))
print(finalHash)
