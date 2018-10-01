def main():
    message = "message.txt"
    instruction = "instruction.txt"
    output = "output.txt"

    with open(message) as messageFile, open(instruction) as instructionFile:
        for messageLine, instructionLine in zip(messageFile, instructionFile):
            print("{}\t{}".format(messageLine.strip(), instructionLine.strip()))

if __name__ == '__main__':
    main()