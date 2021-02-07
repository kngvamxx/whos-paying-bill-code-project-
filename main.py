#whos paying bill
import random
#seed
create_seed=int(input("enter any number to create seed\n:"))
random.seed(create_seed)
#participant Name
participant=input("give me everybodys name separated by a comma\n:")
name=participant.split(",")

#random Gen 
count=len(name)
random_choice=random.randint(0,count-1)
random_name=name[random_choice]
print(f"{random_name} gonna pay the bill")