"""
=========================================================
Project Name : File Manager (CRUD Operations)
Author       : Ajay Kumar
Course       : MCA (1st Year)
Language     : Python
Module Used  : pathlib

Description:
This is a menu-driven File Manager developed using Python.
The project performs CRUD (Create, Read, Update, Delete)
operations on files in the current working directory.

Features:
1. Create File
2. Read File
3. Update File
   - Rename File
   - Overwrite Content
   - Append Content
4. Delete File
5. Display Files and Folders

Note:
This project works only on the current directory.
It does not access or modify files outside the current folder.
=========================================================
"""

from pathlib import Path
from pathlib import Path

def read_fileand_folder():
    path = Path(".")
    for index, item in enumerate(path.iterdir(), start=1):
        print(f"{index} {item}")

def create_file():
    try:
        read_fileand_folder()
        name=input("Enter file name that you want to create:-").strip()
        p=Path(name)
        if p.exists():
            print(f"{p} is already exists")
        else:
            with open(p,'w') as file:
                data=input("What you want to write in this file:")
                file.write(data)
            print("file created successfully !")
    except Exception as e:
        print(f"error occured: {e}")

def read_file():
    try:
        read_fileand_folder()
        name=input("Which file you want to read:-  ").strip()
        p=Path(name)
        if p.exists() and p.is_file():
            with open(p,"r") as file:
                data=file.read()
                print(data)
        else:
            print("The file does not exist!")
    except Exception as e :
        print(f"An error occured as {e}")

def update_file():
    try:
        read_fileand_folder()
        name=input("which file you want to update:-").strip()
        p=Path(name)
        if p.exists() and p.is_file():
            print("press 1 for updating file name")
            print("press 2 for overwriting content on your file ")
            print("press 3 for appending some content on your file ")
            res=int(input("tell your choice:-"))
            if res == 2 or res == 3:
                with open(p, "r") as file:
                    data = file.read()

                print(f"\nCurrent Data:\n{data}")
            if res==1:
                name2=input("tell your new file name:-").strip()
                p2=Path(name2)
                if not p2.exists():
                    p.rename(p2)
                    print("file renamed successfully...")
                else:
                    print("file with this name already exists ")
            elif res==2:
                newdata=input("Enter new content to update:-")
                with open(p,"w") as file:
                    file.write(newdata)
                print("✅ File content overwritten successfully.")
            elif res==3:              
                newdata=input("Enter new content to update:-")
                with open(p,"a") as file:
                    file.write("\n"+newdata)
                print("✅ Content appended successfully.")
            else:
                print("Invalid choice !")

        else:
                print("file does not exists")
                return
    except Exception as e:
        print(f"an error occured: {e}")
        

def delete_file():
    try:
        read_fileand_folder()
        name=input("which file you want to delete:-").strip()
        p=Path(name)
        if p.exists() and p.is_file():
            confirm = input("Are you sure? (yes/no): ").lower()
            if confirm=="yes":
                p.unlink()
                print("\nFile deleted successfully.")
            else:
                print(" deleted operation cancelled.")
        else:
            print("\n this file name does not exists !")
    except Exception as e:
        print(f"an error occured: {e}")
while True:
    print("Press 1 for creating a file")
    print("Press 2 for reading a file")
    print("Press 3 for update a file")
    print("Press 4 for delete a file")
    print("Press 5 for Exit ")

    check=int(input("Please tell what you want:- "))
    if check == 1:
        create_file()
    elif check == 2:
        read_file()
    elif check == 3:
        update_file()
    elif check == 4:
        delete_file()
    elif check == 5:
        print("Thank you for using File Manager!")
        break
    else:
        print("please select valid options")
        