teams = ["arsenal","bournemouth", "chelsea", "dynamo kiev", 21,True, 3.40]
#print(type(teams[-2+1]))
#lengthOfNames = len(teams)
#print(lengthOfNames)
#print(teams[len(teams)-1])
#change item in a list
#teams[1] = "PSG"
print(teams)
#adding items to a list
#teams.append("Manchester City")
#teams = teams + list(["Bayern Munich"])
#teams = teams + ["Bayern Munich"]
#print(teams)
#print(len(teams))
#delete items from a list
output =teams.pop()
print(teams)
print(output)
# pop returns the value you are removing if you assign it to a variable
#it pops an item out of the list
# pop on default removes the last item on the list. removes using index number
#teams.remove(21)
#int(teams)
# remove needs the value of the item you want to remove
#slice
print(teams[:4])
