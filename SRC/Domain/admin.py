import json
import os
path=r"D:\Restaurent Management system\Vikas_Restaurent_Management_system_Py\SRC\Database\menu.json"
def load_data(f):
    with open(path,'r')as f:
        return json.load(f)   
def view_menu():
    menu=load_data("menu.json")
    print("\n------Current Menu-------")
    print(json.dumps(menu,indent=4))
#view_menu()
paths=r"D:\Restaurent Management system\Vikas_Restaurent_Management_system_Py\SRC\Database\staff.json" 
def load_datas(f):
    with open(paths,'r')as f:
        return json.load(f)
def view_staff():
    staffs=load_datas("staff.json")
    print("\n------Staff list-------")
    print(json.dumps(staffs,indent=4))       
#view_staff()
def add_menu():
    path=r"D:\Restaurent Management system\Vikas_Restaurent_Management_system_Py\SRC\Database\menu.json"
    dish_name=input("Enter dish name you want to add in menu .")
    is_cambo=input("Is it a cambo (half_plate/full_plate)(yes/no):").lower()
    if is_cambo=="yes":
        half_plate_price=int(input("Enter halfplate price ."))
        full_plate_price=int(input("Enter full plate price ."))
        
    else:
        price=int(input("Enter the price of dish ."))
    new_dish={
        "dish_name":dish_name,
        "half_plate_price":half_plate_price,
        "full_plate_price":full_plate_price
    }    
    with open(path,'a')as f:
        json.dump(new_dish,f,indent=4)
    print("Sucess full dish added in menu .")
#add_menu()
path=r"D:\Restaurent Management system\Vikas_Restaurent_Management_system_Py\SRC\Database\menu.json"
def load_data(f):
    with open(path,'r')as f:
        return json.load(f)
def delete_id():
    delete_id=int(input("Enter the id you want to delete from menu ."))
    menus=load_data("menu.json")
    for menu in menus:
        if menu['id']==delete_id:
            menus.remove(menu)
            found=True
            break
    if found:
        with open(path,'w')as f:
            json.dump(menus,f,indent=4)
            print(f"Item deleted by id   {delete_id} deleted .")
    else:
        print(f"No item found with this id .")  
#delete_id()
def admin():
    while True:
        print(" 1.View Menu .")
        print(" 2.View Staff Details . ")
        print(" 3.Add in Menu .")
        print(" 4.Delete from Menu .")
        print(" 5 Exit .")
        choice=int(input("Enter your choice ."))
        if choice==1:
            view_menu()
        elif choice==2:
            view_staff()
        elif choice==3:
            add_menu()
        elif choice==4:
            delete_id()
        elif choice==5:
            break    
        else:
            print("Enter a valid choice .")
admin()                    



           

