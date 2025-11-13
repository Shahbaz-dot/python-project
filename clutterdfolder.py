import os

files = os.listdir("clutterfolderr")
i = 1
for file in files:
  if file.endswith(".png"):
    print(file)
    os.rename(f"clutterfolderr/{file}", f"clutterfolderr/{i}.png")
    i = i + 1