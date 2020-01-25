'''def filw():
    outfile=open('philosophers.txt','w')#open or create the file with write mode
    outfile.write('16\n')
    outfile.write('15\n')#writing in the file
    outfile.write('12\n')
    outfile.close()#closing the file
def filr():
    outfile=open('philosophers.txt','r')#open or create the file with read mode
    cont=outfile.read()#reading the file
    print(cont)
def filer():
    infile=open('philosophers.txt','r')
    line=infile.readline()
    while line!='':
        amount=float(line)
        print(amount)
        line=infile.readline()
    infile.close()

filw()
filer()'''
import pickle
PhoneBook={'Chris':'555-1111','Katie':'555-2222','Joanne':'555-3333'}
output_file=open('phonebook.dat','wb')
pickle.dump(PhoneBook,output_file)
output_file.close()
in_file=open('phonebook.dat','rb')
pb=pickle.load(in_file)
in_file.close()
print(pb)
