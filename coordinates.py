#A few lines using lists
#to locate coordinates

print("\n\n\n")
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]   
map = [row1, row2, row3]
print("Write two number from 1 to 3 to place an X in the coordinates")
print("the first number for columns, the second for rows\n")
print("          1     2     3\n")
print(f"    1   {row1}\n    2   {row2}\n    3   {row3}\n")

position = input("Where do you want to put the X?  ")

horizontal=int(position[0])
vertical=int(position[1])

if((horizontal<0 or horizontal>3) or (vertical<0 or vertical >3)):
  print("wrong numbers, run the program again")
else:
  selected_row=map[vertical-1]
  selected_row[horizontal-1]="X"

  print(f"\n        {row1}\n        {row2}\n        {row3}\n")