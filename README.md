# 🤖 AI Agents avec LangChain — Activité Pratique N°3

## 👩‍🎓 Réalisé par

* Étudiante en informatique / data / IA
* Projet : Agents intelligents avec LangChain + RAG

---

## 📌 Objectif du projet

Ce projet a pour objectif de :

* Comprendre le fonctionnement des agents IA avec LangChain
* Implémenter un agent simple
* Ajouter une mémoire conversationnelle
* Intégrer des outils (tools)
* Utiliser des middlewares (prompt dynamique, gestion d’erreurs, etc.)
* Développer un chatbot RAG (Retrieval-Augmented Generation)
* Créer une interface utilisateur avec Streamlit

---

## 🧱 Structure du projet

```
ai_agents_langchain_project/
│
├── agent_simple.py        # Agent de base
├── agent_memory.py        # Agent avec mémoire
├── agent_tools.py         # Agent avec outils
├── agent_middleware.py    # Agent avec middleware
├── rag_chatbot.py         # RAG en console
├── app.py                 # Interface Streamlit
│
├── data/
│   └── cours_ia.txt       # Document pour le RAG
│
├── requirements.txt       # Dépendances
├── .env                   # Clés API
└── README.md              # Documentation
```

---

## ⚙️ Installation

### 1. Cloner ou extraire le projet

```bash
cd ai_agents_langchain_project
```

---

### 2. Créer un environnement virtuel

```bash
python -m venv venv
```

---

### 3. Activer l’environnement

#### Windows (cmd) :

```bash
venv\Scripts\activate
```

#### Windows (PowerShell) :

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
.\venv\Scripts\Activate.ps1
```

---

### 4. Installer les dépendances

```bash
pip install -r requirements.txt
```

---

## 🔑 Configuration des clés API

Créer un fichier `.env` :

```env
OPENAI_API_KEY=ta_cle_openai
TAVILY_API_KEY=ta_cle_tavily
```

---

### 🔹 OpenAI

👉 https://platform.openai.com/api-keys

### 🔹 Tavily

👉 https://app.tavily.com

---

## 🚀 Exécution des scripts

### ▶️ Agent simple

```bash
python agent_simple.py
```

---

### ▶️ Agent avec mémoire

```bash
python agent_memory.py
```

---

### ▶️ Agent avec tools

```bash
python agent_tools.py
```

---

### ▶️ Agent avec middleware

```bash
python agent_middleware.py
```

---

### ▶️ RAG (console)

```bash
python rag_chatbot.py
```

---

### ▶️ Interface Streamlit

```bash
streamlit run app.py
```

Puis ouvrir dans le navigateur :

```
http://localhost:8501
```

---

## 🧠 Explication des modules

### 🔹 Agent simple

Un agent de base qui répond à des questions sans outils ni mémoire.

---

### 🔹 Mémoire

Permet à l’agent de garder le contexte de la conversation.

Exemple :

* "Je m'appelle Fatima"
* "Comment je m'appelle ?" → réponse correcte

---

### 🔹 Tools

Ajout de capacités externes :

* DuckDuckGo → recherche web
* Tavily → recherche avancée
* Python REPL → calculs

---

### 🔹 Middleware

Permet de contrôler le comportement de l’agent :

* Prompt dynamique
* Gestion des erreurs
* Guardrails (contrôle des réponses)
* Human-in-the-loop

---

### 🔹 RAG

Le chatbot utilise un document local pour répondre :

1. Chargement du document
2. Découpage en chunks
3. Création des embeddings
4. Stockage dans FAISS
5. Recherche pertinente
6. Génération de réponse

---

### 🔹 Streamlit

Interface web interactive permettant de :

* Poser des questions
* Voir les réponses
* Visualiser les documents utilisés

---

## 🧪 Exemple d’utilisation

Question :

```
Quelle est la différence entre machine learning et deep learning ?
```

Réponse :
→ basée sur le document `cours_ia.txt`

---

## ⚠️ Problèmes fréquents

### ❌ Erreur activation venv

➡ utiliser cmd ou changer ExecutionPolicy

---

### ❌ Clé API invalide

➡ vérifier `.env`

---

### ❌ FAISS erreur

```bash
pip install faiss-cpu
```

---

### ❌ Tavily ne fonctionne pas

➡ vérifier `TAVILY_API_KEY`

---

## 📊 Résultat attendu

✔ Agent simple fonctionnel
✔ Mémoire opérationnelle
✔ Tools intégrés
✔ Middleware utilisé
✔ RAG fonctionnel
✔ Interface Streamlit

---

## 🎯 Conclusion

Ce projet démontre comment :

* Construire des agents intelligents
* Intégrer des outils externes
* Gérer le contexte et les erreurs
* Implémenter un système RAG
* Déployer une interface utilisateur simple

LangChain permet ainsi de créer des applications IA avancées de manière modulaire et extensible.

---

## ⭐ Bonus

Possibilités d’amélioration :

* Ajouter PDF comme source RAG
* Ajouter base de données
* Ajouter chat multi-utilisateurs
* Déployer sur le cloud

---

## 📌 Auteur

Projet réalisé dans le cadre d’un TP LangChain.
KHALID NAITALI

---
