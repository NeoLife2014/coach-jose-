# 📋 Coach José - Documentation Complète

## 🎯 Vue d'ensemble

**Coach José** est un **chatbot IA conversationnel** conçu pour :
- ✅ Attirer et engager les prospects
- ✅ Expliquer les produits Neolife de manière automatisée
- ✅ Capturer les leads (email, téléphone, nom)
- ✅ Rediriger vers votre boutique Neolife

---

## 🚀 Démarrage Rapide

### 1. Cloner le projet
```bash
git clone https://github.com/NeoLife2014/coach-jose-.git
cd coach-jose-
```

### 2. Installer les dépendances

**Backend:**
```bash
cd backend
pip install -r requirements.txt
```

**Frontend:**
```bash
cd frontend
npm install
```

### 3. Configurer les variables d'environnement

```bash
cp .env.example .env
```

Éditer `.env` et ajouter:
```
OPENAI_API_KEY=sk-your-openai-key-here
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-supabase-key
NEOLIFE_SHOP_URL=https://shopneolife.com/startupforworld
FRONTEND_URL=http://localhost:3000
DEBUG=false
```

### 4. Lancer localement

**Terminal 1 - Backend:**
```bash
cd backend
python -m uvicorn app.main:app --reload
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```

Visitez: **http://localhost:3000** 🎉

---

## 📁 Structure du Projet

```
coach-jose/
├── backend/                    # API FastAPI (Python)
│   ├── app/
│   │   ├── main.py            # Application principale
│   │   ├── config.py          # Configuration
│   │   └── routes/
│   │       ├── chat.py        # Endpoint chatbot GPT-4
│   │       ├── leads.py       # Gestion CRM
│   │       └── health.py      # Health checks
│   ├── requirements.txt        # Dépendances
│   └── Dockerfile             # Image Docker
│
├── frontend/                   # Application Next.js (React)
│   ├── pages/
│   │   ├── index.tsx          # Page chatbot principale
│   │   ├── dashboard.tsx      # Dashboard admin
│   │   └── _app.tsx           # Configuration globale
│   ├── package.json           # Dépendances NPM
│   ├── next.config.js         # Config Next.js
│   ├── tsconfig.json          # Config TypeScript
│   └── tailwind.config.js     # Styles Tailwind
│
├── docs/                       # Documentation
│   ├── SETUP.md               # Guide installation
│   ├── API.md                 # Documentation API
│   └── DEPLOYMENT.md          # Guide déploiement
│
├── docker-compose.yml         # Orchestration Docker
├── .env.example              # Template .env
└── README.md                 # Ce fichier
```

---

## 🔧 Configuration

### Variables d'Environnement Requises

| Variable | Description | Exemple |
|----------|-------------|---------|
| `OPENAI_API_KEY` | Clé API OpenAI | `sk-...` |
| `SUPABASE_URL` | URL Supabase | `https://xxx.supabase.co` |
| `SUPABASE_KEY` | Clé API Supabase | `eyJ0...` |
| `NEOLIFE_SHOP_URL` | Lien boutique Neolife | `https://shopneolife.com/startupforworld` |
| `FRONTEND_URL` | URL du frontend | `http://localhost:3000` |
| `DEBUG` | Mode debug | `false` |

---

## 📊 Flux de Conversion

```
┌─────────────────┐
│   Prospect      │
│   visite site   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Chatbot IA      │
│ (GPT-4)         │
│ Questions →     │
│ Réponses        │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Capture Lead    │
│ Email/Téléphone │
│ CRM             │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Redirect Shop   │
│ Neolife         │
│ VENTE! 💰       │
└─────────────────┘
```

---

## 🎯 Endpoints API

### Chat
- `POST /api/chat/message` - Envoyer message au chatbot
- `GET /api/chat/info` - Info chatbot

### Leads
- `POST /api/leads/capture` - Capturer un lead
- `GET /api/leads/list` - Lister les leads
- `GET /api/leads/{id}` - Détails d'un lead
- `POST /api/leads/{id}/status` - Mettre à jour le status

### Health
- `GET /api/health` - Health check

Voir **`docs/API.md`** pour la documentation complète.

---

## 🐳 Docker

### Lancer avec Docker Compose

```bash
docker-compose up -d
```

### Accès
- Frontend: http://localhost:3000
- Backend: http://localhost:8000
- Docs API: http://localhost:8000/docs

---

## 📦 Déploiement Production

### Option 1: Vercel (Frontend) + Railway (Backend) ⭐

**Frontend (Vercel):**
1. Aller sur https://vercel.com
2. Importer repo GitHub
3. Configurer `NEXT_PUBLIC_API_URL`
4. Déployer

**Backend (Railway):**
1. Aller sur https://railway.app
2. Créer nouveau projet
3. Connecter GitHub repo
4. Ajouter variables d'env
5. Déployer

Voir **`docs/DEPLOYMENT.md`** pour détails complets.

---

## 💡 Fonctionnalités

✅ **Chatbot IA Intelligent**
- Conversations naturelles avec GPT-4
- Réponses personnalisées pour Neolife
- Historique conversations

✅ **Capture de Leads**
- Formulaire intégré
- Stockage CRM (Supabase)
- Export données

✅ **Dashboard**
- Statistiques conversions
- Gestion leads
- Historique interactions

✅ **Production-Ready**
- Scalable
- Sécurisé
- Dockerisé
- CORS configuré

---

## 🔐 Sécurité

- ✅ Variables d'env protégées
- ✅ CORS configuré
- ✅ Validation données
- ✅ Rate limiting (à ajouter)
- ✅ HTTPS en production

---

## 💰 Coûts Estimés

| Service | Coût |
|---------|------|
| Vercel (Frontend) | ✅ Gratuit |
| Railway (Backend) | ✅ Gratuit |
| Supabase (CRM) | ✅ Gratuit (500k req) |
| OpenAI (GPT-4) | $5-20/mois |
| **TOTAL** | **$5-20/mois** |

---

## 🆘 Troubleshooting

### Erreur: "Cannot connect to backend"
- Vérifier que backend tourne: `http://localhost:8000/api/health`
- Vérifier `NEXT_PUBLIC_API_URL` dans `.env`

### Erreur: "OPENAI_API_KEY not found"
- Vérifier clé dans `.env`
- Redémarrer backend: `Ctrl+C` puis relancer

### Erreur: "Supabase connection failed"
- Vérifier URL et clé Supabase
- Vérifier que projet Supabase est actif

---

## 📚 Documentation Complète

- **SETUP.md** - Installation détaillée
- **API.md** - Référence complète des endpoints
- **DEPLOYMENT.md** - Guide déploiement production

---

## 🤝 Support

Pour toute question ou problème:
1. Lire la documentation
2. Vérifier les logs: `docker logs coach-jose-backend`
3. Consulter DEPLOYMENT.md pour troubleshooting

---

## 📄 Licence

Propriétaire - Neolife International

---

**Créé avec ❤️ pour Coach José**
