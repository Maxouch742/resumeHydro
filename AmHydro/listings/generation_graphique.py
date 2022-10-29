from matplotlib import pyplot as plt
import numpy as np
import operator
import math

def plot_Stationnarite(data, key) :

    debit_max = np.nan
    fig = plt.figure()
    for cle, donne in data.items() :
        plt.plot(cle,donne[key],marker='o',color='red')
        if np.isnan(debit_max) == True :
            debit_max = donne[key]
        elif debit_max < donne[key] :
            debit_max = donne[key]
    plt.grid()
    plt.xlabel("Années")
    plt.ylabel("Débit [$m^3/s$]")
    plt.ylim(0,round(debit_max, -2))
    plt.title("Stationnarité ({:s}-{:s})".format(list(data.keys())[0], list(data.keys())[-1]))
    fig.autofmt_xdate(rotation=45)
    plt.savefig("stationnarite.png")


def plot_Homogeneite(data) :

    mois = ['Janvier','Fevrier','Mars','Avril','Mai','Juin','Juillet','Aout','Septembre','Octobre','Novembre','Decembre']
    mois = np.array(mois)

    fig = plt.figure()
    for annee in data.keys() :
        debit = []
        for i in data[annee]['debit_mensuel'] :
            debit.append(i)
        debit = np.array(debit)
        plt.plot(mois,debit)
    plt.grid()
    plt.xlabel("Mois")
    plt.ylabel("Débit [$m^3/s$]")
    plt.title("Homogénéité ({:s}-{:s})".format(list(data.keys())[0], list(data.keys())[-1]))
    fig.autofmt_xdate(rotation=45)
    plt.savefig("homogeneite.png")


def calcul_TempsRetour(data_dict, formule=["Hazen"]) :

    data_tried = dict(sorted(data_dict.items(), key=lambda x: x[1]['debit_max'], reverse=True))
    
    rang = 1
    for key, data in data_tried.items() :
        data.update({"rang":rang})
        rang += 1
        data.update({"temps_retour_Hazen":tempsRetour('Hazen', rang, len(data_tried))})
        for form in formule :
            if form != 'Hazen' or form != 'hazen' :
                name = "temps_retour_" + form
                data.update({name:tempsRetour(form, rang, len(data_tried))})

    return data_tried


def tempsRetour(name, rang, annee) :

    if name.lower() == "hazen" :
        tRetour = annee / (rang - 0.5)
    elif name.lower() == 'weibull' :
        tRetour = (annee + 1) / rang
    elif name.lower() == 'mediane' :
        tRetour = (annee + 0.365) / (rang - 0.3175)
    elif name.lower() == 'hosking' :
        tRetour = (annee) / (rang - 0.35)
    elif name.lower() == 'blom' :
        tRetour = (annee + 0.25) / (rang - 0.375)
    elif name.lower() == 'cunnane' :
        tRetour = (annee + 0.20) / (rang - 0.40)
    elif name.lower() == 'gringorten' :
        tRetour = (annee + 0.12) / (rang - 0.44)
    else :
        tRetour = np.nan
    return tRetour


