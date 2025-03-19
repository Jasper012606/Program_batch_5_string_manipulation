#input full name
    #fix casing
    #remove spaces
full_name = input("Enter your full name: ").strip().title().replace(" ", "")
#print full name in pascal case
print(full_name)