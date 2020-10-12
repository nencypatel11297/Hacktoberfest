data = {}
def newWord():
    x = input("Write the word: ")
    x = x.lower()
    y = input("Meaning of the word: ")
    data[x] = y
def accessWord():
    p = input("Write the word: ")
    p = p.lower()
    try:
        f = data[p]
        print(f)
    except Exception as e:
        print("No Such Word Found")
while True:
    print("\nYour personal dictionary.\nEnter 'n' To add new word.\nEnter 'a' to access your word.\nEnter 'q' to exit")
    d = input("Enter your choice: ")
    if d == 'n' or d == 'N':
        newWord()
    elif d == 'a' or d == 'A':
        accessWord()
    elif d == 'q' or d == 'Q':
        break
    else:
        print("Invalid choice.")
