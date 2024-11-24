"""
    
"""
# import src.members.Member as Person
import src.DataManager 


def main() -> None:
    options_msg = """{0}
    0.Exit
    1.Add Member
    2.Update Member
    3.Remove Member
    4.Display Member
    5.....
    
{0}
    """.format('-'*50)
    print(options_msg)
    
    user_choice_input : str = input("Enter your choice : ")
    if(user_choice_input not in "012345"):
        print("Error [001]: Invalid input choice ")
    
    if(user_choice_input == "0") : 
        print("Sytem Exiting.....")

main()