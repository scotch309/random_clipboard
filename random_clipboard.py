import secrets, string
import pyperclip
chars = string.ascii_letters + string.digits
pyperclip.copy(''.join(secrets.choice(chars) for x in range(50)))