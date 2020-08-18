__author__ = "Michael E Miles"
letters = "abcdefghijklmnopqrstuvwxyz"

#  With a negative step value make sure the start is greater than the stop value
backwards = letters[25:-27:-1]  # My solution
backwards1 = letters[25::-1]  # Also works
backwards2 = letters[::-1]  # As does this one (my favorite)
print(backwards)
print(backwards1)
print(backwards2)
print()

#  Challenge
print(letters[16:13:-1])
print(letters[4::-1])
print(letters[:17:-1])

print(letters[-4:])
print(letters[-1:])
print(letters[:1])
print(letters[0])
