football="goat.txt"
with open(football,"w") as file:
    file.write("the greatest of all time is lionel messi.\n")
    file.write("cristiano ronaldo is the second best player after messi.\n")
    file.write("pele is nowhere near to messi and ronaldo")
with open(football,"r") as file:
    a=file.read()
print(a)
