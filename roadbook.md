*Rendu des slides:* **7 juin 2023**

## Janvier
Le code avance peu à cause de difficultés sur la partie image pyramid et sliding window. Problèmes avec les tailles d’image. Il faut mieux les définir, tout ça doit être secondaire.
Commencer à se pencher sur la partie théorique des SVM avec le livre.

## Février
Afin d’avancer, on met momentanément de côté la pyramide d’images. Pour l’instant, la taille de la sliding window doit un peu être ajustée manuellement.
Il faut implémenter l’algorithme de non-maximum suppression.
Ensuite, il faudra entraîner un nouveau modèle, en faisant attention aux données d’entraînement, et faire du hard negative mining.

## Mars
On a implémenté l’algorithme de non-maximum suppression. À voir s’il est intéressant d’utiliser la version Soft NMS.
Il faut entraîner un nouveau modèle, plus performant.
Le modèle qu’on utilisait jusque là a été entraîné avec P=13233 visages et N=30000 patches négatifs (mais seulement 10 images). Pas certain de la pertinence des patches négatifs utilisés. -> une des 10 images représentait des pièces dont la face présentait un visage. C’étaient donc des hard negative examples important. C’est un point sur lequel on doit être attentif.

model_01 correspond au tout premier modèle
model_02 au deuxième, entraîné avec un img_to_use qui ne contient plus d’image où des zones peuvent ressembler à un visage.
Mise en place d’un premier jeu de test (21 images).
Il faut évaluer les performances de model_02 sur ce jeu et garder une trace, avant de faire du hnm.
