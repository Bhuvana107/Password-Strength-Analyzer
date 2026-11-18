
import string
import secrets
import getpass

print("===== PASSWORD STRENGTH ANALYZER =====")

password = getpass.getpass("Enter a demo password: ")

score = 0

if len(password) >= 8:
    score += 1

if any(c.isupper() for c in password):
    score += 1

if any(c.islower() for c in password):
    score += 1

if any(c.isdigit() for c in password):
    score += 1

if any(c in string.punctuation for c in password):
    score += 1

if len(set(password)) >= 5:
    score += 1

print("\n===== ANALYSIS RESULT =====")

if score <= 2:
    print("Password Strength: WEAK")
elif score <= 4:
    print("Password Strength: MEDIUM")
else:
    print("Password Strength: STRONG")

print("Security Score:", score, "/ 6")

if score < 6:
    chars = [
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation)
    ]

    all_chars = string.ascii_letters + string.digits + string.punctuation

    chars += [secrets.choice(all_chars) for _ in range(12)]

    secrets.SystemRandom().shuffle(chars)

    print("Suggested Strong Password:")
    print(''.join(chars))

print("Analysis Completed!")
