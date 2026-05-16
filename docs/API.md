# 📖 Documentation API - Coach José

Documentation complète de tous les endpoints API.

---

## 🔗 Base URL

```
Local:      http://localhost:8000
Production: https://coach-jose-api.railway.app
```

---

## ✅ Health Check

### Vérifier statut API

```http
GET /api/health
```

**Response (200)**:
```json
{
  "status": "healthy",
  "service": "Coach José API",
  "version": "1.0.0"
}
```

---

## 💬 Chat Endpoints

### 1. Démarrer Conversation

```http
POST /api/chat/start
Content-Type: application/json

{
  "user_id": "user-123",
  "user_email": "prospect@example.com",
  "source": "website"
}
```

**Response (200)**:
```json
{
  "conversation_id": "conv-abc123",
  "message": "Bonjour! Je suis Coach José. Comment puis-je vous aider avec nos produits Neolife?",
  "session_token": "token-xyz"
}
```

### 2. Envoyer Message

```http
POST /api/chat/message
Content-Type: application/json

{
  "conversation_id": "conv-abc123",
  "message": "Quels sont vos produits?",
  "session_token": "token-xyz"
}
```

**Response (200)**:
```json
{
  "conversation_id": "conv-abc123",
  "response": "Neolife propose une gamme complète de produits de santé et bien-être...",
  "next_action": "ask_for_contact",
  "confidence": 0.95
}
```

### 3. Qualifier le Lead

```http
POST /api/chat/qualify
Content-Type: application/json

{
  "conversation_id": "conv-abc123",
  "qualification": {
    "interest_level": "high",
    "budget": "1000+",
    "timeline": "immediate"
  }
}
```

**Response (200)**:
```json
{
  "lead_score": 85,
  "recommendation": "immediate_contact",
  "next_step": "collect_contact_info"
}
```

---

## 👥 Lead Management

### 1. Créer Lead

```http
POST /api/leads
Content-Type: application/json

{
  "email": "prospect@example.com",
  "phone": "+33612345678",
  "name": "Jean Dupont",
  "conversation_id": "conv-abc123",
  "qualification": "high",
  "source": "website_chat"
}
```

**Response (201)**:
```json
{
  "id": "lead-123",
  "email": "prospect@example.com",
  "status": "new",
  "created_at": "2026-05-16T10:30:00Z",
  "next_action": "send_welcome_email"
}
```

### 2. Récupérer Leads

```http
GET /api/leads?limit=50&offset=0&status=new
```

**Response (200)**:
```json
{
  "total": 250,
  "leads": [
    {
      "id": "lead-123",
      "email": "prospect@example.com",
      "name": "Jean Dupont",
      "status": "new",
      "score": 85,
      "created_at": "2026-05-16T10:30:00Z"
    }
  ]
}
```

### 3. Mettre à jour Lead

```http
PUT /api/leads/lead-123
Content-Type: application/json

{
  "status": "contacted",
  "notes": "Intéressé par le pack starter"
}
```

**Response (200)**:
```json
{
  "id": "lead-123",
  "status": "contacted",
  "updated_at": "2026-05-16T11:00:00Z"
}
```

### 4. Supprimer Lead

```http
DELETE /api/leads/lead-123
```

**Response (204)**: No content

---

## 📊 Analytics

### 1. Statistiques Conversations

```http
GET /api/analytics/conversations?start_date=2026-05-01&end_date=2026-05-31
```

**Response (200)**:
```json
{
  "total_conversations": 1250,
  "total_leads_generated": 340,
  "conversion_rate": 0.272,
  "average_conversation_length": 4.2,
  "peak_hour": 14
}
```

### 2. Performance Chatbot

```http
GET /api/analytics/performance
```

**Response (200)**:
```json
{
  "satisfaction_score": 4.5,
  "response_time_ms": 1200,
  "message_count": 5432,
  "error_rate": 0.02,
  "top_questions": [
    "Quels sont les produits?",
    "Quel est le prix?"
  ]
}
```

---

## 🔐 Authentication (Futur)

```http
POST /api/auth/login
Content-Type: application/json

{
  "email": "admin@coach-jose.app",
  "password": "secure-password"
}
```

**Response (200)**:
```json
{
  "token": "eyJhbGciOiJIUzI1NiIs...",
  "expires_in": 86400
}
```

Utiliser le token dans les requêtes:
```http
Authorization: Bearer eyJhbGciOiJIUzI1NiIs...
```

---

## ❌ Codes Erreur

| Code | Message | Solution |
|------|---------|----------|
| 400 | Bad Request | Vérifier paramètres JSON |
| 401 | Unauthorized | Ajouter token Authorization |
| 404 | Not Found | Vérifier URL et paramètres |
| 429 | Too Many Requests | Attendre / upgrade plan |
| 500 | Server Error | Contacter support |

**Format erreur**:
```json
{
  "error": "invalid_request",
  "message": "Missing required field: email",
  "details": {}
}
```

---

## 🧪 Tests avec cURL

### Health check
```bash
curl http://localhost:8000/api/health
```

### Créer conversation
```bash
curl -X POST http://localhost:8000/api/chat/start \
  -H "Content-Type: application/json" \
  -d '{"user_id":"user-123","user_email":"test@example.com"}'
```

### Envoyer message
```bash
curl -X POST http://localhost:8000/api/chat/message \
  -H "Content-Type: application/json" \
  -d '{
    "conversation_id":"conv-123",
    "message":"Bonjour!"
  }'
```

### Récupérer leads
```bash
curl "http://localhost:8000/api/leads?limit=10"
```

---

## 📚 OpenAPI Documentation

Documentation interactive disponible à:

```
http://localhost:8000/docs
```

Tester les endpoints directement dans le browser ! 🎉

---

## 🔄 Webhooks (Futur)

Recevoir notifications d'événements:

```json
{
  "event": "new_lead",
  "lead_id": "lead-123",
  "timestamp": "2026-05-16T10:30:00Z"
}
```

Configurer webhook URL dans settings.

---

## 💡 Examples Complets

### Workflow complet: Chat → Lead

```bash
# 1. Démarrer conversation
CONV_ID=$(curl -s -X POST http://localhost:8000/api/chat/start \
  -H "Content-Type: application/json" \
  -d '{
    "user_id":"user-123",
    "user_email":"prospect@example.com"
  }' | jq -r '.conversation_id')

# 2. Envoyer plusieurs messages
curl -X POST http://localhost:8000/api/chat/message \
  -H "Content-Type: application/json" \
  -d "{
    \"conversation_id\":\"$CONV_ID\",
    \"message\":\"Quels produits recommandez-vous?\"
  }"

# 3. Créer lead
curl -X POST http://localhost:8000/api/leads \
  -H "Content-Type: application/json" \
  -d "{
    \"email\":\"prospect@example.com\",
    \"phone\":\"+33612345678\",
    \"name\":\"Jean Dupont\",
    \"conversation_id\":\"$CONV_ID\",
    \"qualification\":\"high\"
  }"
```

---

## 🚀 Rate Limiting

Limites par heure:
- Chat: 1000 requêtes
- Leads: 500 requêtes
- Analytics: 100 requêtes

Headers de réponse:
```
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 999
X-RateLimit-Reset: 1632427200
```

---

## 📞 Support API

- 📖 Documentation: https://coach-jose.app/docs
- 🐛 Issues: https://github.com/NeoLife2014/coach-jose-/issues
- 💬 Discussions: https://github.com/NeoLife2014/coach-jose-/discussions
