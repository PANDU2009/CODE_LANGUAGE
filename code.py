# Custom code language dictionary
code_map = {
    'A': '.', 'B': '-', 'C': '|', 'D': '\\', 'E': '/', 'F': '+', 'G': 'x', 'H': 'o',
    'I': '^', 'J': '_', 'K': '<', 'L': '>', 'M': '(', 'N': ')', 'O': '[', 'P': ']',
    'Q': '{', 'R': '}', 'S': '*', 'T': '=', 'U': '~', 'V': "'", 'W': '"', 'X': '#',
    'Y': '?', 'Z': '!'
}

# Reverse mapping for decoding
reverse_map = {v: k for k, v in code_map.items()}

# Set of encoded characters
encoded_chars = set(reverse_map.keys())

def is_encoded(text):
    count = sum(1 for char in text if char in encoded_chars)
    return count >= len(text) * 0.7 if text else False

def encode_to_code_language(text):
    text = text.upper()
    return ''.join(code_map.get(char, char) for char in text)

def decode_from_code_language(code):
    return ''.join(reverse_map.get(char, char) for char in code)

def main():
    while True:
        try:
            text = input().strip()
            if text.lower() == 'exit':
                break
            if is_encoded(text):
                print("Decoded:", decode_from_code_language(text))
            else:
                print("Encoded:", encode_to_code_language(text))
        except EOFError:
            break

if __name__ == "__main__":
    main()
