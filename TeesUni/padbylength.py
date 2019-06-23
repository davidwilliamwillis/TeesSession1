# Pad by length
# Pete 26/09/2017
# Saul 06/05/2019

age = 21
me = "My age is:"
pad_width = 10
pad_char = "."

pad_length = 4 - len(str(age))
pad_length = pad_width - len(str(age))

print(me, pad_length*("."), age)
output = me + (pad_length*".") + str(age)
print(output)

# Play with the commented lines above. What do you notice?
