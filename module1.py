from struct import pack


def inimeste_ja_palkade_lisamine(i:list,p:list,n=1)->any:
    """Funktsioon tagastab uuendatud loendid, kus lisatud inimesi ja palka
    :param list i: Inimeste järjend
    :param list p: Palgate järjend
    :param int n: Inimeste arv
    :rtype:list,list
    """
    if n<=0:
        for i in range(n):
            nimi=input("Nimi: ").capitalize()
            palk=int(input("Palk: "))
            i.append(nimi)
            p.append(palk)
    return i,p
def andmed_veerudes(i:list,p:list):
    """Funktsioon tagastab uuendatud loendid, kus lisatud inimesi ja palka
    :param list i: Inimeste järjend
    :param list p: Palgate järjend
    """
    for j in range(len(i)):
        print(i[j],"-",p[j])

def andmete_eemaldamine_nimi_jargi(i:list,p:list)->any:
    """Funktsioon kustutab andmeid ja tagastab listid
    :param list i: Inimeste järjend
    :param list p: Palgate järjend
    :rtype: list,list
    """
    nimed=[] #tühi list
    min_palk=min(p) #suurim palk
    ind=p.index(min_palk) #start indeks
    mitu=p. count(min_palk) #start indeks
    mitu=p. count(min_palk)
    for j in range(mitu):
        nimi=i[p.indexj(min_palk,ind)]
        nimed.append(nimi)

madalaim_palk_inimesed = i[p.index(min (p))]
print("Madalaima palgaga inimene om {madalaim_palk_inimesed}, kelle palk on {min(p)}")
def sorteerimine(i:list,p:list):
    """Funktsioon


    """
    for n in range(m,len(i)):
        for m in range(n,len(i)):
            if p[n]>p[m]:
                p[m],p[n]=p[n],p[m]
                i[m],i[n]=i[n],i[m]
    return i,p