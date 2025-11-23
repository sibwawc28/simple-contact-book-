import json

while(1):
    print("Enter your choice ")
    print("1) Add a contact")
    print("2) Delete a contact")
    print("3) Update a contact")
    print("4) Search a contact")
    print("5) Display all contacts")
    print("6) Exit")
    choice=int(input())


    if(choice==1):
        name=input("Enter name ")
        phone=int(input("Enter phome number "))
        mail=input("Enter email ")

        newdata={"name":name, "phone":phone, "email":mail}

        with open(r"E:\python\python projects\contact book\contacts.json", "r") as f:
            contacts=json.load(f)

        contacts.append(newdata)

        #if i just dump 'newdata' without reading contacts, it'll overwrite, not append
        with open(r"E:\python\python projects\contact book\contacts.json", "w") as f:
            json.dump(contacts,f, indent=4)

        print("Contact added.")


    elif(choice==2):
        name=input("Enter name of contact to delete ")
    
        with open(r"E:\python\python projects\contact book\contacts.json", "r") as f:
            contacts=json.load(f)

        newcontact=[]

        for each in contacts:
            if (each["name"].lower()!= name.lower()):
                newcontact.append(each)

        with open(r"E:\python\python projects\contact book\contacts.json", "w") as f:
            json.dump(newcontact, f, indent=4)

        print("Contact deleted.")


    elif(choice==3):
        name=input("Enter updated name  ")
        phone=input("Enter updated phone number  ")
        mail=input("Enter updated mail  ")

        with open(r"E:\python\python projects\contact book\contacts.json", "r") as f:
            contacts=json.load(f)

        found=False
        for each in contacts:
            if (each["name"].lower()==name.lower()):
                found=True
                each["name"]=name
                each["phone"]=phone
                each["email"]=mail

        if found:
            with open(r"E:\python\python projects\contact book\contacts.json", "w") as f:
                json.dump(contacts, f, indent=4)
                print("Contact updated.")
        else:
            print("Contact not found.")


    
    elif(choice==4):
        name=input("Enter contact name whose details you want ")

        with open(r"E:\python\python projects\contact book\contacts.json", "r") as f:
            contacts=json.load(f)

        found=False
        for each in contacts:
            if (each["name"].lower()==name.lower()):
                print(each)
                found=True

        if not found:
            print("Contact not found.")


    elif(choice==5):
        print("Showing all contacts ")

        with open(r"E:\python\python projects\contact book\contacts.json", "r") as f:
            contacts=json.load(f)

        for each in contacts:
            print(each)


    elif(choice==6):
        exit()
    

    else:
        print("Invalid number")