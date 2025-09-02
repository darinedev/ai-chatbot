# **🤖 Simple AI Chatbot**
Un chatbot simple en Python qui peut utiliser différentes APIs d'IA (OpenAI, Groq) ou fonctionner en mode simulation.
## **📁 Structure du Projet**
ai-chatbot/
│
├── main.py              # Code principal du chatbot
├── requirements.txt     # Dépendances Python
├── .env.example        # Exemple de fichier d'environnement
├── .gitignore          # Fichiers à ignorer par Git
└── README.md           # Ce fichier
## **🚀 Installation**
### 1- Cloner le repository :
- git clone https://github.com/votre-username/ai-chatbot.git
- cd ai-chatbot
### 2- Créer un environnement virtuel :
- python -m venv venv
source venv/bin/activate  # Linux
### 3- Installer les dépendances :
- pip install -r requirements.txt
### 4- Configurer les variables d'environnement :
- cp .env.example .env
# Éditez .env avec vos clés API (optionnel)

## **🎯 Utilisation**
*Mode Simulation (par défaut - aucune API requise)*
- python main.py
# Avec une API réelle
Modifiez la variable provider dans main.py :

- "simulation" : Mode test sans API
- "openai" : Utilise OpenAI (nécessite une clé API)
- "groq" : Utilise Groq (gratuit, nécessite inscription)
**🔧 Configuration**
# Pour utiliser Groq (gratuit) :

- Inscrivez-vous sur groq.com
- Récupérez votre clé API
- Ajoutez dans votre .env :
GROQ_API_KEY=votre_clé_ici



# Pour utiliser OpenAI :
- Ajoutez dans votre .env :
OPENAI_API_KEY=votre_clé_ici
## **🤝 Contribution**
Les contributions sont les bienvenues ! N'hésitez pas à :

- Signaler des bugs
- Proposer des améliorations
- Ajouter de nouvelles fonctionnalités