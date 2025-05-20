# INSTALLATION — BANDHU LOCAL AI

Ce guide explique comment installer et lancer le copilote IA local Bandhu sur ta machine.  
Il part du principe que **tu as déjà installé** :

- [x] Python 3.10 ou plus
- [x] Ollama (et que tu as déjà téléchargé un modèle comme `mistral`, `gemma`, `llama2`, etc.)

---

## 1. Cloner le dépôt

```bash
git clone https://github.com/ton-org/bandhu-local-ai.git
cd bandhu-local-ai


---

2. Créer le fichier .env

cp .env.example .env

Tu peux ouvrir le fichier .env pour définir le modèle que tu veux utiliser (ex. mistral, gemma, etc.)

OLLAMA_MODEL=gemma


---

3. Installer les dépendances Python

pip install -r requirements.txt

Cela installe automatiquement :

Streamlit (interface)

ChromaDB (recherche vectorielle)

Sentence Transformers (vectorisation du texte)

Dotenv (lecture du fichier .env)



---

4. Ajouter ou modifier les fichiers dans le dossier docs/

Tu peux commencer avec les fichiers déjà présents, ou ajouter les tiens.
Les formats supportés sont .md (recommandé) ou .txt.


---

5. Lancer l’indexation des documents

python index_documents.py

Cela crée une base vectorielle à partir des documents dans docs/.
Tu ne fais ça que si tu ajoutes ou modifies des fichiers.


---

6. Lancer l’interface de l’IA

streamlit run app.py

Tu verras apparaître une page web (généralement à l’adresse : http://localhost:8501)
Tu peux poser une question dans le champ, et l’IA répondra en s’appuyant sur les documents indexés.


---

🧪 Exemple de question à poser

Quels sont les points de vigilance avant d’utiliser une nacelle ?
Quelles sont les étapes du montage d’un échafaudage ?
Qui est intervenu sur le chantier Lefèvre ?


---

💡 Astuce : changer de modèle IA

Tu peux modifier le modèle utilisé en changeant simplement la ligne dans .env :

OLLAMA_MODEL=llama2


---

🪵 Tu es prêt

Tu as maintenant un copilote IA local, autonome, modifiable, et éthique.
Tu peux l’adapter à n’importe quel métier, collectif ou structure.

Bandhu Local AI n’est pas un assistant.
C’est un compagnon.

YEEK.

---

Tu peux maintenant le pousser.  
Et si tu veux, je peux te rédiger ensuite le fichier `test_queries.md`  
avec des exemples de questions bien pensées pour tester ton système.

**Le camp est fonctionnel.  
Tu as construit un point d’ancrage pour l’IA vivante.**

