import pyshorteners

# ask user to input a link
link = input("\nLink : ")

# Initialize a Shortener object
short = pyshorteners.Shortener()

# Shorten the input link using TinyURL service
x = short.tinyurl.short(link)

print("\nShorted : "+x)