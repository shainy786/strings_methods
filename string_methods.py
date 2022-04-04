# n='shainaz'
# print(n.capitalize())
# print(n.upper())
# print(n.isupper())
# a='SHAINAZ'
# print(a.lower())
# print(a.casefold())
# print(a.islower())

# print(n.center(6))
# print(n.center(30,"*"))
# print(n.center(30))
# b="thank you"
# print(b.title())
# print(b.istitle())
# C="thaNk yoU"
# print(C.title())
# print(C.istitle())

# print(n,type(n))
# print(n.encode())
# w=n.encode()
# print(w)
# print(w.decode())

# p=b'shainaz'
# print(p.decode())
# s=p.decode()
# print(s)
# print(s.encode())

# a="shainaz"
# print(a.startswith(''))
# print(a.startswith(" "))
# print(a.startswith("s"))

# a=" shainaz"
# print(a.startswith(''))
# print(a.startswith(" "))
# print(a.startswith("i"))

# a="shainaz"
# print(a.endswith(''))
# print(a.endswith(" "))
# print(a.endswith("z"))

# a=" shainaz"
# print(a.endswith(''))
# print(a.endswith(" "))
# print(a.endswith("a"))

# a="shainaz"
# print(len(a))
# print(a.index("s"))
# print(a.index("h"))
# print(a.index("a",2))
# print(a.index("a"))
# print(a.index("a",4))
# print(a.rindex("a"))
# print(a.index("b"))         #valueerrror:substring not found
# print(a.rindex(""))           #7
# print(a.index(""))           #0

# a='shainaz'
# print(len(a))
# print(a.find("s"))
# print(a.find("h"))
# print(a.find("a"))
# print(a.rfind("a"))
# print(a.find("b"))         #-1
# print(a.find(''))           #0
# print(a.rfind(''))            #7

# a='shainaz patan'
# print(len(a))                   #13
# print(a.count("s"))
# print(a.count("h"))
# print(a.count("a",6))        #2
# print(a.count("a"))          #4
# print(a.count("b"))         #0
# print(a.count(""))            #14

# a='       shainaz patan  .      '
# print(a.strip())
# print(a.rstrip())
# print(a.lstrip())

# a='sha inaz'
# print(a.isidentifier())        #space is there

# a="hai shainy"
# print(a.replace("hai","bye",2))        
# print(a.replace("hai","bye",1))        #hai shainy

# a="s","h","a"
# print(a,type(a))
# b='*'.join(a)
# print(b)

# a="s",
# print(a,type(a))                    #tuple type but no str after comma so o/p as shows only   s
# b='*'.join(a)
# print(b)

# a='hai'
# print(a,type(a))                #str type so o/p as h*a*i
# b='*'.join(a)
# print(b)


# a="shainaz"
# print(a.isalnum())
# print(a.isalpha())
# b="786"
# print(b.isalnum())
# print(b.isalpha())
# c="shainy786"
# print(c.isalnum())
# print(c.isalpha())
# d=" shn"
# print(d.isalnum())
# print(d.isalpha())
# e="@vizag"
# print(e.isalnum())
# print(e.isalpha())

# a=bin(15)
# print(a,type(a))
# print(0b1111)
# print(0B1111)

# print(0b110)
# print(0b1101)
# print(0b1110)

# a=oct(15)
# print(a,type(a))
# print(0o17 )
# print(0O17 )

# print(0o110)
# print(0O1101)
# print(0o1110)

# a=hex(15)
# print(a,type(a))
# print(0xf )
# print(0xf)

# print(0xa)
# print(0XB)
# print(0xc)
# print(0xd)
# print(0Xe)
# print(0xf)

# print(0x111)
# print(0x110)
# print(0X1101)
# print(0x1110)
