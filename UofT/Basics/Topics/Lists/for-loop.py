marks = [95,98,100]
print (marks[-1]) # -1 = last element
print(marks[0:2]) # 2 not included

for score in marks:
    print(score)


# Diiferent in built functions on list

marks.append(99) # to add something

print (marks)

marks.insert(0,97)

print (marks)

print(99 in marks) # to search if an element is poresent or not

print (len(marks)) # to calculate the length of the list