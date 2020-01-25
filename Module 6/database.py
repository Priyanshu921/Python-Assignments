import pickle
database={'office':{'medical':[{'room number':100,'use':'reception','sq_ft':50,'price':75},
                               {'room number':101,'use':'waiting','sq_ft':250,'price':75},
                               {'room number':102,'use':'examination','sq_ft':125,'price':150},
                               {'room number':103,'use':'examination','sq_ft':125,'price':150},
                               {'room number':104,'use':'office','sq_ft':150,'price':100}],
                                'parking':{'location':'premium','style':'covered','price':750}}}
def neFi():
    out_file=open('database.dat','wb')
    pickle.dump(database,out_file)
    out_file.close()
    print("-------------------File Created Successfully---------------------")
def change_detail():
    try:
        out_file=open('database.dat','rb')
        database1=pickle.load(out_file)
        out_file.close()
        rno=int(input('Enter the room number'))
        det=input('Enter the Detail to be changed')
        newp=int(input('Enter the new vlaue of detail'))
        for i in (database1['office']['medical']):
         if i['room number']==rno:
             i[det]=newp
        out_file=open('database.dat','wb')
        pickle.dump(database1,out_file)
        out_file.close()
        print("--------------------Changed Successfully----------------------")
    except:
        print('=======================Error========================')
        nf=int(input('The File is Missing Press 921 to Create a File\n'))
        if nf==921:
            neFi()
def add_room():
    out_file=open('database.dat','rb')
    database1=pickle.load(out_file)
    out_file.close()
    room_number=int(input('Enter the room Number'))
    use=input('Enter the room use')
    sq_ft=int(input('Enter the room size'))
    price=int(input('Enter the room Price'))
    database1['office']['medical'].append({'room number':room_number,'use':use,'sq_ft':sq_ft,'price':price})
    out_file=open('database.dat','wb')
    pickle.dump(database1,out_file)
    out_file.close()
    print("--------------------Room Added----------------------")
def view_room():
    out_file=open('database.dat','rb')
    database1=pickle.load(out_file)
    out_file.close()
    rno=int(input('Enter the Room Number'))
    print()
    print()
    print('Room Number \t use   \t\t Room Area \t Price')
    for i in database1['office']['medical']:
        if i['room number']==rno:
            print(i['room number'],"\t\t",i['use'],"\t",i['sq_ft'],"\t\t",i['price'],"\t")
    print()
    print()
def delete_room():
    out_file=open('database.dat','rb')
    database1=pickle.load(out_file)
    out_file.close()
    rno=int(input('Enter the room number'))
    for i in (database1['office']['medical']):
     if i['room number']==rno:
         database1['office']['medical'].remove(i)
    out_file=open('database.dat','wb')
    pickle.dump(database1,out_file)
    out_file.close()
def view_offices():
    out_file=open('database.dat','rb')
    database1=pickle.load(out_file)
    out_file.close()
    print()
    print()
    offname=input("Enter the office name")
    print("--------------------"+offname+"----------------------")
    if offname=='medical':
        print('Room Number \t use   \t\t Room Area \t Price')
        for i in database1['office']['medical']:
            print()
            print(i['room number'],"\t\t",i['use'],"\t",i['sq_ft'],"\t\t",i['price'],"\t")
    else:
        print("location \t style \t\t price")
        print(database1['office'][offname]['location'],"\t",database1['office'][offname]['style'],"\t",database1['office'][offname]['price'],"\t")
    print()
    print()
def add_office():
    out_file=open('database.dat','rb')
    database1=pickle.load(out_file)
    out_file.close()
    office_name=input("Enter name of the office")
    location=input("Enter the location")
    style=input("Enter the Style")
    price=int(input("Enter the price"))
    database1['office'][office_name]={'location':location,'style':style,'price':price}
    out_file=open('database.dat','wb')
    pickle.dump(database1,out_file)
    out_file.close()
    print("--------------------Office Added----------------------")
def remove_office():
    out_file=open('database.dat','rb')
    database1=pickle.load(out_file)
    out_file.close()
    offname=input("Enter the office name to be deleted")
    del(database1['office'][offname])
    out_file=open('database.dat','wb')
    pickle.dump(database1,out_file)
    out_file.close()
    print("--------------------Office Removed----------------------")
def speci_det():
    out_file=open('database.dat','rb')
    database1=pickle.load(out_file)
    out_file.close()
    off=input('Which office detail you want?')
    if off=='medical':
        rno=int(input("Enter the room Number"))
        detai=input("Which detail you want to use")
        for i in database1['office']['medical']:
            if i['room number']==rno:
                print(i[detai])
    else:
        detai=input("Which detail you want to use")
        print(database1['office'][off][detai])
def pubg():
    print("----------------------Welcome-----------------------")
    choice=int(input(" press 1 to change any detail of the room\n press 2 to add another room \n press 3 to view medical room \n press 4 to delete the room \n press 5 to view offices \n press 6 to add an office \n press 7 to delete an office \n press 8 view specific Detail of the room \n---------------------------------------------------- \n---------------------------------------------------- \n"))
    print("----------------------------------------------------")
    if(choice==1):
        change_detail()
    elif choice==2:
        add_room()
    elif choice==3:
         view_room()
    elif choice==4:
        delete_room()
    elif choice==5:
        view_offices()
    elif choice==6:
        add_office()
    elif choice==7:
        remove_office()
    elif choice==8:
        speci_det()
    elif choice==9:
        neFi()

        
    exit=input("Press y to exit and n to continue")
    if exit=='n':
        pubg()
        
pubg()
