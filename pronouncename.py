# Write a program to pronounce lists of name using win32 Ap1


# Source - https://stackoverflow.com/a
# Posted by Charlie
# Retrieved 2025-11-15, License - CC BY-SA 4.0

# for mac

from os import system
names = ["Shahbaz", "Zishan", "Wasif", "Kaif", "Mussharaf", "Arshad", "Sunny"]

for name in names:
    system(f'say brother {name}')