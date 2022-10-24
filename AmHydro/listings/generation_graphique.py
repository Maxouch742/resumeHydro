from matplotlib import pyplot as plt
import numpy as np

def plot_Stationnarite(data, key) :

    fig = plt.figure()
    for cle, donne in data.items() :
        plt.plot(cle,donne[key],marker='o',color='red')
    plt.grid()
    plt.xlabel("Années")
    plt.ylabel("Débit [$m^3/s$]")
    plt.title("Stationnarité")
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
    seriesAnnuelles.update({'1986':{'debit_mensuel':[34.0,37.0,15.9,58.0,190.0,225.0,247.0,005.0,170.0,125.0,088.0,40.8]}})
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

    plot_Homogeneite(seriesAnnuelles)
    