#sets_4.py ev
alpha = {"a","b","c","d","e","f"}
bravo = {"z","y","x","w","v"}
charlie = alpha.union(bravo)
charlie.update("g","h","i","j","k")
for x in charlie:
	print(x," ",end="")
print()
#pop all the records
for i in range(len(charlie)):
	print("pop ",i," ",end="")
	thepop = charlie.pop()
	print (thepop)

"""
The union method combines two sets and
updates itself.
Notice the update function.
You can not pop from an empty setself.
The concept of "pop" is an important
function in data structures that resemble a stack.
"""
