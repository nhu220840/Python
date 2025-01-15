import pyperclip
import keyboard
import time

file_path = "temp_clipboard.txt"
logged_content = set()

with open(file_path, "a", encoding="utf-8") as file:
    print("Copying the fomulars. Press Ctrl K to stop")
    while True:
        try:
            if keyboard.is_pressed('ctrl+c'):
                time.sleep(0.1)
                content = pyperclip.paste().strip()
                if content and content not in logged_content:
                    file.write(content + "\n")
                    file.flush()
                    logged_content.add(content)
                    print(f"Saved: {content}")
            if keyboard.is_pressed('ctrl+k'):
                print("Stopped.")
                break
        except Exception as e:
            print(f"Error: {e}")
            break

"""prompt chatgpt: Cho mẫu file như này, Chút nữa khi tôi gửi 1 file chỉ có công thức phân tử của các hợp chất, hãy viết tên upac của chúng đúng với định dạng như này, không lan man
Ac: Actinium
Ag: Silver
Al: Aluminum
Am: Americium
Ar: Argon
As: Arsenic
At: Astatine
Ba: Barium
Be: Beryllium
Bh: Bohrium
Bi: Bismuth
Bk: Berkelium
Br: Bromine
B: Boron
C: Carbon
Ca: Calcium
Cd: Cadmium
Ce: Cerium
Cf: Californium
Cl: Chlorine
Cm: Curium
Co: Cobalt
Cr: Chromium
Cs: Cesium
Cu: Copper
Db: Dubnium
Ds: Darmstadtium
Dy: Dysprosium
Er: Erbium
Es: Einsteinium
Eu: Europium
F: Fluorine
Fe: Iron
Fl: Flerovium
Fm: Fermium
Fr: Francium
Ga: Gallium
Gd: Gadolinium
Ge: Germanium
H: Hydrogen
He: Helium
Hf: Hafnium
Hg: Mercury
Ho: Holmium
Hs: Hassium
I: Iodine
In: Indium
Ir: Iridium
K: Potassium
Kr: Krypton
La: Lanthanum
Li: Lithium
Lr: Lawrencium
Lv: Livermorium
Lu: Lutetium
Md: Mendelevium
Mg: Magnesium
Mn: Manganese
Mo: Molybdenum
N: Nitrogen
Na: Sodium
Nb: Niobium
Nd: Neodymium
Ne: Neon
Nh: Nihonium
Ni: Nickel
No: Nobelium
Np: Neptunium
O: Oxygen
Og: Oganesson
Os: Osmium
P: Phosphorus
Pa: Protactinium
Pb: Lead
Pd: Palladium
Pm: Promethium
Po: Polonium
Pr: Praseodymium
Pt: Platinum
Pu: Plutonium
Ra: Radium
Rb: Rubidium
Re: Rhenium
Rf: Rutherfordium
Rg: Roentgenium
Rh: Rhodium
Rn: Radon
Ru: Ruthenium
S: Sulfur
Sb: Antimony
Sc: Scandium
Se: Selenium
Sg: Seaborgium
Si: Silicon
Sm: Samarium
Sn: Tin
Sr: Strontium
Ta: Tantalum
Tb: Terbium
Tc: Technetium
Te: Tellurium
Th: Thorium
Ti: Titanium
Tl: Thallium
Tm: Thulium
Ts: Tennessine
U: Uranium
V: Vanadium
W: Tungsten
Xe: Xenon
Y: Yttrium
Yb: Ytterbium
Zn: Zinc
Zr: Zirconium
"""