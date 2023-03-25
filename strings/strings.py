# Les chaînes de caractères en Python

# Les chaînes de caractères s'écrivent entre guillemets simples ou doubles
ma_chaine_simple = 'Bonjour'
ma_chaine_double = "Bonjour"

# Les chaînes de caractères avec guillemets doubles
# peuvent contenir des guillemets simples
ma_chaine_double = "C'est un bon jour"

# Les chaînes de caractères avec guillemets simples
# peuvent contenir des guillemets doubles sinon
# il faut "échapper" le guillemet double avec un \
ma_chaine_simple = 'Il a dit "Bonjour"'
ma_chaine_double = "Il a dit \"Bonjour\""

# Les chaînes de caractères peuvent être concaténées
# avec l'opérateur +
ma = "Bonjour"
chaine = "Hadrien"
ma_chaine = ma + " " + chaine # Bonjour Hadrien

# Les chaînes de caractères peuvent être répétées
# avec l'opérateur *
ma_chaine = "Bonjour " * 3 # Bonjour Bonjour Bonjour

# On peut accéder à un caractère d'une chaîne de caractères
# avec l'opérateur [] en précisant l'indice du caractère (commence à 0)
ma_chaine = "Bonjour"
ma_chaine[0] # B
ma_chaine[1] # o
ma_chaine[5] # u

# On peut accéder à la longueur d'une chaîne de caractères
# avec la fonction len()
ma_chaine = "Bonjour"
len(ma_chaine) # 7

# On peut accéder à un sous-ensemble de caractères
# avec l'opérateur [début:fin] en précisant l'indice du début
# et l'indice de fin (exclu)
ma_chaine = "Bonjour"
ma_chaine[0:3] # Bon

# On peut accéder à un sous-ensemble de caractères
# avec l'opérateur [début:fin:pas] en précisant l'indice du début
# et l'indice de fin (exclu) et le pas
ma_chaine = "Bonjour"
ma_chaine[0:7:2] # Bnor

# On peut découper une chaîne de caractères en une liste de chaînes
# avec la méthode split()
ma_chaine = "Bonjour Hadrien"
ma_chaine.split() # ['Bonjour', 'Hadrien']
ma_chaine_virgule = "Ambre,Hadrien,Édouard"
ma_chaine_virgule.split(",") # ['Ambre', 'Hadrien', 'Édouard']

# On peut remplacer un caractère ou une chaîne de caractères
# dans une chaîne de caractères avec la méthode replace()
ma_chaine = "Bonjour Hadrien"
ma_chaine.replace("Hadrien", "Ambre") # Bonjour Ambre

# On ne peut pas modifier une chaîne de caractères en Python
# il faut donc mettre le résultat dans une nouvelle variable
# ou réaffecter la variable
ma_chaine = "Bonjour Hadrien"
ma_nouvelle_chaine = ma_chaine.replace("Hadrien", "Ambre")
ma_chaine # Bonjour Hadrien
ma_nouvelle_chaine # Bonjour Ambre

# Les chaînes de caractères contiennent des caractères spéciaux
# comme les retours à la ligne '\n' ou les tabulations '\t' (gros espace)
ma_chaine = "Bonjour\n\tHadrien"
print(ma_chaine) # Bonjour
                 #     Hadrien
