new_member = input("Enter a name of new member: ")

file = open("members.txt", "r")
members = file.readlines()
file.close()

members.append(new_member + "\n")

file = open("members.txt", "w")
members = file.writelines(members)
file.close()


