from pickle import load,dump    #pickle acts a medium to transferbetween your file and your code
from os import remove,rename
import os
import time
print()
print()
print() #U can replace these print statements using \n
print("~"*70)
print()
print()
print("\t\t\t WELCOME TO SANKETH'S LIBRARY \t\t\t")
print("\t\t\t *=*=*=*=*=*=*=*=*=*=*=*=*=*=*\t\t\t")
print()
print()
print()
print()
print()
print()
print("\t\t\t\t\tPROJECT DONE BY:")
print()
print("\t\t\t\t\tSANKETH KULAL")
print()
print("\t\t\t\t");
print()
print("~"*70)
print()
a=input("PRESS ENTER TO CONTINUE:")
#every a-z or  A-Z or 0-9everything has  a ASCII value,,is alwaysa number,enter does not have  an ascii value,insteadit has "\n"
a=str(a)
if a.isalpha():
    pass
class book:
    def __init__(self,bno="",bname="",auname=""):#initialize values and  variables present insidethis  class
        self.bno=bno
        self.bname=bname
        self.auname=auname

    def create_Book(self):
        print()
        print("\t\t\tCreating Book Record\t\t\t")
        print("\t\t\t====================\t\t\t")
        print()
        self.bno=input("\tEnter Book Number:")
        print()
        self.bname=input("\tEnter Name of the Book:")
        print()
        self.auname=input("\tEnter Name of the Author:")
        print()
        print()
        print("\t\t\tBook Created..!!\t\t\t")
        
    def show_Book(self):
        print()
        print()
        print("\t\tBook Number:",self.bno)
        print()
        print("\t\tBook Name:",self.bname)
        print()
        print("\t\tAuthor Name:",self.auname)
        print()
        print()

    def modify_Book(self):
        print()
        print()
        print("\t\tBook No.:",self.bno)
        print()
        self.bname=input("\t\tEnter New Book Name:")
        print()
        self.auname=input("\t\tEnter New Author Name:")
        print()
        print()
        print("\t\tBook Modified..!!")
        print()

    def ret_Bno(self):
        return(self.bno)

    def report_Book(self):
        print(self.bno,self.bname,self.auname)

class Student:
    def __init__(self,admno="",name="",stbno="",token=0): #init Constructor
        self.admno=admno
        self.name=name
        self.stbno=stbno
        self.token=token

    def create_Stud(self):
        print()
        print("\t\t\tCreating Student Record\t\t\t")
        print("\t\t\t=======================\t\t\t")
        print()
        self.admno=input("\t\tEnter Admission Number:")
        print()
        self.name=input("\t\tEnter Name of the Student:")
        print()
        self.stbno=""
        self.token=0
        print()
        print()
        print("\t\t\tStudent Record Created..!!\t\t\t")
        print()
        print("#"*70)
        print()

    def show_Stud(self):
        print()
        print()
        print("\tAdmission No.:",self.admno)
        print()
        print("\tName:",self.name)
        print()
        print("\tStbno:",self.stbno)
        print()
        print()

    def display_Stud(self):
        print()
        print("\tAdmission Number of the Student is:",self.admno)
        print()
        print("\tName of the Student is:",self.name)
        if(self.token==1):
            print("\tBook Number is:",self.stbno)
    def modify_Stud(self):
        print()
        print("\tAdmission No.:",self.admno)
        print()
        self.name=input("\tNew Student Name:")
        print()
        print("\t\tStudent's Name Modified!!")

    def ret_Admno(self):
        return self.admno

    def ret_Stbno(self):
        return self.stbno

    def ret_token(self):
        return self.token

    def add_token(self):
        self.token=1

    def reset_token(self):
        self.token=0

    def get_stbno(self,t):
        self.stbno=t
        
    def report_Stud(self):
        print(self.admno,self.name,self.token)

