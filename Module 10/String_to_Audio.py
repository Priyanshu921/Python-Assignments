'''import winsound
winsound.PlaySound("C:\\Users\\Priyanshu Patidar\\Downloads\\file_example_WAV_1MG.wav",winsound.SND_FILENAME)
#winsound.PlaySound('Welcome.wav', winsound.SND_FILENAME)'''
import winsound
n=input('Enter Number below 10000')
r=int(n)
if(0<r<=10000):
    m=0
    for i in n:
            if i=='0':
               m+=1
            else:
                p=len(n)-m
                q='0'*(p-1)
                i=i+''+q+'.wav'
                winsound.PlaySound(i, winsound.SND_FILENAME)
                m+=1