def plot_TempsRetour(data) :

    fig = plt.figure()

    debit_max = np.nan

    Tretour = {}
    Tretour.update({"Hazen":[]})
    Tretour.update({"Weibull":[]})
    Tretour.update({"Mediane":[]})
    Tretour.update({"Hosking":[]})
    Tretour.update({"Blom":[]})
    Tretour.update({"Cunnane":[]})
    Tretour.update({"Gringorten":[]})
    
    for donne in data.values() :
        Tretour["Hazen"].append([donne["temps_retour_Hazen"],donne['debit_max']])
        if np.isnan(debit_max) == True :
            debit_max = donne["debit_max"]
        elif debit_max < donne["debit_max"]:
            debit_max = donne["debit_max"]
        if "temps_retour_Weibull" in list(donne.keys()) :
            Tretour["Weibull"].append([donne["temps_retour_Weibull"],donne['debit_max']])
        if "temps_retour_Mediane" in list(donne.keys()) :
            Tretour["Mediane"].append([donne["temps_retour_Mediane"],donne['debit_max']])
        if "temps_retour_Hosking" in list(donne.keys()) :
            Tretour["Hosking"].append([donne["temps_retour_Hosking"],donne['debit_max']])
        if "temps_retour_Blom" in list(donne.keys()) :
            Tretour["Blom"].append([donne["temps_retour_Blom"],donne['debit_max']])
        if "temps_retour_Cunnane" in list(donne.keys()) :
            Tretour["Cunnane"].append([donne["temps_retour_Cunnane"],donne['debit_max']])
        if "temps_retour_Gringorten" in list(donne.keys()) :
            Tretour["Gringorten"].append([donne["temps_retour_Gringorten"],donne['debit_max']])
    
    for key, data in Tretour.items() :
        if len(data) > 0 :
            arrayyy = np.array(data)
            plt.plot(arrayyy[:,0], arrayyy[:,1], 'o-', label=key)


    plt.grid()
    plt.xlabel("Temps de retour [année]")
    plt.ylim(0,round(debit_max, -2)+100)
    plt.ylabel("Débit [$m^3/s$]")
    plt.title("Temps de retour calculé")
    plt.savefig("tempsRetour.png")
    plt.legend()
    

