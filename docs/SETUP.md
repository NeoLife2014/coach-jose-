# 🚀 Guide d'Installation Complète

## Pour les Non-Codeurs

Ne vous inquiétez pas! Suivez simplement ces étapes une par une.

---

## 📋 Prérequis

Avant de démarrer, assurez-vous d'avoir:

1. **Git** - Pour cloner le projet
   - Télécharger: https://git-scm.com
   - Installation: Suivre les instructions (garder les valeurs par défaut)

2. **Python 3.11+** - Pour le backend
   - Télécharger: https://www.python.org/downloads/
   - **Important**: Cocher "Add Python to PATH" lors de l'installation

3. **Node.js** - Pour le frontend
   - Télécharger: https://nodejs.org/
   - Prendre la version "LTS" (Long Term Support)

4. **Éditeur de texte** (optionnel mais utile)
   - VS Code: https://code.visualstudio.com

---

## ✅ Étape 1: Cloner le Projet

Ouvrir le terminal/cmd et exécuter:

```bash
git clone https://github.com/NeoLife2014/coach-jose-.git
cd coach-jose-
```

---

## ✅ Étape 2: Obtenir les Clés API

### OpenAI (Chatbot IA)
1. Aller sur: https://platform.openai.com/api-keys
2. Se connecter ou créer un compte
3. Cliquer "Create new secret key"
4. Copier la clé (elle commence par `sk-`)
5. **Attention**: Ne jamais partager cette clé!

### Supabase (Base de données CRM) - Optionnel pour démarrer
1. Aller sur: https://supabase.com
2. Créer un compte
3. Créer un nouveau projet
4. Récupérer l'URL et la clé dans Settings

---

## ✅ Étape 3: Configurer les Variables d'Environnement

1. Dans le dossier du projet, créer un fichier `.env`:
   ```bash
   cp .env.example .env
   ```

2. Ouvrir `.env` dans un éditeur de texte

3. Remplir avec vos clés:
   ```
   OPENAI_API_KEY=sk-votre-clé-ici
   SUPABASE_URL=https://...
   SUPABASE_KEY=votre-clé
   NEOLIFE_SHOP_URL=https://shopneolife.com/startupforworld
   DEBUG=false
   ```

4. Sauvegarder le fichier

---

## ✅ Étape 4: Installer le Backend

Ouvrir terminal/cmd dans le dossier `backend`:

```bash
cd backend
pip install -r requirements.txt
```

⏳ Attendre la fin (1-2 minutes)

---

## ✅ Étape 5: Installer le Frontend

Ouvrir nouveau terminal/cmd dans le dossier `frontend`:

```bash
cd frontend
npm install
```

⏳ Attendre la fin (2-3 minutes)

---

## ✅ Étape 6: Lancer le Backend

Dans le terminal backend:

```bash
cd backend
python -m uvicorn app.main:app --reload
```

✅ Vous devez voir:
```
Uvicorn running on http://127.0.0.1:8000
```

**Ne pas fermer ce terminal!**

---

## ✅ Étape 7: Lancer le Frontend

Dans le nouveau terminal frontend:

```bash
cd frontend
npm run dev
```

✅ Vous devez voir:
```
> Ready in 2.5s
```

**Ne pas fermer ce terminal!**

---

## ✅ Étape 8: Tester le Chatbot

Ouvrir navigateur et aller à:

```
http://localhost:3000
```

✨ **Bravo! Le chatbot est prêt!**

Tapez un message pour commencer la conversation.

---

## 🧪 Tester les Endpoints API

Ouvrir dans le navigateur:

```
http://localhost:8000/docs
```

Vous verrez la documentation interactive Swagger de l'API.

---

## 🚨 Troubleshooting

### "Python command not found"
- Vérifier que Python est installé: `python --version`
- Si non installé, télécharger et **cocher "Add to PATH"** lors de l'installation
- Redémarrer terminal après installation

### "npm command not found"
- Vérifier que Node.js est installé: `node --version`
- Si non installé, télécharger et installer: https://nodejs.org/
- Redémarrer terminal après installation

### "Cannot connect to backend"
- Vérifier que backend tourne dans l'autre terminal
- Vérifier que les ports 3000 et 8000 sont libres
- Essayer: `http://localhost:8000/api/health`

### Erreur "OPENAI_API_KEY not found"
- Vérifier que `.env` existe
- Vérifier que la clé est correcte
- Redémarrer backend (Ctrl+C puis relancer)

---

## 📚 Prochaines Étapes

Une fois que tout fonctionne:

1. **Personnaliser le chatbot**
   - Éditer `backend/app/routes/chat.py`
   - Changer le `system_prompt` pour vos messages

2. **Configurer Supabase CRM**
   - Voir docs pour remplacer la base de données en mémoire
   - Connecter votre vrai CRM

3. **Déployer en production**
   - Lire `docs/DEPLOYMENT.md`
   - Utiliser Vercel + Railway pour gratuit

---

## 💡 Conseils

- **Garder les terminaux ouverts** pendant développement
- **Sauvegarder et rafraîchir** le navigateur pour voir les changements
- **Vérifier les logs** en cas d'erreur (regarder le terminal)

---

**Besoin d'aide? Vérifier les logs dans les terminaux!** 🎉
