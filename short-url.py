#pip install pyshorteners

import pyshorteners

url_longa = input("Cole aqui o seu link: ")

type_tiny = pyshorteners.Shortener()

link_curto = type_tiny.tinyurl.short(url_longa)

print("O seu link curto e ese aqui:" + link_curto)
