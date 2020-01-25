import pickle
class Contact:
    def __init__(self,name,pnum,email):
        self.__name=name
        self.__pnum=pnum
        self.__email=email
    def set_name(self,newname):
        self.__name=newname
    def set_phone(self,newphone):
        self.__pnum=newphone
    def set_email(self,newemail):
        self.__email=newemail
    def get_name(self):
        return self.__name
    def get_phone(self):
        return self.__pnum
    def get_email(self):
        return self.__email
    def __str__(self):
        return f'name :- {self.__name}\nPhone Number :- {self.__pnum}\nEmail :- {self.__email}'
def new_file():
    
    con={}
    out_file=open('contact.dat','wb')
    pickle.dump(con,out_file)
    out_file.close()
def add_contact():
    try:
        out_file=open('contact.dat','rb')
        con=pickle.load(out_file)
        out_file.close()
        rno=input("Enter unique key")
        name=input('Enter your name')
        phone_number=int(input('Enter Mobile Number'))
        email=input('Enter Email')
        pri=Contact(name,phone_number,email)
        con[rno]=pri
        out_file=open('contact.dat','wb')
        pickle.dump(con,out_file)
        out_file.close()
        print()
        print('=================Added Successfully=================')
        print()
    except:
        print('=======================Error========================')
        nf=int(input('The File is Missing Press 921 to Create a File\n'))
        if nf==921:
            new_file()

        
def view_contact():
    try:
        out_file=open('contact.dat','rb')
        con=pickle.load(out_file)
        out_file.close()
        rno=input("Enter unique key")
        print(con[rno])
    except:
        print('Enter Valid Key')
        view_contact()
    
def change_contact():
    out_file=open('contact.dat','rb')
    con=pickle.load(out_file)
    out_file.close()
    rno=input("Enter unique key")
    case=int(input('Press 1 to change Name\nPress 2 to change Phone\nPress 3 to change email id'))
    if case==1:
        val=input('Enter New Name')
        con[rno].set_name(val)
    if case==2:
        val=input('Enter New Phone Number')
        con[rno].set_phone(val)
    if case==3:
        val=input('Enter New Email ID')
        con[rno].set_email(val)
    out_file=open('contact.dat','wb')
    pickle.dump(con,out_file)
    out_file.close()
    print()
    print('================Changed Successfully================')
    print()
def view_all_contacts():
    out_file=open('contact.dat','rb')
    con=pickle.load(out_file)
    out_file.close()
    print()
    print('=============================Contacts==============================')
    print()
    print('Name\t\t\tPhone Number\t\tEmail Id')
    for p_id,p_info in con.items():
        if len(p_info.get_name())<=5:
            print(p_info.get_name()+'\t\t\t'+str(p_info.get_phone())+'\t'+p_info.get_email())
        elif 5<=len(p_info.get_name())<=14: 
            print(p_info.get_name()+'\t\t'+str(p_info.get_phone())+'\t'+p_info.get_email())
        else:
            print(p_info.get_name()+'\t'+str(p_info.get_phone())+'\t'+p_info.get_email())
    print('===================================================================')
    print()
def delete_contact():
    out_file=open('contact.dat','rb')
    con=pickle.load(out_file)
    out_file.close()
    rno=input("Enter unique key")
    del(con[rno])
    out_file=open('contact.dat','wb')
    pickle.dump(con,out_file)
    out_file.close()
    print()
    print('================Deleted Successfully================')
    print()
def main():
        print('======================Welcome=======================')
        choice=int(input("Press 1 to Search Contact\nPress 2 to Add Contact\nPress 3 to delete Contact\nPress 4 to Change Contact\nPress 5 to view all contacts\n====================================================\n                   Select Choices\n====================================================\n"))
        if choice==1:
            view_contact()
        elif choice==2:
            add_contact()
        elif choice==3:
            delete_contact()
        elif choice==4:
            change_contact()
        elif choice==5:
            view_all_contacts()
        exit=input("Press y to exit and n to continue")
        if exit=='n':
            main()
main()
        
