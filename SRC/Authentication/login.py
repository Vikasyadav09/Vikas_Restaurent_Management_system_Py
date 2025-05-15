import json
import os
import sys
import getpass
sys.path.append(r"D:\Restaurent Management system\Vikas_Restaurent_Management_system_Py")
#from SRC.Domain.admin import admin
adminpath=r"D:\Restaurent Management system\Vikas_Restaurent_Management_system_Py\SRC\Database\admin.json"
staffpath=r"D:\Restaurent Management system\Vikas_Restaurent_Management_system_Py\SRC\Database\staff.json"
print("----------Vikas_Restaurent_Management_System--------------")
print("-------------------WELCOME--------------------------------")
def load_data(f):
    with open(adminpath,'r')as f:
        return json.load(f)
def load_datas(f):
    with open(staffpath,'r')as f:
        return json.load(f)
def signin():
    print("1.Admin login .")
    print("2.Staff login .")
    choice=int(input("Enter your choice ."))
    if choice==1:
        while True:

            email=input("Enter admin email .")
            password=getpass.getpass("Enter the password .")
            admins=load_data("admin.json")
            for admin in admins:
                if admin["email"]== email and admin["password"]==password:
                    print(f"\nWelcome as a Admin    {admin["name"]}")
                    from SRC.Domain.admin import admin
                    #admin()
                    return "admin"
                   
                else:
                    print("Enter correct email and password :")
                #email=input("Enter admin email .")
                #password=getpass.getpass("Enter the password .")
                
                    
            
                #return "admin"
            #print("invalid details .")
            
                    
    elif choice==2:

        email=input("Enter Staff email .")
        password=getpass.getpass("Enter your password .")
        staffs=load_datas("staff.json")
        for staff in staffs:
            if staff["email"]==email and staff["password"]==password:
                print(f"\nWelcome Staff    {staff['name']}")
                return "staff"
            print("Invalid Staff details .")
        print("Invalid choice .")
    #signin()           
#elif choice==2:
def signup():
    path=r"D:\Restaurent Management system\Vikas_Restaurent_Management_system_Py\SRC\Database\signup.json"
    name=input("Enter your name .")
    adress=input("Enter your adress .")
    email=input("Enter your email .")
    password=getpass.getpass("Enter your password .")
    new_user=[{
        "name":name,
        "email":email,
        "password":password,
        "adress":adress
        }]
    with open(path,'a') as f:
        json.dump( new_user,f,indent=4)
        print("Signup complete sucessfully .")
        from SRC.Domain.table_management import main_menu
        from SRC.Domain.food_odering import take_order   


    #signup()
def main():
        try:
            while True:
                print("---Login------")
                print("1.Signin .")
                print("2. Signup .") 
                print("3 . Exit .")   
                choice=int(input("Enter your choice ."))
                if choice==1:
                    signin()
                elif choice==2:
                    signup()
                elif choice==3:
                    print("Exiting program .")
                    break
        except Exception as e:
            print("try again after some time network problem .")      

    
           