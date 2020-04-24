"""
Author: Han Su
Date: 24/04/2020
https://github.com/HanSu52/cp1404practicals
"""

COLOR_CODE = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "aquamarine1": "#7fffd4",
              "azure1": "#f0ffff", "beige": "#f5f5dc", "bisque1": "bisque1", "blue1": "#0000ff",
              "BlueViolet": "#8a2be2", "brown": "#a52a2a", "CadetBlue": "#5f9ea0"}
print(COLOR_CODE)

color_name = input("Enter color name: ")
while color_name != "":
    if color_name in COLOR_CODE:
        print(color_name, "is", COLOR_CODE[color_name])
    else:
        print("Invalid color name")
    color_name = input("Enter color name: ")
