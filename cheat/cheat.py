import pyperclip
import time

with open("dic.txt", "r", encoding="utf-8") as file:
    elements = {}
    for line in file:
        line = line.strip()
        if ": " in line:
            symbol, name = line.split(": ")
            elements[symbol] = name

def find_element_in_clipboard():
    while True:
        current_text = pyperclip.paste().strip()
        if current_text in elements:
            full_name = elements[current_text]
            pyperclip.copy(full_name)
            print(f"Found: {current_text} -> {full_name}")

        time.sleep(0.5)

find_element_in_clipboard()