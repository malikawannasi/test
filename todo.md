# TODO - Améliorations et Raccourcis

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
