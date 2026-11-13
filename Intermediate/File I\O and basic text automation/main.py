# with open("./Input/Letters/starting_letter.txt", "r") as f:
#     file = f.readlines()
#
#
# print(file[1:])

name_list = open("./Input/Names/invited_names.txt", "r")

letter = open("./Input/Letters/starting_letter.txt", "r")

letter_body = letter.read()


for i in name_list:

    y = i.rstrip("\n")

    with open("./Input/Letters/starting_letter.txt", "r") as f:
        file = f.readlines()
    letter_list = open(f"./Output/ReadyToSend/invite_{y}.txt", "w")
    First_line = (file[0])

    z = letter_body.replace("[name],", f"{y},")

    letter_list.write( f"{z}" )
