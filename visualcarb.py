import matplotlib.pyplot as plt 

def bar_carb(A,x_name,y_name,title):
    X = list(A.keys())
    Y = list(A.values())
    
    # Création du diagramme en bâtons
    plt.figure(figsize=(10, 6))  # Définir la taille de la figure
    plt.bar(X, kg, color='skyblue')
    
    # Ajout de titres et labels
    plt.title(title, fontsize=16)
    plt.xlabel(x_name, fontsize=14)
    plt.ylabel(y_name, fontsize=14)
    plt.xticks(rotation=45)
    # Afficher le diagramme
    plt.show()