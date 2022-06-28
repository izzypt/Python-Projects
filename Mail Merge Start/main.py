#TO DO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

PLACEHOLDER = "[name]"


#################
 # OPEN FILES
#################
invited_people_file = open("./input/Names/invited_names.txt")
invite_file = open("./Input/Letters/starting_letter.txt")

###############################
 # READ THE FILE || FILE LINES
###############################
invited_people_list = invited_people_file.readlines()
invite = invite_file.read()
i = 0

#########################################
 # CREATE A LIST WITH ALL INVITED PEOPLE
#########################################
for line in invited_people_list:
    invited_people_list[i] = line.replace("\n", "")
    i += 1
    
############################################
# CREATE A NEW FILE FOR EACH PEOPLE INVITED
############################################
for guest in invited_people_list:
    with open(f"./Output/ReadyToSend/{guest}.txt", mode="w") as file:
        new_invite = invite.replace(PLACEHOLDER, guest)
        file.write(new_invite)

###############
 # CLOSE FILES
###############
invited_people_file.close()
invite_file.close()