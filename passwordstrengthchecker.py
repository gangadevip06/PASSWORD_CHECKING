password = input("Enter your password: ")


# Character checks
has_upper = False
has_lower = False
has_digit = False
has_symbol = False


symbols = "!@#$%^&*()-_+=<>?/"



for char in password:

    if char.isupper():
        has_upper = True

    elif char.islower():
        has_lower = True

    elif char.isdigit():
        has_digit = True

    elif char in symbols:
        has_symbol = True



# Strength calculation

score = 0


if len(password) >= 8:
    score += 1

if has_upper:
    score += 1

if has_lower:
    score += 1

if has_digit:
    score += 1

if has_symbol:
    score += 1



# Result

if score <= 2:
    strength = "Weak"

elif score <= 4:
    strength = "Medium"

else:
    strength = "Strong"



print("\nPassword Strength:", strength)


# Extra security suggestions

if not has_upper:
    print("Add uppercase letters")

if not has_digit:
    print("Add numbers")

if not has_symbol:
    print("Add symbols")

if len(password) < 8:
    print("Use minimum 8 characters")