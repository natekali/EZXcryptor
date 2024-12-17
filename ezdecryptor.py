#!/usr/bin/python3

#color
class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

#banner
def banner():
    print(f"{Color.RED}▓█████ ▒███████▒   ▓█████▄ ▓█████  ▄████▄   ██▀███ ▓██   ██▓ ██▓███  ▄▄▄█████▓{Color.END}")
    print(f"{Color.RED}▓█   ▀ ▒ ▒ ▒ ▄▀░   ▒██▀ ██▌▓█   ▀ ▒██▀ ▀█  ▓██ ▒ ██▒▒██  ██▒▓██░  ██▒▓  ██▒ ▓▒{Color.END}")
    print(f"{Color.RED}▒███   ░ ▒ ▄▀▒░    ░██   █▌▒███   ▒▓█    ▄ ▓██ ░▄█ ▒ ▒██ ██░▓██░ ██▓▒▒ ▓██░ ▒░{Color.END}")
    print(f"{Color.BOLD}▒▓█  ▄   ▄▀▒   ░   ░▓█▄   ▌▒▓█  ▄ ▒▓▓▄ ▄██▒▒██▀▀█▄   ░ ▐██▓░▒██▄█▓▒ ▒░ ▓██▓ ░ {Color.END}")
    print(f"{Color.BOLD}░▒████▒▒███████▒   ░▒████▓ ░▒████▒▒ ▓███▀ ░░██▓ ▒██▒ ░ ██▒▓░▒██▒ ░  ░  ▒██▒ ░ {Color.END}")
    print(f"{Color.BOLD}░░ ▒░ ░░▒▒ ▓░▒░▒    ▒▒▓  ▒ ░░ ▒░ ░░ ░▒ ▒  ░░ ▒▓ ░▒▓░  ██▒▒▒ ▒▓▒░ ░  ░  ▒ ░░   {Color.END}")
    print(f"{Color.BOLD} ░ ░  ░░░▒ ▒ ░ ▒    ░ ▒  ▒  ░ ░  ░  ░  ▒     ░▒ ░ ▒░▓██ ░▒░ ░▒ ░         ░    {Color.END}")

#cesar method
def cesar(value, shift):
    result = ""
    for char in value:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result

#ceasr bruteforce
def cesar_brute(value):
    print(f"{Color.YELLOW}testing...{Color.END}")
    for shift in range(26):
        result = cesar(value, shift)
        print(f"{Color.GREEN}int {shift}:{Color.END} {result}")

#rot13
def rot13(value):
    return cesar(value, 13)

#substitution
def substitute(value):
    result = ""
    mapping = {chr(90 - (i - 65)): chr(i) for i in range(65, 91)}
    for char in value:
        if char.upper() in mapping:
            result += mapping[char.upper()] if char.isupper() else mapping[char.upper()].lower()
        else:
            result += char
    return result

#vigenere
def vigenere(value, keyword):
    result = ""
    keyword = keyword.lower()
    keyword_length = len(keyword)
    keyword_index = 0
    for char in value:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift = ord(keyword[keyword_index % keyword_length]) - ord('a')
            result += chr((ord(char) - base - shift) % 26 + base)
            keyword_index += 1
        else:
            result += char
    return result

#vigenere bruteforce
def vigenere_brute(value, max_length):
    print(f"{Color.YELLOW}testing... (length {max_length}){Color.END}")
    from itertools import product
    import string
    letters = string.ascii_lowercase
    for length in range(1, max_length + 1):
        for keyword_tuple in product(letters, repeat=length):
            keyword = ''.join(keyword_tuple)
            result = vigenere(value, keyword)
            print(f"{Color.GREEN}key '{keyword}':{Color.END} {result}")

#processing func
def process():
    print("")
    banner()
    print("")
    print(f"{Color.BOLD}1. CESAR{Color.END}")
    print(f"{Color.RED}2. ROT13{Color.END}")
    print(f"{Color.BOLD}3. SUBSTITUTION{Color.END}")
    print(f"{Color.RED}4. VIGENERE{Color.END}")
    print("")
    choice = input(f'{Color.BOLD}> choose decryption method: {Color.END}')
    text = input(f'{Color.BOLD}> enter the text to decrypt: {Color.END}')
    print("")
    if choice == '1':
        brute = input(f'{Color.BOLD}> bruteforce (y/n)? {Color.END}').strip().lower()
        if brute == 'y':
            cesar_brute(text)
        else:
            shift = int(input(f'{Color.BOLD}> enter int value for decryption: {Color.END}'))
            print("")
            print(f"{Color.GREEN}result:{Color.END}", cesar(text, shift))
    elif choice == '2':
        print(f"{Color.GREEN}result:{Color.END}", rot13(text))
    elif choice == '3':
        print(f"{Color.GREEN}result:{Color.END}", substitute(text))
    elif choice == '4':
        brute = input(f'{Color.BOLD}> bruteforce (y/n)? {Color.END}').strip().lower()
        if brute == 'y':
            length = int(input(f'{Color.BOLD}> enter max length: {Color.END}'))
            vigenere_brute(text, length)
        else:
            keyword = input(f'{Color.BOLD}> enter the keyword for decryption: {Color.END}')
            print("")
            print(f"{Color.GREEN}result:{Color.END}", vigenere(text, keyword))
    else:
        print(f"{Color.RED}invalid choice!{Color.END}")

#main func
def main():
    process()
    while True:
        print("")
        retry = input("another (y/n)? ").strip().lower()
        if retry == 'y':
            process()
        elif retry == 'n':
            print(f"{Color.RED}ezdecryptor stopped!{Color.END}")
            break
        else:
            print(f"{Color.RED}invalid input - enter 'y' or 'n'{Color.END}")

#interpreter start
if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"{Color.RED}error: {e}{Color.END}")
    except KeyboardInterrupt:
        print(f"\r{Color.RED}ezdecryptor stopped!{Color.END}")