def writebook():
    ch="Y"
    fp=open("book1.dat","ab")
    while ch=="Y":
        bk.create_Book()
        dump(bk,fp)
        print()
        ch=input("\t\tDo you Want to Continue??<y/n>:")
        print()
        print("#"*70)
        print()
        ch=ch.upper()
def writestudent():
    ch="Y"
    fp=open("student1.dat","ab")
    while ch=="Y":
        st.create_Stud()
        dump(st,fp)
        ch=input("\t\tDo You Want to Continue <y/n>:")
        ch=ch.upper()
        print()
def display_alls():
    fin=open("student1.dat","rb") #Your code and the created student and book file should all be in the same folder
    if not(fin):
        print("\t\tFile is Not Found...")
    else:
        try:
            while True:
                print()
                st=load(fin)
                st.show_Stud()
        except EOFError:
            pass
    fin.close()

def display_allb():
    fin=open("book1.dat","rb")
    if not(fin): #Whether file existsor not
        print()
        print()
        print("Book File is Not Found...")
    else:
        try:
            while True:
                bk=load(fin)
                bk.show_Book()
        except EOFError:
            pass
    fin.close()

def display_spb(no):
    flag=0 # Here we use flag variable to check if book is found or not
    fin=open("book1.dat","rb")
    try:
        while True:
            bk=load(fin)
            if(bk.ret_Bno()==no):
                bk.show_Book()
                flag=1
    except EOFError:
        pass
    fin.close()
    if flag==0:
        print()
        print()
        print("\t\t\tBOOK NOT PRESENT..!!")

def display_sps(n): #Value that was in ad will now be in "n",so now n is my admission number of student to be displayed
    flag=0 #flag variable is  used to check whether astudent isfound or not
    fin=open("student1.dat","rb")
    try:
        while True:
            st=load(fin)
            if(st.ret_Admno()==n):
                st.show_Stud()
                flag=1
    except EOFError:
        pass
    fin.close()
    if flag==0:
        print()
        print("\t\t\tSTUDENT NOT PRESENT..!!")
def modify_bookrecord():
    found=0
    print()
    print()
    print("\t\t\tModify Book")
    print()
    print()
    n=input("\t\tEnter the Book Number to be Modified:")
    print()
    fin=open("book1.dat","rb")
    fout=open("temp.dat","wb")
    try:
        while True:
            bk=load(fin)
            if bk.ret_Bno()==n:
                print()
                print("\t\t\tBook Details\t\t\t")
                print("\t\t\t============\t\t\t")
                bk.show_Book()
                print()
                print("\t\tEnter New Details")
                print()
                print()
                bk.modify_Book()
                dump(bk,fout)
                found=1
            else:
                dump(bk,fout)
    except EOFError:
        pass
    if found==0:
        print("\t\t\tBook Not Present..")
    fin.close()
    fout.close()
    remove("book1.dat")
    rename("temp.dat","book1.dat")

def modify_student_record():
    found=0
    print()
    print("\t\t\tModify Student Record\t\t\t")
    print("\t\t\t=====================\t\t\t")
    print()
    print()
    n=input("\t\tEnter Students Admission Number to be Modified:")
    print()
    fin=open("student1.dat","rb")
    fout=open("temp.dat","wb")
    try:
        while True:
            st=load(fin)
            if st.ret_Admno()==n:
                print()
                print("\t\t\tSTUDENT DETAILS")
                print("\t\t\t===============")
                st.show_Stud()
                print()
                print("\t\t\tEnter New Student Details:")
                st.modify_Stud()
                dump(st,fout)
                found=1
            else:
                dump(st,fout)
    except EOFError:
        pass
    if found==0:
        print("\t\t\tSTUDENT NOT PRESENT..")
    fin.close()
    fout.close()
    remove("student1.dat")
    rename("temp.dat","student1.dat")

