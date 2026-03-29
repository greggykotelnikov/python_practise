def convert(s):
    s = s.replace(":)", "🙂")
    s = s.replace(":(", "🙁")
    return s

def main():
    text = input("Greetings, dear friend! ")
    print(convert(text))

main()