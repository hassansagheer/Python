import re
email = input("What's your Email: ").strip()
if re.search(r".+@.+(\.edu)|(\.com)",email):
    print("Valid Email")
else:
    print("Invalid Email")