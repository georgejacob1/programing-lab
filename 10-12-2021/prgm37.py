# 37.accept a list of words and return lenght of longest word using user defined function

def longest():
    text = input("please input a list of words to evaluate :")
    longest = 0
    for words in text.split():
        if len(words)>longest :
            longest = len(words)
    print("The longest word is",words,"with length",longest)
longest()
