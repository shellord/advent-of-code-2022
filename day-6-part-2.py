FILE_PATH = "inputs/day-6.txt"
input_file = open(FILE_PATH, "r")


packet = input_file.read()


def getLastPacketPosition():
    fourteen_packets = []
    for i in range(len(packet)):
        for j in packet[i:]:
            if j not in fourteen_packets:
                fourteen_packets.append(j)
                if(len(fourteen_packets) == 14):
                    return i+14
            else:
                fourteen_packets = []
                break


print(getLastPacketPosition())
