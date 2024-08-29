
text = input("Greeting: ")
words = text.strip().split()
if "hello" in words[0].lower():
    print("$0")
elif text[0].strip().lower() == "h":
    print("$20")
else:
    print("$100")