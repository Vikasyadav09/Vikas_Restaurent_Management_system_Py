import json
import os
adminpath=r"D:\Restaurent Management system\Vikas_Restaurent_Management_system_Py\SRC\Database\admin.json"
staffpath=r"D:\Restaurent Management system\Vikas_Restaurent_Management_system_Py\SRC\Database\staff.json"
def load_data(f):
    with open(adminpath,'r')as f:
        return json.load(f)
def load_datas(f):
    with open(staffpath,'r')as f:
        return json.load(f)
print("1.signin .")
print("2. signup .")    
choice=int(input("Enter your choice ."))
if choice==1:
                
    def signin():
        print("1.Admin login .")
        print("2.Staff login .")
        choice=int(input("Enter your choice ."))
        if choice==1:
            email=input("Enter admin email .")
            password=int(input("Enter the password ."))
            admins=load_data("admin.json")
            for admin in admins:
                if admin["email"]== email and admin["password"]==password:
                    print(f"\nWelcome Admin    {admin["name"]}")
                    return "admin"
                print("invalid details .")    
        elif choice==2:

            email=input("Enter Staff email .")
            password=int(input("Enter your password ."))
            staffs=load_datas("staff.json")
            for staff in staffs:
                if staff["email"]==email and staff["password"]==password:
                    print(f"\nWelcome Staff    {staff['name']}")
                    return "staff"
            print("Invalid Staff details .")
        print("Invalid choice .")
    signin()           
elif choice==2:
    def signup():
        path=r"D:\Restaurent Management system\Vikas_Restaurent_Management_system_Py\SRC\Database\signup.json"
        name=input("Enter your name .")
        email=input("Enter your email .")
        password=int(input("Enter your password ."))
        new_user=[{
            "name":name,
            "email":email,
            "password":password
        }]
        with open(path,'a') as f:
            json.dump( new_user,f,indent=4)
        print("Signup complete sucessfully .")    


    signup()