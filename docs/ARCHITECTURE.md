# ARCHITECTURE

**Versão:** 2.1.0

---

## Visão Geral

Arquitetura Full-Stack Separada:

- Backend: Django REST API
- Frontend: Vue.js SPA
- Database: Supabase PostgreSQL
- Storage: Supabase Storage (CDN)

---

## Estrutura de Diretórios

```
projeto-terraviva/
├── order/                      # App Django: Pedidos
│   ├── models.py               # Order, OrderItem
│   ├── views.py                # checkout(), OrdersList
│   ├── serializers.py
│   └── urls.py
│
├── product/                    # App Django: Produtos
│   ├── models.py               # Product, Category
│   ├── views.py                # LatestProductsList, ProductDetail
│   ├── serializers.py
│   └── urls.py
│
├── terraviva/                  # Configuração Django
│   ├── settings.py
│   ├── storage.py              # Custom Supabase Storage backend
│   ├── urls.py
│   └── wsgi.py
│
├── terraviva_v/                # Frontend Vue.js
│   ├── src/
│   │   ├── components/
│   │   ├── views/
│   │   ├── router/
│   │   ├── store/
│   │   └── main.js
│   ├── vercel.json             # SPA routing config
│   └── package.json
│
├── docs/                       # Documentação
│   ├── ROADMAP.md
│   ├── ARCHITECTURE.md
│   └── ENVIRONMENT.md
│
├── requirements.txt
├── CHANGELOG.md
└── README.md
```

---

## Infraestrutura de Produção

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        TERRA VIVA INFRASTRUCTURE                        │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│         ┌──────────────────┐       ┌──────────────────┐                 │
│         │     VERCEL       │       │    RENDER.COM    │                 │
│         │   ────────────   │       │   ────────────   │                 │
│         │   Vue.js SPA     │◄─────►│   Django API     │                 │
│         │   CDN Global     │       │   gunicorn       │                 │
│         └──────────────────┘       └────────┬─────────┘                 │
│                                             │                           │
│                              ┌──────────────┴──────────────┐            │
│                              ▼                             ▼            │
│                   ┌──────────────────┐         ┌──────────────────┐     │
│                   │    SUPABASE      │         │    SUPABASE      │     │
│                   │    PostgreSQL    │         │    Storage       │     │
│                   │   500MB free     │         │   1GB free       │     │
│                   └──────────────────┘         │   CDN (285 POPs) │     │
│                                                └──────────────────┘     │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### URLs de Produção

| Serviço     | URL                                        |
| ----------- | ------------------------------------------ |
| Frontend    | <https://terraviva.vercel.app\>            |
| Backend API | <https://terraviva-api-bg8s.onrender.com\> |

---

## Storage Architecture

### Custom Storage Backend

```python
# terraviva/storage.py
class SupabaseStorage(Storage):
    """
    Custom Django storage backend for Supabase Storage.
    - Upload direto para bucket Supabase
    - URLs públicas via CDN
    - Fallback para imagens legadas
    """
```

### Configuração Django 5.2+

```python
STORAGES = {
    "default": {
        "BACKEND": "terraviva.storage.SupabaseStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}
```

### Estrutura do Bucket

```
media/                          # Bucket Supabase
└── uploads/
    ├── produto1.jpg
    ├── produto1_thumb.jpg
    └── ...
```

### Limitações do Supabase Storage

**Nomes de arquivo:** O Supabase Storage não aceita caracteres especiais (acentos, cedilha, etc.) em nomes de arquivo. Utilize apenas caracteres ASCII:

- Correto: `maca.jpg`, `limao.jpg`, `acai.jpg`
- Incorreto: `maçã.jpg`, `limão.jpg`, `açaí.jpg`

O upload de arquivos com caracteres especiais resultará em erro `400 Bad Request: Invalid key`.

---

## Stack Tecnológico

| Camada            | Tecnologia            | Versão |
| ----------------- | --------------------- | ------ |
| Backend Runtime   | Python                | 3.14   |
| Backend Framework | Django                | 5.2.10 |
| API               | Django REST Framework | 3.15.2 |
| Auth              | djoser                | 2.2.3  |
| Storage           | supabase-py           | 2.27.1 |
| Payments          | Stripe                | 11.3.0 |
| Frontend          | Vue.js                | 3.2.13 |
| State             | Vuex                  | 4.0.0  |
| CSS               | Bulma                 | 0.9.4  |

---

## Estrutura Proposta (Fase 2)

```
projeto-terraviva/
├── backend/
│   ├── apps/
│   │   ├── order/
│   │   └── product/
│   ├── config/
│   │   └── settings/
│   │       ├── base.py
│   │       ├── development.py
│   │       └── production.py
│   └── requirements/
│       ├── base.txt
│       └── production.txt
│
├── frontend/
│   ├── src/
│   ├── tests/
│   └── vite.config.js
│
└── .github/
    └── workflows/
```

---

**Última revisão:** 11/01/2026
