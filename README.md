# Role-Hierarchy

Role Hierarchy app helps to create and maintains roles and its hierarchy.
![alt text](https://github.com/pratyusha321/Role-Hierarchy/blob/main/images/Flow.png)

  
 Whole program is created in Python and it's developed in pure python with no libraries.
##  Prerequisite to run Python Code:
  1. Python 3.x version
  
 ## Run the Code
  Command to run the code is : 
  
                        python app.py
  
 ## Process Steps
  1. The program starts with creating a Root role i.e. CEO
  2. And it navigates to multiple Operations to select:
  
                1. Add Sub Role.  
                2. Display Roles.  
                3. Delete Role.  
                4. Add User.  
                5. Display Users.
                6. Display Users and Sub Users.
                7. Delete User.
                8. Number of users from top.
                9. Height of role hierachy.
                10. Common boss of users.
  3. By selecting Operations "1. Add Sub Role", we can add the Sub Role and it's reporting to details.
  
      For Example: 
  
                   Enter sub role name : CTO  
                   Enter reporting to role name : CEO
  4. After adding all corresponding roles in hierarchy to view, Operations "2. Display Roles."
      
      For Example:
                  
                  CEO, COO, CTO, Sr Product Eng Manager, Sr Product Marketing Manager, Director of Technology.
  5. The Next option is to delete the created roles by selecting operation "3. Delete Role."
  6. After creation of roles, the next operation is to create Users i.e. "4. Add User." After the User name, that user need to assign with the defined Role.
      For Example: 
    
                    Enter User Name : Kenny
                    Enter Role : Director of Technology
  7. The Next operation is to display the created User Name and that corresponding Role assigned.
      For Example:
                  
                    Tyson - CEO
                    Ray - COO
                    Max - Director of Technology
                    Kenny - Director of Technology
                    Will - Sr Product Eng Manager
  8. The Next step is to Display the User Name and their Reporting Users list and operation is "6. Display Users and Sub Users."
      For Example:
                  
                    Tyson - Ray, Max, Kenny, Will
                    Ray - Will
                    Max -
                    Kenny -
                    Will -
  9. The Next step is to delete the created Users. And it's operation is "7. Delete User."
  10. The Next step is to show the number of user from the top for a given User and it's operation is "8. Number of users from top."
       For Example:
                  
                    Enter user name : Kenny
                    Number of users from top : 1
  11. The next step is to show the Height of the role hierarchy.
      For Example:
  
                  height - 3
  12. The Final step is to display the common boss for the users and it's operation is "10. Common boss of users."
      For Example:

                  Enter user 1 : Will
                  Enter user 2 : Kenny
                  Top most common boss : Tyson
