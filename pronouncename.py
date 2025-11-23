# Write a program to pronounce lists of name using import

from os import system
names = ["Shahbaz", "Zishan", "Wasif", "Kaif", "Mussharaf", "Arshad", "Sunny"]

for name in names:
    system(f'say brother {name}')
