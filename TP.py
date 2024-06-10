import pandas as pd
import matplotlib.pyplot as plt

#1. Importation du jeu de données
csvfile = pd.read_csv('./Data/Phising_dataset_predict.csv', delimiter = ';')
csvfile2 = pd.read_csv('./Data/Phising_Detection_Dataset.csv', delimiter = ';')

csvfile.head(5)

csvfile.info

# Head = Les première ligne du tableau tout dépend du chiffre entre parenthèse
# Info = Information (champs, données, etc)


#2. Visualisation du jeu de données :