if __name__ == "__main__" :

    seriesAnnuelles = {}
    seriesAnnuelles.update({'1965':{'debit_mensuel':[11.3,09.7,14.0,14.5,160.0,205.0,205.0,350.0,145.0,084.0,021.0,17.5]}})
    seriesAnnuelles.update({'1966':{'debit_mensuel':[16.6,18.5,16.6,47.0,105.0,175.0,155.0,150.0,097.0,125.0,025.0,19.5]}})
    seriesAnnuelles.update({'1967':{'debit_mensuel':[16.7,18.8,20.0,39.0,145.0,320.0,240.0,210.0,110.0,075.0,038.0,35.0]}})
    seriesAnnuelles.update({'1968':{'debit_mensuel':[19.2,14.6,21.0,53.0,125.0,205.0,220.0,115.0,140.0,057.0,185.0,40.0]}})
    seriesAnnuelles.update({'1969':{'debit_mensuel':[14.8,13.4,13.9,32.0,120.0,205.0,190.0,175.0,082.0,065.0,045.0,22.0]}})
    seriesAnnuelles.update({'1970':{'debit_mensuel':[26.0,21.0,17.2,38.0,085.0,235.0,165.0,195.0,110.0,140.0,024.0,27.0]}})
    seriesAnnuelles.update({'1971':{'debit_mensuel':[30.0,43.0,24.0,29.0,105.0,145.0,270.0,096.0,063.0,049.0,044.0,40.0]}})
    seriesAnnuelles.update({'1972':{'debit_mensuel':[26.0,23.0,13.1,31.0,062.0,185.0,170.0,380.0,077.0,059.0,035.0,16.3]}})
    seriesAnnuelles.update({'1973':{'debit_mensuel':[43.0,33.0,27.0,47.0,105.0,150.0,250.0,195.0,120.0,063.0,019.2,22.0]}})
    seriesAnnuelles.update({'1974':{'debit_mensuel':[24.0,25.0,25.0,53.0,105.0,130.0,160.0,160.0,095.0,020.0,015.3,14.6]}})
    seriesAnnuelles.update({'1975':{'debit_mensuel':[24.0,26.0,26.0,52.0,140.0,195.0,200.0,160.0,125.0,115.0,030.0,27.0]}})
    seriesAnnuelles.update({'1976':{'debit_mensuel':[24.0,12.4,41.0,49.0,078.0,130.0,155.0,090.0,089.0,155.0,035.0,17.6]}})
    seriesAnnuelles.update({'1977':{'debit_mensuel':[14.6,17.2,52.0,75.0,145.0,220.0,180.0,295.0,110.0,315.0,044.0,33.0]}})
    seriesAnnuelles.update({'1978':{'debit_mensuel':[27.0,17.9,48.0,32.0,090.0,185.0,180.0,325.0,081.0,050.0,024.0,18.4]}})
    seriesAnnuelles.update({'1979':{'debit_mensuel':[16.8,15.3,23.0,23.0,155.0,160.0,210.0,088.0,215.0,039.0,030.0,27.8]}})
    seriesAnnuelles.update({'1980':{'debit_mensuel':[32.0,37.0,14.7,24.0,058.0,170.0,195.0,215.0,110.0,105.0,035.0,34.0]}})
    seriesAnnuelles.update({'1981':{'debit_mensuel':[28.0,26.0,99.0,11.0,086.0,215.0,295.0,170.0,320.0,100.0,058.0,33.0]}})
    seriesAnnuelles.update({'1982':{'debit_mensuel':[37.0,28.0,68.0,70.0,130.0,170.0,235.0,220.0,165.0,097.0,069.0,33.0]}})
    seriesAnnuelles.update({'1983':{'debit_mensuel':[27.0,66.0,56.0,70.0,155.0,180.0,290.0,235.0,175.0,090.0,040.0,15.2]}})
    seriesAnnuelles.update({'1984':{'debit_mensuel':[23.0,36.0,35.0,60.0,067.0,165.0,225.0,205.0,125.0,081.0,036.0,27.0]}})
    seriesAnnuelles.update({'1985':{'debit_mensuel':[37.0,32.0,12.9,44.0,140.0,190.0,200.0,160.0,130.0,097.0,041.0,17.2]}})
    seriesAnnuelles.update({'1986':{'debit_mensuel':[34.0,37.0,15.9,58.0,190.0,225.0,247.0,095.0,170.0,125.0,088.0,40.8]}})
    seriesAnnuelles.update({'1987':{'debit_mensuel':[36.0,32.0,03.0,88.0,097.0,295.0,305.0,495.0,160.0,155.0,032.0,28.0]}})
    seriesAnnuelles.update({'1988':{'debit_mensuel':[17.1,32.0,03.0,58.0,140.0,140.0,230.0,185.0,150.0,190.0,075.0,29.0]}})
    seriesAnnuelles.update({'1989':{'debit_mensuel':[14.3,21.0,03.0,52.0,160.0,145.0,210.0,185.0,110.0,076.0,055.0,23.0]}})
    seriesAnnuelles.update({'1990':{'debit_mensuel':[21.0,34.0,02.0,38.0,140.0,145.0,160.0,180.0,105.0,097.0,052.0,15.3]}})
    seriesAnnuelles.update({'1991':{'debit_mensuel':[14.4,39.0,04.0,55.0,110.0,270.0,200.0,175.0,185.0,085.0,024.0,36.0]}})
    seriesAnnuelles.update({'1992':{'debit_mensuel':[13.5,12.5,16.7,62.0,110.0,290.0,225.0,215.0,175.0,075.0,046.0,38.0]}})
    seriesAnnuelles.update({'1993':{'debit_mensuel':[28.0,42.0,38.0,49.0,125.0,200.0,180.0,150.0,460.0,170.0,037.0,27.0]}})

    # Recherche du max et du min
    for data in seriesAnnuelles.values() :
        tab = data['debit_mensuel']
        data.update({'debit_max':max(tab)})
        data.update({'debit_min':min(tab)})

    #plot_Stationnarite(seriesAnnuelles, "debit_max")
    #plot_Homogeneite(seriesAnnuelles)

    seriesAnnuelles = calcul_TempsRetour(seriesAnnuelles, ['Weibull'])
    plot_TempsRetour(seriesAnnuelles)