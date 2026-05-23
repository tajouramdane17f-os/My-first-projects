import string
import secrets

chqracters = string .ascii_letters + string.digits + string.punctuation
password = ''.join(secrets.choice(chqracters) for i in range(24))
print("your new password is: " + password)