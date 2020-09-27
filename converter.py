# 2020.09.27
# Guitar Scale Converter
# taewook Nam

import sys

class Converter:

    def __init__(self):

        self.scale = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
        self.SCALE_LENGTH = len(self.scale)

    def convert(self, note, step=1):
        location = 0

        for i in range(self.SCALE_LENGTH):
            if note == self.scale[i]:
                location = i
                break

        if location + step > self.SCALE_LENGTH - 1:
            # print("SCALE_LENGTH :", SCALE_LENGTH, "loaction :", location, "step :", step)
            return self.scale[step - (self.SCALE_LENGTH - 1 - location) - 1]
        else:
            # print("SCALE_LENGTH :", SCALE_LENGTH, "loaction :", location, "step :", step)
            return self.scale[location + step]

    def decode(self):
        inp = input("코드를 띄어쓰기로 구분하여 입력하세요 : ")

        chordList = []

        tmpChord = ''

        for i in range(len(inp)):
            if inp[i] == ' ':
                chordList.append(tmpChord)
                tmpChord = ''
                continue
            tmpChord += inp[i]

        print(chordList)

        step = int(input("키를 입력하세요 : "))
        
        for chord in chordList:
            print(self.convert(chord, step), end=' ')


if __name__ == '__main__':
    # try:
    #     while True:
    #         cvt = Converter()
    #         note_inp = input("음을 입력하세요 : ")
    #         step_inp = int(input("키를 입력하세요 : "))
    #         res = cvt.convert(note_inp, step_inp)
    #         print(res)
    # except KeyboardInterrupt:
    #     sys.exit()
    cvt = Converter()
    cvt.decode()
