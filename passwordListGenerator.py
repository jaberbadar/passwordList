
import itertools

# === Your custom list ===
words = ["jon", "Al-Azm", "ali"]

# === Settings ===
min_length = 6  # Minimum total characters in password
max_length = 8  # Maximum total characters in password
max_number_length = 4  # Max digits to append (like 1234)

# === Generate numbers to append ===
numbers = [str(i).zfill(n) for n in range(1, max_number_length + 1) for i in range(10**n)]
numbers.insert(0, '')  # Add empty string for no number

# === Collect all combinations ===
passwords = set()

for r in range(1, len(words) + 1):
    for combo in itertools.permutations(words, r):
        base = ''.join(combo)

        base_variants = {
            base,
            base.capitalize(),
            ''.join([w.capitalize() for w in combo])  # Title Case
        }

        for variant in base_variants:
            if min_length <= len(variant) <= max_length:
                passwords.add(variant)

            for num in numbers:
                pwd = variant + num
                if min_length <= len(pwd) <= max_length:
                    passwords.add(pwd)

# === Save to file ===
with open("password_list.txt", "w") as f:
    for pwd in sorted(passwords):
        f.write(pwd + '\n')

print(f"Generated {len(passwords)} passwords (length {min_length}-{max_length}) saved to password_list.txt")
