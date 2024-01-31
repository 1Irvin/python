print("How many siblings are there?")
siblings=int(input())
print("How many popsicles are in the box?")
popsicles=int(input())
if (popsicles % siblings)== 0:
   print("Give away")
else:
    print("Eat them yourself")
