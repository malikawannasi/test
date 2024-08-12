# TODO - Améliorations et Raccourcis
# TODO

## Améliorations

1. **Configurer le fichier Swagger** :
   - Vérifier et ajuster les définitions des routes et des modèles dans le fichier Swagger (swagger.yaml / swagger.json).
   - S'assurer que toutes les informations nécessaires sont bien documentées et cohérentes.

2. **Intégrer Swagger UI** :
   - Ajouter ou mettre à jour la configuration de Swagger UI pour qu'il pointe vers le fichier Swagger correct.
   - Tester l'affichage de l'API dans Swagger UI pour vérifier que toutes les routes et les détails sont correctement rendus.

3. **Personnaliser le CSS** :
   - Modifier le style par défaut de Swagger UI pour qu'il corresponde aux directives de style du projet.
   - Ajouter des règles CSS personnalisées pour améliorer l'apparence et la lisibilité de l'interface Swagger UI.

## Raccourcis

- **Vérification rapide du fichier Swagger** : Utiliser des outils comme Swagger Editor pour valider le fichier Swagger avant intégration.
- **Tests locaux de Swagger UI** : Lancer un serveur local avec Swagger UI pour tester les modifications avant de déployer sur un serveur de staging.
- **Utilisation des variables d'environnement** : Configurer Swagger UI pour qu'il puisse utiliser des variables d'environnement pour l'URL du fichier Swagger en développement et en production.

## Améliorations à Apporter

1. **Validation des Données Entrantes**
   - Ajouter une validation plus stricte pour les données entrantes, par exemple pour vérifier que les valeurs poussées dans la pile sont des nombres valides.
   
2. **Gestion des Erreurs Avancée**
   - Implémenter une gestion des erreurs plus détaillée et des messages d'erreur plus explicites pour une meilleure expérience utilisateur.

3. **Tests Unitaires**
   - Écrire des tests unitaires pour toutes les fonctions de l'API afin d'assurer leur bon fonctionnement et leur robustesse.

4. **Authentification et Autorisation**
   - Ajouter un mécanisme d'authentification et d'autorisation pour sécuriser l'accès aux opérations sur les piles.

5. **Documentation Complète**
   - Améliorer la documentation Swagger pour inclure des descriptions plus détaillées des paramètres et des réponses.

6. **Optimisation des Performances**
   - Optimiser le code pour gérer plus efficacement les grandes quantités de données dans les piles.

## Raccourcis Prises

1. **Aucune Fonction de Sauvegarde Persistante**
   - Les piles ne sont pas sauvegardées de manière persistante (par exemple, en base de données). Les données sont perdues lorsque l'application est arrêtée.

2. **Aucune Interface Utilisateur Graphique**
   - Pas de frontend pour interagir avec l'API, uniquement des endpoints REST.

3. **Validation Minimale des Entrées**
   - La validation des entrées est minimale, ce qui pourrait entraîner des erreurs non détectées si des données incorrectes sont envoyées à l'API.

4. **Pas de Gestion Avancée des Sessions**
   - Aucune gestion des sessions ou des utilisateurs, ce qui limite la personnalisation et la sécurité des opérations sur les piles.
