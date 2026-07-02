# try/except ili try....catch
try:
    #print(100/0)
    broj1 = int(input("Vnesi broj1: "))
    broj2 = int(input("Vnesi broj2: "))
    zbir = broj1+broj2
    print(zbir)
   #except: ako ostavime samo exept togas gi zema vo predvid site mozni greski  
except ZeroDivisionError:
    print("Ne moze da se deli so 0")
except ValueError:
    print("Vnesovte pogresna vrednost")
except IndexError:
    print("Ne postoi takov indeks")
#except:
#    raise ValueError("Vnesovte losi podatoci") - ova ako sakame nie da ja definirame greskata kako da ja pojavuva