def del_stud():
    flag=0
    print()
    print()
    n=input("\t\tEnter Admission Number to be Deleted:")
    print()
    fin=open("student1.dat","rb")
    fout=open("temp.dat","wb")
    try:
        while True:
            st=load(fin)
            if st.ret_Admno()!=n:
                dump(st,fout)
            else:
                flag=1
    except EOFError:
        pass
    fin.close()
    fout.close()
    remove("student1.dat")
    rename("temp.dat","student1.dat")
    if flag==1:
        print()
        print("\t\t\tRECORD DELETED..!!")
    else:
        print()
        print("\\t\t\tSORRY..!! RECORD DOES NOT EXIST..!!...")
def del_book():
    flag=0
    print()
    print()
    n=input("\t \t Enter Book No to be Deleted:")
    print()
    fin=open("book1.dat","rb")
    fout=open("temp.dat","wb")
    try:
        while True:
            bk=load(fin)
            if bk.ret_Bno()!=n:
                dump(bk,fout)
            else:
                flag=1 #flag=1 here means that book was found and successfully deleted
    except EOFError:
        pass
    fin.close()
    fout.close()
    remove("book1.dat")
    rename("temp.dat","book1.dat")
    if flag==1:
        print ("\t\t\t Record Deleted")
    else:
        print ("\t\t\t SORRY..!! RECORD NOT PRESENT..")


def book_issue():
    sn=" " #Student No.
    bn=" " #Book No.
    found=0 #becomes 1 when student is found
    flag=0 #become 1 when the book is found
    print()
    print()
    print("\t\t\t BOOK ISSUE \t\t\t")
    print("\t\t\t ========== \t\t\t")
    print()
    print()
    sn=input("\t \t Enter the Student's Admission Number:")
    print()
    fin1=open("book1.dat","rb") #pointer to BOOK1.dat
    fin2=open("student1.dat","rb") #pointer to Student.dat
    fout=open("temp.dat","wb") #pointer to temp.dat
    try:
        while True:
            st=load(fin2) #object for student class
            if (st.ret_Admno()==sn):
                st.show_Stud()
                found=1 #becomes 1 when the student is found
                if st.ret_token()==0:
                    bn=input("\t \t Enter Book Number:")
                    try:
                        while True:
                            bk=load(fin1) #object for book class
                            if bk.ret_Bno()==bn:
                                bk.show_Book()
                                flag=1 #becomes 1 when the book is found
                                st.add_token()
                                st.get_stbno(bk.ret_Bno()) #book number issued will be added to stbno for the particular student
                                dump(st,fout)
                                #os.system("cls")
                                print()
                                print()
                                print ("\t \t \t Book Issued Successfully \t \t \t")
                                print()
                                print ("\t PLEASE NOTE : Write the current date in backside of your book ")
                                print ("\t\t and submit within 15 days")
                                print ()
                                print ("\t\t Fine Rs.20 for each day after 15 days period..!!")
                                print()
                                
                    except EOFError:
                        pass
                else:
                    print("\t You have not returned the last book..")
    
    except EOFError:
        pass
    if(flag==0):
        print ("\t \t \t No Such Book Present !!!")
    if(found==0):
        print ("\t \t \t No Such Student Exists !!!")
    fin1.close()
    fin2.close()
    fout.close()
    remove("student1.dat")
    rename("temp.dat","student1.dat")
            
def book_deposit():
    print()
    print()
    print()
    print("\t\t\t BOOK DEPOSITING")
    print("\t\t\t ===============")
    sn=" "
    found=0
    flag=0
    day=0
    fine=0
    print()
    print()
    sn=input("\t \t Enter Students Admission Number:")
    print()
    fin1=open("student1.dat","rb")
    fin2=open("book1.dat","rb")
    fout=open("temp.dat","wb")
    try:
        while True:
            st=load(fin1)
            if st.ret_Admno()==sn:
                found=1
                print()
                print ("\t Student Token Number",st.ret_token())
                if st.ret_token()==1:
                    try:
                        while True:
                            bk=load(fin2)
                            if bk.ret_Bno()==st.ret_Stbno():
                                bk.show_Book()
                                flag=1
                                print()
                                days=int(input("\t Book Deposited In no. of days:"))
                                if days>=15:
                                    fine=(days-15)*20
                                    print()
                                    print ("\t Fine : Rs.",fine)
                                st.reset_token()
                                st.get_stbno(0)
                                st.show_Stud()
                                dump(st,fout)
                                print()
                                print ("\t \t BOOK DEPOSITED !!!")
                  
                            
                    except EOFError:
                        pass
                else:
                    print()
                    print("\t \t You have not issued the  book..")
        
               
    except EOFError:
        pass
    if(found==0):
        print()
        print("\t No Such Student Exists")
    fin1.close()
    fin2.close()
    fout.close()
    remove("student1.dat")
    rename("temp.dat","student1.dat")
    
