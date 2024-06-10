import pandas as pd

#1. Importation du jeu de données
csvfile = pd.read_csv('./Data/Phising_dataset_predict.csv', delimiter = ';')

csvfile.head(5)

csvfile.info

#Questions guidantes :
# • Comment importer un fichier CSV en Python ?
# • Quelles informations peut-on obtenir avec les méthodes head() et info() de pandas ?

# Head = Les première ligne du tableau tout dépend du chiffre entre parenthèse
# Info = 


#2. Visualisation du jeu de données :