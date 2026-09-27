def get_detailsName(name):
    char1=name[0]
    char2=name[-1]
    char3=name[:3]
    return char1, char2, char3
user_name=input("Enter your name: ")
print(get_detailsName(user_name))    