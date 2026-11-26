def encode(text, k):
    """Shift each English letter by k positions, keeping its case."""
    result = []
    for char in text:
        if "A" <= char <= "Z":
            start = ord("A")
        elif "a" <= char <= "z":
            start = ord("a")
        else:
            result.append(char)
            continue

        # Use positions 0–25 so shifts wrap around the alphabet.
        position = (ord(char) - start + k) % 26
        result.append(chr(start + position))

    return "".join(result)


def decode(text, k):
    # Reversing the shift undoes the encoding.
    return encode(text, -k)


def main():
    print("1. Encode\n2. Decode")
    choice = input("Choose 1 or 2: ").strip()
    if choice not in ("1", "2"):
        print("Invalid option. Choose 1 or 2.")
        return

    text = input("Message: ")
    try:
        shift = int(input("Shift: "))
    except ValueError:
        print("Invalid shift. Enter a whole number.")
        return

    if choice == "1":
        print("Encoded message:", encode(text, shift))
    else:
        print("Decoded message:", decode(text, shift))


if __name__ == "__main__":
    main()