bk=book() # we have 2 important classes also, one is student and the other is book
st=Student()
'''
classes is a combination of variables and methods/functions
Objects used to call functions
'''
def adminmenu():
    ch="Y"
    while ch=="Y":
        print()
        print()
        print ("\t \t \t ADMINISTRATION MENU \t \t \t")
        print ("\t \t \t =================== \t \t \t")
        print()
        print()
        print ("\t 1. CREATE STUDENT RECORD")
        print()
        print ("\t 2. DISPLAY ALL STUDENTS RECORD")
        print()
        print ("\t 3. DISPLAY SPECIFIC STUDENT RECORD")
        print()
        print ("\t 4. MODIFY STUDENT RECORD")
        print()
        print ("\t 5. DELETE STUDENT RECORD")
        print()
        print ("\t 6. CREATE BOOK")
        print()
        print ("\t 7. DISPLAY ALL BOOKS")
        print()
        print ("\t 8. DISPLAY SPECIFIC BOOK")
        print()
        print ("\t 9. MODIFY BOOK")
        print()
        print ("\t 10.DELETE BOOK RECORD")
        print()
        ch1=int(input("\t \t Enter Your Choice:"))
        print()
        #os.system("cls")
        if ch1==1:
            writestudent()
        elif ch1==2:
            display_alls()
        elif ch1==3:
            print()
            print()
            ad=input("\t \t Enter Student's Admno to be Displayed:")
            display_sps(ad)
        elif ch1==4:
            modify_student_record()
        elif ch1==5:
            del_stud()
        elif ch1==6:
            writebook()
        elif ch1==7:
            display_allb()
        elif ch1==8:
            print()
            print()
            bn=input("\t \t ENTER BOOK NUMBER TO BE DISPLAYED:")
            display_spb(bn)
        elif ch1==9:
            modify_bookrecord()
        elif ch1==10:
            del_book()
        print()
        ch=input("\t \t Do you want Continue with ADMINMENU<y/n>:")
        ch=ch.upper()
        print()
        if ch=="Y":
            continue
        else:
            mainmenu()
def mainmenu():  #IN C PROG, to define a function u would write void/int/float funcname {body}
    ch="Y" #ch is also known as choice
    while ch=="Y":
        print()
        print()
        print ("\t \t \t MAIN MENU \t \t \t")
        print ("\t \t \t ========= \t \t \t")
        print()
        print ("\t 1. BOOK ISSUE")
        print()
        print ("\t 2. BOOK DEPOSIT")
        print()
        print ("\t 3. ADMINISTRATION MENU")
        print()
        print ("\t 4. EXIT")
        print()
        ch1=int(input("\t \t Enter Your Choice:"))
        print()
        print ("\t \t Loading ....")
        time.sleep(5)
        #os.system("cls")
        if ch1==1:
            book_issue()
        elif ch1==2:
            book_deposit()
        elif ch1==3:
            adminmenu()
        else:
            exit(0)
        print()
        ch=input("\t \t \t Do You Want to Continue with mainmenu <y/n>:")
        ch=ch.upper()
        if  ch=="N":
            break
        print()
        print()
        print ("\t \t Loading...")
        time.sleep(30)
        #os.system("cls")
        
#os.system("cls")
mainmenu()
              

