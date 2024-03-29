"""
Authors - Kundan Kumar (kk7272) & Deepam Shah (ds3689)
Version - 4
Revision - 3
transformer.py file is the main file which takes data from instruction.txt
and message.txt file
There are 5 transformations in this code namely sigma, ro, delta, tau and alpha.
Alpha transformation is our own function which makes a palindrome of that
input word.

"""
import sys
import textwrap


def shiftRight(character, move):
    move = move % 26
    moved = ord(character) + move
    if moved > 90:
        moved = 64 + (moved - 90)
    return chr(moved)


def shiftLeft(character, move):
    move = move % 26
    moved = ord(character) - move
    if moved < 65:
        moved = 91 - (65 - moved)
    return chr(moved)

# sigma transformation takes 4 variables cipher, message,index and times
# cipher can either be 'e' encryption or 'd' decryption
# message is the message which we want to encrypt or decrypt
# index is the position and times refer to the number of times the
# transformation should happen
def sigmaTransformation(cipher, message, index, times=1):
    if cipher is "e":
        if times > 0:
            return message[0:index] + shiftRight(message[index], times) + \
                   message[index + 1:]
        else:
            return message[0:index] + shiftLeft(message[index], times) + \
                   message[index + 1:]
    elif cipher is "d":
        if times > 0:
            return message[0:index] + shiftLeft(message[index], times) + \
                   message[index + 1:]
        else:
            return message[0:index] + shiftRight(message[index], times) + \
                   message[index + 1:]
    else:
        return None

# ro transformation takes 3 variables cipher, message and times
# cipher can either be 'e' encryption or 'd' decryption
# message is the message which we want to encrypt or decrypt
# times refer to the number of times the transformation should happen
def roTransformation(cipher, message, times=1):
    times = times % len(message)
    if cipher is "e":
        if times > 0:
            return message[-times:] + message[:-times]
        else:
            return message[times:] + message[:times]
    elif cipher is "d":
        if times > 0:
            return message[times:] + message[:times]
        else:
            return message[-times:] + message[:-times]
    return None

# delta transformation takes 4 variables cipher, message,index and times
# cipher can either be 'e' encryption or 'd' decryption
# message is the message which we want to encrypt or decrypt
# index is the position and times refer to the number of times the
# transformation should happen

def deltaTransformation(cipher, message, index, times=1):
    if cipher is "e":
        return message[:index] + message[index]*times + message[index:]
    elif cipher is "d":
        return message[:index] + message[index+times:]
    return None

# ta transformation takes 5 variables cipher, message,indexI,indexJ
# and divide
# cipher can either be 'e' encryption or 'd' decryption
# message is the message which we want to encrypt or decrypt
# indexI and indexJ is used to transfer the alphabet at indexI and indexJ

def tauTransformation(cipher, message, indexI, indexJ, divide=1):
    divided = textwrap.wrap(message, divide)
    divided[indexI], divided[indexJ] = divided[indexJ], divided[indexI]
    return "".join(divided)

# alpha transformation takes 2 variables cipher and message
# if we choose 'e' as cipher and our message is race, it will
# convert it to racecar
# similarly if we choose 'd' as cipher and our message is racecar,
# it will convert to race
def alphaTransformation(cipher, message):
    if cipher is "e":
        return message + message[len(message)-2::-1]
    elif cipher is "d":
        return message[:len(message)//2+1]
    else:
        return None


def main():
    # if len(sys.argv) == 5:
    #     message = sys.argv[1]
    #     instruction = sys.argv[2]
    #     output = sys.argv[3]
    #     cipher = sys.argv[4]
    # else:
    #     print("You provided invalid command line arguments. "
    #           "Please provide them separately")
    #     message = input("Enter message file name [message.txt]\n")
    #     instruction = input("Enter instruction file name [instruction.txt]\n")
    #     output = input("Enter output file name [output.txt]\n")
    #     cipher = input("encrypt or decrypt ? [e/d]\n")
    #
    # # message = "message.txt"
    # # instruction = "instruction.txt"
    # # output = "output.txt"
    # # cipher = "e"
    # feed = []
    # with open(message) as messageFile, open(instruction) as instructionFile:
    #     for messageLine, instructionLine in zip(messageFile, instructionFile):
    #         feed.append([messageLine.strip(), instructionLine.strip()])
    # for index, inputLine in enumerate(feed):
    #     text = inputLine[0]
    #     allInst = inputLine[1].split(";")
    #     if cipher == "d":
    #         allInst.reverse()
    #     result = ""
    #     for inst in allInst:
    #         if inst[0] is "S":
    #             if "," in inst:
    #                 commaIndex = inst.index(",")
    #                 result = sigmaTransformation(cipher, text,
    #                         int(inst[1:commaIndex]), int(inst[commaIndex + 1:]))
    #             else:
    #                 result = sigmaTransformation(cipher, text, int(inst[1:]))
    #         elif inst[0] is "R":
    #             if len(inst) is 1:
    #                 result = roTransformation(cipher, text)
    #             else:
    #                 result = roTransformation(cipher, text, int(inst[1:]))
    #         elif inst[0] is "D":
    #             if "," in inst:
    #                 commaIndex = inst.index(",")
    #                 result = deltaTransformation(cipher, text,
    #                         int(inst[1:commaIndex]), int(inst[commaIndex + 1:]))
    #             else:
    #                 result = deltaTransformation(cipher, text, int(inst[1:]))
    #         elif inst[0] is "T":
    #             if "(" in inst:
    #                 openBracketIndex = inst.index("(")
    #                 closedBracketIndex = inst.index(")")
    #                 commaIndex = inst.index(",")
    #                 result = tauTransformation(cipher, text,
    #                          int(inst[closedBracketIndex+1:commaIndex]),
    #                          int(inst[commaIndex + 1:]), len(text)//
    #                             int(inst[openBracketIndex+1:closedBracketIndex]))
    #             else:
    #                 commaIndex = inst.index(",")
    #                 result = tauTransformation(cipher, text,
    #                         int(inst[1:commaIndex]), int(inst[commaIndex + 1:]))
    #         elif inst is "A":
    #             result = alphaTransformation(cipher, text)
    #         text = result
    #     feed[index].append(result)
    # with open(output, "w") as outputFile:
    #     for result in feed:
    #         print("{}\t{}\t{}".format(result[0],result[1],result[2]))
    #         outputFile.write(result[2]+"\n")
    #
    #
    #
    #
    xxx = []
    message = "message.txt"
    with open(message) as messageFile:
        for messageLine in messageFile:
           xxx = messageLine.split(",")
        for x in xxx:
            print(x)


if __name__ == '__main__':
    main()
