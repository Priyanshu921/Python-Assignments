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
c1=Contact('Priyanshu',1234567890,'priyanshu@patidar.com')
print(c1)
print('\n\nnow using the get methods')
print('name:-',c1.get_name())
print('Phone Number:-',c1.get_phone())
print('Email Id:-',c1.get_email())
c1.set_name('Priyanshu Patidar')
c1.set_phone(8871710658)
c1.set_email('patidar@priyanshu.com')
print('\n\nAfter changing the values using set Methods')
print(c1)
