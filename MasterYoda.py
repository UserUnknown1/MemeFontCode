def yodafication(str):
    lst=str.split()
    lst.reverse()
    return " ".join(lst)
    


greeting=input("Please enter your sentence")
yodasays=yodafication(greeting)
print(yodasays)
