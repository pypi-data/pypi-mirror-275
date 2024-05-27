
class Protocal():
    def __init__(self):
        self.buffers = []
        for i in range(11):
            self.buffers.append(0)

    def makePacket(self, index, para1, para2, para3, para4):
        self.buffers[0] = 0
        self.buffers[1] = index
        self.buffers[2] = para1
        self.buffers[3] = para2
        self.buffers[4] = para3
        self.buffers[5] = para4
        self.buffers[6] = 90
        self.buffers[7] = 7
        self.buffers[8] = 253
        self.buffers[9] = 254
        self.buffers[10] = 254

    def makePacketMenuSetting(self, main, sub):
        self.makePacket(0, 11, main, sub, 255)
        return self.buffers
    
