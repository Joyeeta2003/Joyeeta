text="Hii, %$#i am #$%%^joyeet%&*a"
print("the ariginal str=",text)
punc="!@#$%^&*()_~`,"
for ele in text:
  if ele in punc:
    text=text.replace(ele,"")
print("the string after removeing punctuation:",text)
