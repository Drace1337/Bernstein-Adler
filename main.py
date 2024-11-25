import random
import string

def bernstein_hash(string):
    h = 5381
    for char in string:
        h = (h * 32 + ord(char)) & 0xFFFFFFFF
    return h

def adler32_hash(string):
    p = 65521
    A = 1
    B = 0
    for char in string:
        A = (A + ord(char)) % p
        B = (B + A) % p
    return (B << 16) + A

def find_collisions(strings, hash_func):
    hash_map = {}
    collisions = 0
    collision_examples = []

    for string in strings:
        hash_value = hash_func(string)
        if hash_value in hash_map:
            if not collision_examples:
                collision_examples.append((hash_map[hash_value], hash_func(hash_map[hash_value])))
                collision_examples.append((string, hash_value))
            collisions += 1
        else:
            hash_map[hash_value] = string

    return collisions, collision_examples

# Generate C1 strings
c1_strings = []
for i in range(100000):
    c1_strings.append(''.join(random.choices(string.ascii_lowercase, k=8)))

# Generate C2 strings
c2_strings = []
for i in range(100000):
    c2_strings.append(''.join(random.choices(string.ascii_lowercase, k=100)))

# Search for collisions using Bernstein algorithm in C1 strings
c1_collisions, c1_collision_examples = find_collisions(c1_strings, bernstein_hash)
print("Bernstein algorithm collisions in C1 strings:", c1_collisions)
if c1_collision_examples:
    print("Examples of collisions in C1 strings:")
    for example in c1_collision_examples:
        print(f"String: {example[0]}, Hash: {example[1]}")
else:
    print("No collision found in C1 strings for Bernstein algorithm.")

# Search for collisions using Bernstein algorithm in C2 strings
c2_collisions, c2_collision_examples = find_collisions(c2_strings, bernstein_hash)
print("Bernstein algorithm collisions in C2 strings:", c2_collisions)
if c2_collision_examples:
    print("Examples of collisions in C2 strings:")
    for example in c2_collision_examples:
        print(f"String: {example[0]}, Hash: {example[1]}")
else:
    print("No collision found in C2 strings for Bernstein algorithm.")

# Search for collisions using Adler32 algorithm in C1 strings
c1_collisions, c1_collision_examples = find_collisions(c1_strings, adler32_hash)
print("Adler32 algorithm collisions in C1 strings:", c1_collisions)
if c1_collision_examples:
    print("Examples of collisions in C1 strings:")
    for example in c1_collision_examples:
        print(f"String: {example[0]}, Hash: {example[1]}")
else:
    print("No collision found in C1 strings for Adler32 algorithm.")

# Search for collisions using Adler32 algorithm in C2 strings
c2_collisions, c2_collision_examples = find_collisions(c2_strings, adler32_hash)
print("Adler32 algorithm collisions in C2 strings:", c2_collisions)
if c2_collision_examples:
    print("Examples of collisions in C2 strings:")
    for example in c2_collision_examples:
        print(f"String: {example[0]}, Hash: {example[1]}")
else:
    print("No collision found in C2 strings for Adler32 algorithm.")
