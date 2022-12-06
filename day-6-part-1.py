FILE_PATH = "inputs/day-6.txt"
input_file = open(FILE_PATH, "r")


packet = input_file.read()


def getLastPacketPosition():
    four_packets = []
    for i in range(len(packet)):
        for j in packet[i:]:
            if j not in four_packets:
                four_packets.append(j)
                if(len(four_packets) == 4):
                    return i+4
            else:
                four_packets = []
                break


print(getLastPacketPosition())
