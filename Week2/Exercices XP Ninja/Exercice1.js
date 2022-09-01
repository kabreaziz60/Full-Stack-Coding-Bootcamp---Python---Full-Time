// Exercice 1 : Vérification De L'IMC
// Des Instructions
// Astuce :
// - Vous devez utiliser des fonctions pour réaliser cet exercice, pour cela jetez un œil à la leçon de demain.
// Créez deux objets, chaque objet doit contenir les détails d'une personne. Voici les détails:
// Nom et prénom
// Masse
// Hauteur
// Chaque objet doit également avoir une clé dont la valeur est une fonction (c'est-à-dire une méthode), qui calcule l'indice de masse corporelle (IMC) de chaque personne
// En dehors des objets, créez une fonction JS qui compare l'IMC des deux objets.
// Affichez le nom de la personne qui a le plus grand IMC.

let etudiant ={
    Nom : kabre,
    Prenom : bibi,
    Masse : 64,
    Hauteur : 1.85,
}
function maFonction1(etudiant){
    let IMCe= Masse/(Hauteur*Hauteur);
    return IMCe;
}
maFonction1(etudiant);
let prof={
    Nom : lingani,
    Prenom : malick,
    Masse : 70,
    Hauteur : 1.75,
}