## Guide d'utilisation 

Voici les étapes pour utiliser Docasis :

### 1. Importer vos documents

![Onglet Indexation de fichiers](https://raw.githubusercontent.com/Cinnamon/kotaemon/main/docs/images/file-index-tab.png)

Pour commencer, vous devez importer les documents que vous souhaitez interroger dans l'application. Rendez-vous dans l'onglet **Fichiers** :

*   **Importation de fichiers :**
    *   Glissez-déposez vos fichiers ou sélectionnez-les depuis votre ordinateur.
    *   Cliquez sur **Télécharger et indexer**.
    *   L'application traitera les fichiers et affichera un message une fois le traitement terminé.

*   **Liste des fichiers :**
    *   Cette section affiche la liste de vos documents importés, et vous permet de les supprimer si nécessaire.

### 2. Échanger avec vos documents

![Onglet Chat](https://raw.githubusercontent.com/Cinnamon/kotaemon/main/docs/images/chat-tab.png)

Dans l'onglet **Conversations**, vous pouvez interagir avec le chatbot et lui poser des questions sur vos documents :

1.  **Panneau des paramètres de conversation**

    *   Vous pouvez y créer, sélectionner, renommer ou supprimer des conversations.
    *   Une nouvelle conversation est créée automatiquement si aucune n'est sélectionnée.
    *   Vous pouvez choisir les documents à utiliser comme contexte pour le chatbot.
        *   En sélectionnant **Désactiver**, aucun document n'est utilisé comme contexte.
        *   En sélectionnant **Rechercher tout**, tous les documents seront utilisés comme contexte.
        *   En sélectionnant **Sélectionner**, vous pourrez choisir les documents à utiliser. Si aucun document n'est sélectionné, aucun document ne sera utilisé comme contexte.
2.  **Panneau de conversation**

    *   C'est ici que vous échangez avec le chatbot.
3.  **Panneau d'informations**

    *   Ce panneau affiche des informations contextuelles liées aux réponses du chatbot, comme les sources ou le score de pertinence.
    *   Les passages cités du document source sont mis en évidence pour vérifier l'exactitude de la réponse.

    **Signification des scores :**

    *   **Confiance de la réponse** : niveau de confiance du modèle de langage concernant sa réponse.
    *   **Score de pertinence** : niveau de pertinence général de la source par rapport à votre question.
    *   **Score Vectorstore** : niveau de correspondance de la source à votre question via la similarité des embeddings de texte (indique "recherche plein-texte" si la source est récupérée d'une recherche de mots-clés).
    *   **Score de pertinence LLM** : niveau de pertinence de la source par rapport à votre question évalué par un modèle de langage.
    *   **Score de reranking** : niveau de pertinence de la source via un modèle de reranking (Cohere).

    En général, la qualité des scores est la suivante : `Score de pertinence LLM > Score de reranking > Score Vectorstore`. Le score de pertinence général est calculé à partir du score de pertinence LLM. Les sources sont triées par score de pertinence et sont favorisées si elles ont été citées par le chatbot.

### 3. Personnaliser vos paramètres

Vous pouvez personnaliser le comportement de l'application en modifiant les paramètres disponibles dans l'onglet **Réglages**.