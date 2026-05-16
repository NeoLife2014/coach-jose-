# 🚀 Guide de Déploiement - Coach José

Déployer votre chatbot IA en production (gratuitement ou à bas coût).

---

## Option 1: Vercel (Frontend) + Railway (Backend) ⭐ RECOMMANDÉ

### Avantages
- ✅ Gratuit pour démarrer
- ✅ Scaling automatique
- ✅ CDN mondial
- ✅ Déploiement via GitHub

### Étapes

#### A. Déployer le Frontend (Vercel)

1. **Créer compte**: https://vercel.com (connectez-vous avec GitHub)

2. **Importer le projet**:
   - Cliquer "New Project"
   - Sélectionner votre repo `coach-jose-`
   - Configurer:
     - Framework: Next.js
     - Root Directory: `./frontend`

3. **Variables d'environnement**:
   ```
   NEXT_PUBLIC_API_URL=https://coach-jose-api.railway.app
   ```

4. **Déployer**: Cliquer "Deploy"

**Résultat**: Votre site à `coach-jose.vercel.app`

#### B. Déployer le Backend (Railway)

1. **Créer compte**: https://railway.app

2. **Créer nouveau projet**: Dashboard → "New Project" → "GitHub Repo"

3. **Connecter repo**: Sélectionner `NeoLife2014/coach-jose-`

4. **Configurer service**:
   - Root directory: `/backend`
   - Dockerfile: `backend/Dockerfile`

5. **Ajouter variables d'environnement** dans Railway:
   ```
   OPENAI_API_KEY=sk-your-key
   SUPABASE_URL=https://...
   SUPABASE_KEY=your-key
   NEOLIFE_SHOP_URL=https://shopneolife.com/startupforworld
   DEBUG=false
   ```

6. **Déployer**: Railway déploiera automatiquement

7. **Récupérer URL**: Voir dans Railway Dashboard, ex: `coach-jose-api.railway.app`

8. **Mettre à jour Vercel**: 
   - Aller dans Vercel Settings
   - Ajouter `NEXT_PUBLIC_API_URL=https://coach-jose-api.railway.app`
   - Redéployer

**Résultat**: Backend à `coach-jose-api.railway.app`

---

## Option 2: Heroku (Backend) + Netlify (Frontend)

### Heroku Backend

```bash
# Installer Heroku CLI
# https://devcenter.heroku.com/articles/heroku-cli

# Login
heroku login

# Créer app
heroku create coach-jose-api

# Ajouter variables
heroku config:set OPENAI_API_KEY=sk-your-key
heroku config:set SUPABASE_URL=...
heroku config:set SUPABASE_KEY=...

# Déployer
git push heroku main

# Logs
heroku logs --tail
```

### Netlify Frontend

1. Créer compte: https://netlify.com
2. "New site from Git"
3. Configurer:
   - Build command: `cd frontend && npm run build`
   - Publish directory: `frontend/.next`
4. Variables d'environnement:
   ```
   NEXT_PUBLIC_API_URL=https://coach-jose-api.herokuapp.com
   ```

---

## Option 3: Docker + Serveur VPS

### Déployer avec Docker

```bash
# Build images
docker-compose build

# Démarrer services
docker-compose up -d

# Logs
docker-compose logs -f backend
docker-compose logs -f frontend

# Arrêter
docker-compose down
```

### VPS Providers (DigitalOcean, Linode, etc.)

```bash
# Sur votre serveur VPS
git clone https://github.com/NeoLife2014/coach-jose-.git
cd coach-jose-

# Configurer .env
nano .env

# Lancer Docker
docker-compose up -d

# Vérifier
curl http://localhost:8000/api/health
```

---

## Configuration DNS & SSL

### Point de domaine personnalisé

1. **Chez votre registrar** (GoDaddy, OVH, etc.):
   - Ajouter record CNAME vers Vercel/Railway
   - Exemple: `coach-jose.votredomaine.com` → `cname.vercel-dns.com`

2. **Vercel/Railway**: Ajouter domaine personnalisé

3. **SSL**: Automatique (Let's Encrypt)

---

## Monitoring & Logs

### Vercel
- Dashboard → Deployments → Logs

### Railway
- Dashboard → Services → Logs

### Backend Healthcheck
```bash
curl https://coach-jose-api.railway.app/api/health
```

---

## Coûts Estimés (Gratuit/Mois)

| Service | Gratuit | Payant |
|---------|---------|--------|
| Vercel | ✅ Oui | $20+/mois |
| Railway | ✅ Oui | $7/mois |
| Supabase | ✅ Oui | $25+/mois |
| OpenAI | ❌ Payant | $0.01-0.03/requête |

**Total**: Quasi gratuit sauf OpenAI (environ $5-20/mois avec usage modéré)

---

## CI/CD Automatique

Railway et Vercel déploient **automatiquement** à chaque push sur `main`:

```bash
git add .
git commit -m "Fix chatbot response"
git push origin main
# → Déploiement auto en 2-3 min
```

---

## Troubleshooting Déploiement

### "API connection refused"
- Vérifier que backend est déployé
- Vérifier URL dans variables d'env frontend
- Vérifier CORS configuré

### "OPENAI_API_KEY not found"
- Ajouter la variable dans Railway/Heroku settings
- Vérifier qu'elle est correcte

### "Supabase connection timeout"
- Vérifier URL et clé Supabase
- Vérifier que projet Supabase est actif

---

## Prochaines Étapes

1. ✅ Déployer Backend
2. ✅ Déployer Frontend
3. 🔄 Configurer Supabase CRM
4. 📊 Ajouter monitoring
5. 🔐 Configurer authentification admin

---

## Support Déploiement

- Railway docs: https://docs.railway.app
- Vercel docs: https://vercel.com/docs
- Heroku docs: https://devcenter.heroku.com
