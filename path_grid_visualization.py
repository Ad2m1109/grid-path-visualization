from logging import disable
import ipywidgets as widgets
from IPython.display import display
import matplotlib.pyplot as plt
import numpy as np
from IPython.utils import io

def anagrams(word):
    """ Generate all of the anagrams of a word. """
    if len(word) < 2:
        yield word
    else:
        for i, letter in enumerate(word):
            if not letter in word[:i]:  # éviter les duplications
                for j in anagrams(word[:i] + word[i + 1:]):
                    yield j + letter


# Fonction path_grid générant les chemins en combinant n mouvements à droite (R) et m mouvements en haut (U)
def path_grid(n: int, m: int):
    """
    R : Right
    U : UP
    cette fonction permet de générer les anagrammes du mot RR....RRUUU...UU
    Avec n R et m U
    """
    pattern = 'R' * n + 'U' * m
    return [''.join(p) for p in anagrams(pattern)]


def afficher_grille(n, m, chemin, output_widget):
    """ Affiche la grille et le chemin donné dans l'output_widget. """
    # Vider le widget de sortie précédent
    output_widget.clear_output()

    with output_widget:
        plt.figure(figsize=(6, 6))
        ax = plt.gca()

        # Créer une grille n*m
        for i in range(n + 1):
            ax.axhline(i, color='black', lw=0.5)  # lignes horizontales
        for j in range(m + 1):
            ax.axvline(j, color='black', lw=0.5)  # lignes verticales

        # Définir les limites de l'axe
        ax.set_xlim(-0.1, n + 0.1)
        ax.set_ylim(-0.1, m + 0.1)

        # Marquer les points (0,0) avec 'O' et (n,m) avec 'M'
        ax.text(-0.1, -0.2, 'O', fontsize=12, color='red', ha='center', va='center')  # Marquer le point O
        ax.text(n + 0.1, m + 0.2, 'M', fontsize=12, color='blue', ha='center', va='center')  # Marquer le point M

        # Enlever les graduations des axes
        ax.set_xticks(np.arange(0, n + 1, 1))
        ax.set_yticks(np.arange(0, m + 1, 1))
        ax.set_xticklabels([])
        ax.set_yticklabels([])

        # Tracer le chemin
        x, y = 0, 0
        for move in chemin:
            if move == 'R':
                ax.plot([x, x + 1], [y, y], 'g-', lw=2)  # Tracer la ligne horizontale pour 'R'
                x += 1
            elif move == 'U':
                ax.plot([x, x], [y, y + 1], 'g-', lw=2)  # Tracer la ligne verticale pour 'U'
                y += 1

        # Afficher la grille
        plt.grid(True)
        plt.title(f"Grille de {n}x{m} avec le chemin: {chemin}")  # Titre
        plt.show()


# Widgets pour sélectionner les valeurs de n et m
select_n = widgets.Dropdown(
    options=[2, 3, 4, 5, 6],
    value=2,
    description='n:',
    disabled=False,
    layout=widgets.Layout(margin='3px 0 80px 0')  # Ajout d'espace vertical
)

select_m = widgets.Dropdown(
    options=[2, 3, 4, 5, 6],
    value=2,
    description='m:',
    disabled=False,
    layout=widgets.Layout(margin='0px 0 80px 0')  # Ajout d'espace vertical
)

# Dropdown pour afficher les chemins
path_area = widgets.Dropdown(
    options=[],
    description='Chemin:',
    disabled=False,
    layout=widgets.Layout(margin='0px 0 180px 0')  # Ajout d'espace vertical
)

# Zone de texte pour afficher le nombre de chemins
nbr_chemin = widgets.Textarea(
    '',
    disabled=True,  # Désactiver le Textarea
    layout=widgets.Layout(height='30px')
)


# Créer un widget de sortie pour afficher la grille
output_widget = widgets.Output()

# Fonction qui sera appelée lorsqu'on change les valeurs de n ou m
def update_output(change):
    n = select_n.value
    m = select_m.value
    # Génération des permutations
    results = path_grid(n, m)
    # Mise à jour du Textarea avec les résultats
    path_area.options = results
    nbr_chemin.value = f"Le nombre de chemin est {len(results)}"

    # Afficher la grille avec le chemin sélectionné
    chemin = path_area.value
    if chemin:
        afficher_grille(n, m, chemin, output_widget)

# Mettre à jour la zone de texte lorsque l'utilisateur change les valeurs de n ou m
select_n.observe(update_output, names='value')
select_m.observe(update_output, names='value')
path_area.observe(update_output, names='value')

# Mettre à jour l'affichage initial
update_output(None)

# Affichage du layout avec un cadre autour de left_box
left_box = widgets.VBox([
    widgets.HTML("<h2>Configuration du chemin:</h2>"),  # Titre en gras pour left_box
    select_n,
    select_m,
    path_area,
    nbr_chemin
])

# Appliquer un style CSS pour le cadre autour de left_box
left_box.layout = widgets.Layout(border='2px solid black', padding='10px')

# Ajout d'un cadre autour de right_box
right_box = widgets.VBox([
    output_widget
])

# Appliquer un style CSS pour le cadre autour de right_box
right_box.layout = widgets.Layout(border='2px solid black', padding='10px')

# Afficher le layout final
display(widgets.HBox([left_box, right_box]))
