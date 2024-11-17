print("Enter a character: ")
alphabet=input()
if len(alphabet)>1:
    print("ERROR! ALPHABET NOT DETECTED")
else:
    if alphabet>='a' and alphabet<='z':
        print(alphabet,"is an alphabet")
    elif alphabet>='A' and alphabet<='Z':
        print(alphabet,"is an alphabet")
    else:
        print(alphabet,"is not an alphabet")