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

#Pour un graphique à Secteur (avec des données fictives) :
labels = ['Phishing', 'Légitime']
sizes = [150, 850]

# Création du graphique à secteurs
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff'])
plt.title('Proportions des différentes classes d\'emails')
plt.axis('equal')  # Assure que le pie chart est dessiné comme un cercle.
plt.show()

#Pour un graphique en barre (moins utile dans le cas présent) : 
labels = ['Phishing', 'Légitime']
sizes = [150, 850]

# Création du graphique à barres
plt.figure(figsize=(8, 6))
plt.bar(labels, sizes, color=['#ff9999','#66b3ff'])
plt.title('Proportions des différentes classes d\'emails')
plt.xlabel('Classe')
plt.ylabel('Nombre d\'emails')
plt.show()


#3. Analyse statistique :
print(csvfile.describe())