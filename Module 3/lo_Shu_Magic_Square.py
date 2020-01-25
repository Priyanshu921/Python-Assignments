def LsMs(magicSquare):
    if(magicSquare[0][0]+magicSquare[0][1]+magicSquare[0][2]==magicSquare[1][0]+magicSquare[1][1]+magicSquare[1][2])and(magicSquare[0][0]+magicSquare[0][1]+magicSquare[0][2]==magicSquare[2][0]+magicSquare[2][1]+magicSquare[2][2])and((magicSquare[1][0]+magicSquare[1][1]+magicSquare[1][2]==magicSquare[2][0]+magicSquare[2][1]+magicSquare[2][2])):
        return True
magicSquare=[[4,9,2],[3,5,7],[8,1,6]]
if(LsMs(magicSquare)):
    print("Magic Square")
else:
    print("Not a Magic Square")
