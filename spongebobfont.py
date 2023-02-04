def sponge_bob(input_string):
    out=[]
    for pos in range(len(input_string)):
        if pos%2==0:
            out.append(input_string[pos].upper())
        else:
            out.append(input_string[pos].lower())
    return ''.join(out)

trial_string=input("Input a sentence")
new_string=[]
words=trial_string.split()
for word in words:
    each_word=sponge_bob(word)
    new_string.append(each_word)

print(' '.join(new_string))
