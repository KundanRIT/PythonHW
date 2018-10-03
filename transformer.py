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


def sigmaTransformation(cipher, message, index, times=1):
    if cipher is "e":
        return message[0:index] + shiftRight(message[index], times) + message[
                                                                     index + 1:]
    elif cipher is "d":
        return message[0:index] + shiftLeft(message[index], times) + message[
                                                                     index + 1:]
    else:
        return None


def roTransformation(cipher, message, times=1):
    times = times % len(message)
    if cipher is "e":
        return message[-times:][::-1] + message[:-times]
    elif cipher is "d":
        return message[times:] + message[:times][::-1]
    return None


def deltaTransformation(cipher, message, index, times=1):
    if cipher is "e":
        return message[:index] + message[index]*times + message[index+1:]
    elif cipher is "d":
        return message[:index] + message[index+times-1:]
    return None


def tauTransformation(cipher, message, indexI, indexJ, divide=1):
    divided = textwrap.wrap(message, divide)
    divided[indexI], divided[indexJ] = divided[indexJ], divided[indexI]
    return "".join(divided)


def alphaTransformation(cipher, message):
    if cipher is "e":
        return message + message[len(message)-2::-1]
    elif cipher is "d":
        return message[:len(message)//2+1]
    else:
        return None


def main():
    message = "message.txt"
    instruction = "instruction.txt"
    output = "output.txt"
    cipher = "e"
    feed = []
    with open(message) as messageFile, open(instruction) as instructionFile:
        for messageLine, instructionLine in zip(messageFile, instructionFile):
            feed.append([messageLine.strip(), instructionLine.strip()])
    for index, input in enumerate(feed):
        text = input[0]
        allInst = input[1].split(";")
        result = ""
        for inst in allInst:
            if inst[0] is "S":
                if "," in inst:
                    commaIndex = inst.index(",")
                    result += sigmaTransformation(cipher, text,
                            int(inst[1:commaIndex]), int(inst[commaIndex + 1:]))
                else:
                    result += sigmaTransformation(cipher, text, int(inst[1:]))
            elif inst[0] is "R":
                if len(inst) is 1:
                    result += roTransformation(cipher, text)
                else:
                    result += roTransformation(cipher, text, int(inst[1:]))
            elif inst[0] is "D":
                if "," in inst:
                    commaIndex = inst.index(",")
                    result += deltaTransformation(cipher, text,
                            int(inst[1:commaIndex]), int(inst[commaIndex + 1:]))
                else:
                    result += deltaTransformation(cipher, text, int(inst[1:]))
            elif inst[0] is "T":
                if "(" in inst:
                    openBracketIndex = inst.index("(")
                    closedBracketIndex = inst.index(")")
                    commaIndex = inst.index(",")
                    result += tauTransformation(cipher, text,
                             int(inst[closedBracketIndex+1:commaIndex]),
                             int(inst[commaIndex + 1:]), len(text)//
                                int(inst[openBracketIndex+1:closedBracketIndex]))
                else:
                    commaIndex = inst.index(",")
                    result += tauTransformation(cipher, text,
                            int(inst[1:commaIndex]), int(inst[commaIndex + 1:]))
            elif inst is "A":
                result += alphaTransformation(cipher, text)
        feed[index].append(result)
    with open(output, "a") as outputFile:
        for result in feed:
            print("{}\t{}\t{}".format(result[0],result[1],result[2]))
            outputFile.write(result[2]+"\n")


if __name__ == '__main__':
    main()