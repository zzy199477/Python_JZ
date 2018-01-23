yours=['Yale','MIT','Berkeley']
mine=['UCLA','CMU','Cornell']

ours1=yours+mine

ours2=[]
ours2.append(yours)
ours2.append(mine)

print(ours1)
print(ours2)

#The difference between the printed result of ours1 and ours 2 is that ours1 has all the schools combined in one list,
# while ours2 has the schools in one list with with two seperate sub-lists, with mine appended on the right side.


yours[1]='Harvard'

print(ours1)
print(ours2)

#The reason ours1 does not change but ours2 changes is that ours1 is a new variable and ours2 refers to two existing variables.
#changing yours will not make a change in this new variable.