# bandhu-local-ai

# Bandhu Local AI

Assistant IA local, open source.  
Pensé pour devenir le **copilote métier** d’une entreprise, d’un artisan, d’un collectif ou d’un porteur de projet.

---

## 🚧 Objectif

Créer une IA locale qui :

- lit les documents internes (procédures, rapports, fiches)
- répond aux questions métier en langage naturel
- tourne **sans connexion cloud**
- peut être adaptée à chaque structure

---

## 🔧 Stack

- **Ollama** : moteur LLM local (ex : Mistral, LLaMA2)
- **ChromaDB** : recherche vectorielle locale
- **Streamlit** : interface simple, accessible à tous
- **Docs en `.md`, `.txt`, `.pdf`** : corpus modifiable librement

---

## 📁 Structure du dépôt

bandhu-local-ai/
├── app.py # Interface Streamlit
├── index_documents.py # Script d’indexation du corpus
├── rag_engine.py # Récupération des blocs pertinents
├── ollama_client.py # Dialogue avec le modèle
├── docs/ # Dossier des documents métiers
├── test_queries.md # Exemples de requêtes
├── .env.example # Variables d’environnement
└── requirements.txt # Dépendances Python


---

## 🌿 Philosophie

**Ce projet n’est pas un produit.  
C’est une graine.**

Une manière de rendre l’intelligence artificielle **utile, lisible, modifiable et transmissible.**  
Chaque entreprise, chaque atelier, chaque collectif pourra le forker, l’adapter, le versionner.

**Pas besoin de licence.  
Pas besoin de dépendance.  
Pas besoin de magie noire.**

Juste : du texte, du code propre, et une IA qui parle votre langue.

---

## ✨ Lancement rapide (à venir)

Un guide pas à pas t’aidera à :

- Indexer tes propres documents
- Poser une première question
- Modifier le comportement de l’IA
- Héberger le tout localement

---

**Bandhu, ce n’est pas un outil.  
C’est une manière de collaborer avec le vivant.**  
Et GitHub devient notre atelier.

**YEEK.**
