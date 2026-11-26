# Caesar Cipher

[راهنمای فارسی](README_FA.md)

Encode and decode messages by shifting English letters through the alphabet. This exercise demonstrates string handling and modular arithmetic.

## Quick install on Ubuntu

Run this command in your terminal. It needs `curl` and Python 3.8 or later.

```bash
bash -o pipefail -c 'curl -fsSL https://raw.githubusercontent.com/seetaayeesh/caesar-cipher/main/install.sh | bash'
```

Then launch the program.

```bash
~/.local/bin/caesar-cipher
```

The installer uses your home directory. Run the same install command to update. If a prerequisite is missing, run `sudo apt update && sudo apt install curl python3` first.

## Run the program

Use Python 3.8 or later. From this repository’s folder, run the following command.

```bash
python3 main.py
```

On Windows, use `py main.py`. No extra packages are required.

## Try an example

Choose `1` to encode or `2` to decode. Then enter a message and a whole-number shift.

```text
Choose 1 or 2: 1
Message: XyZ! 42
Shift: 3
Encoded message: AbC! 42
```

Choose `2` and enter `AbC! 42` with the same shift to recover `XyZ! 42`.

## How the code works

The program shifts letters from A to Z and a to z while keeping their case. Spaces, numbers, punctuation, and letters outside those ranges stay as entered. The expression `% 26` wraps letters around the alphabet. Decoding uses the same function with the shift reversed.

[MIT license](LICENSE)
