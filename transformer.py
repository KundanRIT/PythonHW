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
        inst = input[1]
        result = None
        if inst[0] is "S":
            if "," in inst:
                commaIndex = inst.index(",")
                result = sigmaTransformation(cipher, text,
                        int(inst[1:commaIndex]), int(inst[commaIndex + 1:]))
            else:
                result = sigmaTransformation(cipher, text, int(inst[1:]))
        feed[index].append(result)
    for result in feed:
        print("{}\t{}\t{}".format(result[0],result[1],result[2]))


if __name__ == '__main__':
    main()