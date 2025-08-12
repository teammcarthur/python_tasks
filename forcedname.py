def force_name():
    while True:#infinite loop, looking for name with 2-10 characters
        text=str(input("Please type in name"))
        if len(text) >2 and len(text) <10 and text.isalpha():
            print(text)
            break #you can only break loop if statement is true
        else:
            print("ERROR - please type valid name")
            return text #returns valid name back to variable that called the function

#main program
first_name=force_name()
middle_name=force_name()
last_name=force_name()
print("Name {} {} {}".format(first_name,middle_name,last_name))