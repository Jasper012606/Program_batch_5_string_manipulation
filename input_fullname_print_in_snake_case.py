#input fullname
    #fix casing
    #replace space with underscore
full_name = input("Enter your full name: ").strip().lower().replace(" ", "_")
#print in snake case
print(full_name)