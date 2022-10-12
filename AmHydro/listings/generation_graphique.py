from matplotlib import pyplot as plt


if __name__ == "__main__" :

    seriesAnnuelles = {}
    seriesAnnuelles.update({'1965':{'debit_mensuel':[11.3,9.7,14,14.5,160,205,205,350,145,84,21,17.5]}})
    seriesAnnuelles.update({'1966':{'debit_mensuel':[16.6,18.5,16.6,47,105,175,155,150,97,125,25,19.5]}})
    seriesAnnuelles.update({'1967':{'debit_mensuel':[16.7,18.8,20,39,145,320,240,210,110,75,38,35]}})
    seriesAnnuelles.update({'1968':{'debit_mensuel':[19.2,14.6,21,53,125,205,220,115,140,57,185,40]}})
    seriesAnnuelles.update({'1969':{'debit_mensuel':[14.8,13.4,13.9,32,120,205,190,175,82,65,45,22]}})
    seriesAnnuelles.update({'1970':{'debit_mensuel':[26,21,17.2,38,85,235,165,195,110,140,24,27]}})
    seriesAnnuelles.update({'1971':{'debit_mensuel':[30,43,24,29,105,145,270,96,63,49,44]}})
    seriesAnnuelles.update({'1972':{'debit_mensuel':[26,23,13.1,31,62,185,170,380,77,59,35,16.3]}})
    seriesAnnuelles.update({'1973':{'debit_mensuel':[43,33,27,47,105,150,250,195,120,63,19.2,22]}})
    seriesAnnuelles.update({'1974':{'debit_mensuel':[24,25,25,53,105,130,160,160,95,20,15.3,14.6]}})
    seriesAnnuelles.update({'1975':{'debit_mensuel':[24,26,26,52,140,195,200,160,125,115,30,27]}})
    seriesAnnuelles.update({'1976':{'debit_mensuel':[24,12.4,41,49,78,130,155,90,89,155,35,17.6]}})
    seriesAnnuelles.update({'1977':{'debit_mensuel':[14.6,17.2,52,75,145,220,180,295,110,315,44,33]}})
    seriesAnnuelles.update({'1978':{'debit_mensuel':[27,17.9,48,32,90,185,180,325,81,50,24,18.4]}})
    seriesAnnuelles.update({'1979':{'debit_mensuel':[16.8,15.3,23,23,155,160,210,88,215,39,30]}})
    seriesAnnuelles.update({'1980':{'debit_mensuel':[32,37,14.7,24,58,170,195,215,110,105,35,34]}})
    seriesAnnuelles.update({'1981':{'debit_mensuel':[28,26,99,11,86,215,295,170,320,100,58,33]}})
    seriesAnnuelles.update({'1982':{'debit_mensuel':[37,28,68,70,130,170,235,220,165,97,69,33]}})
    seriesAnnuelles.update({'1983':{'debit_mensuel':[27,66,56,70,155,180,290,235,175,90,40,15.2]}})
    seriesAnnuelles.update({'1984':{'debit_mensuel':[23,36,35,60,67,165,225,205,125,81,36,27]}})
    seriesAnnuelles.update({'1985':{'debit_mensuel':[37,32,12.9,44,140,190,200,160,130,97,41,17.2]}})
    seriesAnnuelles.update({'1986':{'debit_mensuel':[34,37,15.9,58,190,225,247,5,170,125,88,40,30]}})
    seriesAnnuelles.update({'1987':{'debit_mensuel':[36,32,33,88,97,295,305,495,160,155,32,28]}})
    seriesAnnuelles.update({'1988':{'debit_mensuel':[17.1,32,37,58,140,140,230,185,150,190,75,29]}})
    seriesAnnuelles.update({'1989':{'debit_mensuel':[14.3,21,33,52,160,145,210,185,110,76,55,23]}})
    seriesAnnuelles.update({'1990':{'debit_mensuel':[21,34,28,38,140,145,160,180,105,97,52,15.3]}})
    seriesAnnuelles.update({'1991':{'debit_mensuel':[14.4,39,45,55,110,270,200,175,185,85,24,36]}})
    seriesAnnuelles.update({'1992':{'debit_mensuel':[13.5,12.5,16.7,62,110,290,225,215,175,75,46,38]}})
    seriesAnnuelles.update({'1993':{'debit_mensuel':[28,42,38,49,125,200,180,150,460,170,37,27]}})

    # Recherche du max et du min
    for data in seriesAnnuelles.values() :
        liste = data['debit_mensuel']
        data.update({'debit_max':max(liste)})
        data.update({'debit_min':min(liste)})