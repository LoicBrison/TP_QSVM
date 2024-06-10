import pandas as pd

#1. Importation du jeu de données
csvfile = pd.read_csv('Data/Phising_dataset_predict.csv', delimiter = ';')

csvfile.head(5)

csvfile.info
