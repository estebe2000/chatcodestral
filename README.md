# chatcodestral
# 🤖 Codestral Chatbot

Un chatbot léger et puissant conçu pour l'assistance au codage, propulsé par le modèle **Codestral** de Mistral AI.

Ce projet démontre comment interagir directement avec l'API de Mistral via des requêtes HTTP brutes, en utilisant les endpoints de chat et de complétion de code (FIM - Fill In the Middle).

## 🚀 Fonctionnalités

* **Assistant de Chat :** Posez des questions sur la programmation, l'algorithmique ou l'architecture logicielle.
* **Complétion de Code (FIM) :** Capacité à compléter des bouts de code manquants (Fill-In-the-Middle) via l'endpoint dédié.
* **Léger :** Aucune dépendance lourde, utilise des requêtes API directes.

## 🛠️ Prérequis

* Python 3.8 ou supérieur
* Une clé API Mistral (Codestral est gratuit en phase de beta/test via [La Console Mistral](https://console.mistral.ai/codestral))

## 📦 Installation

1.  **Clonez le dépôt :**
    ```bash
    git clone [https://github.com/votre-nom-utilisateur/codestral-chatbot.git](https://github.com/votre-nom-utilisateur/codestral-chatbot.git)
    cd codestral-chatbot
    ```

2.  **Installez les dépendances :**
    ```bash
    pip install requests python-dotenv
    ```

3.  **Configuration de la Clé API :**
    * Créez un fichier `.env` à la racine du projet.
    * Ajoutez votre clé API (Ne commitez jamais ce fichier !) :
    ```env
    MISTRAL_API_KEY=votre_cle_api_ici
    ```

## ⚙️ Configuration des Endpoints

Ce bot est configuré pour utiliser les endpoints spécifiques de Codestral :

| Type | Endpoint URL | Description |
| :--- | :--- | :--- |
| **Chat** | `https://codestral.mistral.ai/v1/chat/completions` | Pour la conversation standard |
| **FIM** | `https://codestral.mistral.ai/v1/fim/completions` | Pour l'auto-complétion de code |

## 💻 Utilisation

Pour lancer le chatbot dans votre terminal :

```bash
python main.py
