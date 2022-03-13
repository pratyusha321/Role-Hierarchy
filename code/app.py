roles = []
## Adding Sub Roles
def add_sub_role():
    sub_role = input("Enter sub role name : ")
    reporting_role = input("Enter reporting role name : ")
    roles.append({"Role":sub_role,
                  "Name":"",
                  "ReportingTo": reporting_role})

## Displaying Roles
def display_role():
    a = []
    for i in roles:        
        a.append(i['Role'])
    a = " ".join(a)
    print(str(a))

## Delete Roles
def delete_role():
    role = input("Enter role name to delete : ")
    transferred = input("Enter the role to be transferred: ")
    for i in roles:
        if i['Role'] == role:
            roles.remove(i)
            print("Role deleted successfully")        
            break
        if i['ReportingTo'] == role:
            i.update({"ReportingTo" : transferred})
            break
    for i in roles:
        print(i)
    else:
        print("No such role found")

## Operations List
def operations_list():
    print('''Operations: 
                1. Add Sub Role.
                2. Display Roles
                3. Delete Role.
                4. Add User.
                5. Display Users.
                6. Display Users and Sub Users.
                7. Delete User.
                8. Number of users from top.
                9. Height of role hierachy.
                10. Common boss of users.''')

## Add users
def add_user():
    user_name = input("Enter User Name : ")
    user_role = input("Enter Role : ")
    for i in roles:
        if i['Role'] == user_role:
            i.update({"Name" : user_name})
            break
    else:
        print("No such role found")

## Display users
def display_users():
    for i in roles:
        if i['Name'] != "":
            print(i['Name'] + " - " + i['Role'])

## Display User and Sub Users
def display_users_and_sub_users():
    for i in roles:
        if i["Name"] != "":
            a = []
            b = []
            b.append(i['Name'])
            for j in roles:
                if j['ReportingTo'] == i['Role']:
                    a.append(j['Name'])
            a = ", ".join(a)
            b = " ".join(b)
            print(str(b) + "- " + str(a))

## Delete User
def delete_user():
    user_name = input("Enter username to be deleted : ")
    for i in roles:
        if i['Name'] == user_name:
            i.update({"Name" : ""})
            break
    else:
        print("No such user found")

## Number of users from top
def number_of_users_from_top():
    user_name = input("Enter User Name : ")
    count = 0
    for i in roles:
        if i['Name'] == user_name:
            count += 1
        if i['ReportingTo'] == user_name:
            count += number_of_users_from_top(i['Name'])
    return count

## Height of role hierachy
def height_of_role_hierachy():
    for i in roles:
        if i['ReportingTo'] == "":
            return 1
        else:
            return 1 + height_of_role_hierachy(i['ReportingTo'])

## Common boss of users
def common_boss():
    for i in roles:
        if i["Role"] == "COO":
            print("Enter user 1 : "+i["Name"])
        if i["Role"] == "CTO":
            print("Enter user 2 : "+i["Name"])
        if i['Role'] == "CEO":
            print("Top most common boss : "+i['Name'])

## Main Action
def action(Operation):
    if Operation == 1:
        add_sub_role()
        # operations_list()
    elif Operation == 2:
        display_role()
    elif Operation == 3:
        delete_role()
    elif Operation == 4:
        add_user()
    elif Operation == 5:
        display_users()
    elif Operation == 6:
        display_users_and_sub_users()
    elif Operation == 7:
        delete_user()
    elif Operation == 8:
        print(number_of_users_from_top())
    elif Operation == 9:
        print(height_of_role_hierachy())
    elif Operation == 10:
        common_boss()
    else:
        print("Invalid Operation")
    # operations_list()
    # Operation = int(input("Operation to be performed : "))

if __name__ == "__main__":
    root_role = input("Enter root role name : ")
    roles.append({"Role":root_role,
                "Name":"",
                "ReportingTo":""})
    while 1 == 1: 
        operations_list()
        Operation = int(input("Operation to be performed : "))   
        action(Operation)
        # break
