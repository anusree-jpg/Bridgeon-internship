sentence="python is easy to learn python is fast"
words=sentence.split()
frequency={}
for text in words:
 count=frequency.get(text,0)
 frequency[text]=count+1
print(frequency)