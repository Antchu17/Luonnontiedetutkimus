import numpy
from astropy.io import fits


def valitse():
    luettava = input("Anna luettavan tiedoston nimi: ")
    if luettava[-5::] != ".fits":   #Jos käyttäjä ei anna tiedoston päätettä niin ohjelma lisää sen
        luettava = luettava + ".fits"
    try:    #Ohjelma yrittää avata tiedoston, jos tiedosto ei avaudu niin ohjelma ilmoittaa ongelmasta
        fits.open(luettava)
    except FileNotFoundError:
        print("Tiedostoa ei löytynyt.")
        luettava = None
    return luettava

def luo(luettava):  #Tämä funktio luo halutun tekstitiedoston fits tiedoston tiedoilla
    hdul = fits.open(luettava)
        
    if hdul[0].header['SIMPLE'] == True:
        star = (str(hdul[0].header['OBJNAME'])).strip()
        crval = (str(hdul[0].header['CRVAL1'])).strip()
        naxis = (str(hdul[0].header['NAXIS1'])).strip()
        cdelt = (str(hdul[0].header['CDELT1'])).strip()
        unit = (str(hdul[0].header['CUNIT1'])).strip()

        kirjoitettava = input("Anna kirjoitettavan tiedoston nimi(leave empty for default name): ")
        if len(kirjoitettava) == 0:
            kirjoitettava = luettava[0:-5] + ".txt"
        if kirjoitettava[-4::] != ".txt":
            kirjoitettava = kirjoitettava + ".txt"
        tiedosto = open(kirjoitettava, "w")
        tiedosto.write("star;crval;cdelt;naxis;unit\n")
        rivi = star+";"+crval+";"+cdelt+";"+naxis+";"+unit
        tiedosto.write(rivi)
        tiedosto.close()

    
    elif hdul[0].header['SIMPLE'] == False:
        print("epäonnistui, tiedosto ei ole fits standardin mukainen.")
    return None

def valikko():  #Tämä funktio tulostaa ohjelman valikon ja kysyy käyttäjän valinnan
    print("Mitä haluat tehdä:")
    print("1) Valitse tiedosto")
    print("2) Luo tekstitiedosto tiedoston pohjalta")
    print("0) Lopeta")
    valinta = input("Valintasi: ")
    return valinta
    

def paaohjelma():
    print("Tämä ohjelma luo teksti-tiedoston halutuista fits tiedoston tiedoista.")
    while True:
        valinta = valikko()
        if valinta == "0":
            break
        elif valinta == "1":
            tiedosto = valitse()
            if tiedosto != None:
                print(tiedosto+"\n")
            else:
                print("")
        elif valinta == "2":
            try:
                luo(tiedosto)
            except:
                print("Tiedosto on valittava ensimmäisenä!\n")
        else:
            print('Virheellinen valinta\n')
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
