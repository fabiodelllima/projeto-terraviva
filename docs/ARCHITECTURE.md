# ARCHITECTURE

**Projeto:** Terra Viva  
**Versão:** 2.0.0

---

## Índice

- [Visão Geral](#visão-geral)
- [Estrutura Atual](#estrutura-atual)
- [Estrutura Proposta (Fase 2)](#estrutura-proposta-fase-2)
- [Justificativas Técnicas](#justificativas-técnicas)
- [Plano de Migração](#plano-de-migração)
- [Padrões Arquiteturais](#padrões-arquiteturais)

---

## Visão Geral

Terra Viva segue arquitetura **Full-Stack Separada** com:

- Backend Django (API REST)
- Frontend Vue.js (SPA)
- Database PostgreSQL (produção)

**Estilo Arquitetural:** Modular / Domain-Driven Structure

---

## Estrutura Atual

### Árvore de Diretórios

```
projeto-terraviva/
├── order/                      # Django App: Pedidos
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── models.py               # Order, OrderItem
│   ├── serializers.py          # OrderSerializer, MyOrderSerializer
│   ├── urls.py                 # /api/v1/checkout/, /orders/
│   └── views.py                # checkout(), OrdersList
│
├── product/                    # Django App: Produtos
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── models.py               # Product, Category
│   ├── serializers.py          # ProductSerializer, CategorySerializer
│   ├── urls.py                 # /api/v1/products/*
│   └── views.py                # LatestProductsList, ProductDetail, search()
│
├── terraviva/                  # Configuração Django
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py             # Configurações principais
│   ├── urls.py                 # URLs raiz
│   └── wsgi.py
│
├── terraviva_v/                # Frontend Vue.js
│   ├── public/
│   ├── src/
│   │   ├── components/         # ProductBox, CartItem, OrderSummary
│   │   ├── views/              # 10 páginas (Home, Cart, etc)
│   │   ├── router/             # Vue Router
│   │   ├── store/              # Vuex store
│   │   ├── App.vue
│   │   └── main.js
│   ├── package.json
│   └── vue.config.js
│
├── media/                      # Uploads Django (imagens de produtos)
├── staticfiles/                # Static files coletados (collectstatic)
├── db.sqlite3                  # Database de desenvolvimento
├── manage.py
├── requirements.txt
├── netlify.toml
└── .gitignore
```

**Nota Importante:** O projeto atual NÃO segue Domain-Driven Design completo:

```
APPS FALTANTES:
├── user/     => Autenticação usa django.contrib.auth (builtin)
│                djoser gerencia registro/login, mas SEM app dedicado
└── payment/  => Stripe integrado DENTRO de order/views.py
                 NÃO TEM app isolado para pagamentos
```

**Justificativa:** Projeto acadêmico de 2021 (MVP rápido).
**Proposta para Fase 2:** Criar `user/` e `payment/` para isolamento adequado.

**Padrão Django Oficial:** Apps ficam no mesmo nível que `manage.py`

```python
INSTALLED_APPS = [
    'order',
    'product',
    ...
]
```

---

## Estrutura Proposta (Fase 2)

### Modular Architecture - Two Scoops Layout

```
projeto-terraviva/
│
├── backend/                    # Backend Django
│   ├── apps/                   # Apps Django organizadas por domínio
│   │   ├── __init__.py
│   │   ├── order/              # Domínio: Pedidos
│   │   │   ├── migrations/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── models.py
│   │   │   ├── serializers.py
│   │   │   ├── tests/          # Testes isolados por app
│   │   │   │   ├── test_models.py
│   │   │   │   ├── test_views.py
│   │   │   │   └── test_serializers.py
│   │   │   ├── urls.py
│   │   │   └── views.py
│   │   │
│   │   └── product/            # Domínio: Produtos
│   │       ├── migrations/
│   │       ├── __init__.py
│   │       ├── admin.py
│   │       ├── models.py
│   │       ├── serializers.py
│   │       ├── tests/
│   │       ├── urls.py
│   │       └── views.py
│   │
│   ├── config/                 # Configuração Django
│   │   ├── settings/
│   │   │   ├── __init__.py
│   │   │   ├── base.py         # Configurações comuns
│   │   │   ├── development.py  # Dev: DEBUG=True, SQLite
│   │   │   ├── production.py   # Prod: DEBUG=False, PostgreSQL
│   │   │   └── test.py         # Tests: in-memory DB
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   │
│   ├── media/                  # Uploads (imagens de produtos)
│   ├── static/                 # Static files backend
│   ├── staticfiles/            # Coletados
│   ├── manage.py
│   ├── requirements/           # Dependencies por ambiente
│   │   ├── base.txt
│   │   ├── development.txt
│   │   ├── production.txt
│   │   └── test.txt
│   └── pytest.ini              # Configuração de testes
│
├── frontend/                   # Frontend Vue.js
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── views/
│   │   ├── router/
│   │   ├── store/
│   │   ├── App.vue
│   │   └── main.js
│   ├── tests/                  # Testes de frontend
│   │   ├── unit/
│   │   └── e2e/
│   ├── .env.local
│   ├── .env.production
│   ├── package.json
│   └── vite.config.js
│
├── docs/                       # Documentação técnica
│   ├── ROADMAP.md
│   ├── ARCHITECTURE.md
│   ├── BUSINESS_RULES.md
│   ├── DEPLOYMENT.md
│   ├── ENVIRONMENT.md
│   └── decisions/              # ADRs
│       ├── ADR-001-backend-frontend-separation.md
│       ├── ADR-002-render-netlify.md
│       ├── ADR-003-supabase-postgresql.md
│       └── ADR-006-modular-architecture.md
│
├── .github/                    # CI/CD
│   └── workflows/
│       ├── backend-ci.yml
│       ├── frontend-ci.yml
│       └── keep-supabase-alive.yml
│
├── README.md
├── CHANGELOG.md
├── LICENSE
└── .gitignore
```

### Diferenças Principais

```
╔═══════════════════════════════════════════════════════════╗
║  ASPECTO          │ ATUAL (Fase 1)   │ PROPOSTO (Fase 2)  ║
╠═══════════════════════════════════════════════════════════╣
║  Apps Django      │ Raiz             │ backend/apps/      ║
║  Config Django    │ terraviva/       │ backend/config/    ║
║  Settings         │ Único arquivo    │ Por ambiente       ║
║  Frontend         │ terraviva_v/     │ frontend/          ║
║  Requirements     │ Único arquivo    │ Por ambiente       ║
║  Testes           │ Não existem      │ Isolados por app   ║
║  Docs             │ Raiz             │ docs/              ║
║  CI/CD            │ Não existe       │ .github/           ║
╚═══════════════════════════════════════════════════════════╝
```

---

## Justificativas Técnicas

### 1. Apps em `backend/apps/`

**Problema Atual:**

```
projeto-terraviva/
├── order/          # App misturado com configs
├── product/        # App misturado com configs
├── terraviva/      # Config misturada com apps
└── terraviva_v/    # Frontend misturado
```

**Solução Proposta:**

```
projeto-terraviva/
├── backend/
│   └── apps/
│       ├── order/      # Apps isoladas
│       └── product/
└── frontend/           # Frontend isolado
```

---

### 2. Settings por Ambiente

**Problema Atual:**

```python
# terraviva/settings.py (ÚNICO ARQUIVO)

DEBUG = True  # Inseguro em produção
ALLOWED_HOSTS = []  # Quebra deploy

if os.environ.get('PRODUCTION'):  # Lógica condicional problemática
    DEBUG = False
    # mais configs...
```

**Solução Proposta:**

```python
# backend/config/settings/base.py (COMUM)
INSTALLED_APPS = [...]
MIDDLEWARE = [...]

# backend/config/settings/development.py
from .base import *
DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3'}}

# backend/config/settings/production.py
from .base import *
DEBUG = False
ALLOWED_HOSTS = [os.environ['ALLOWED_HOSTS']]
DATABASES = {'default': dj_database_url.config()}
```

**Benefícios:**

- Código mais limpo (sem condicionais)
- Seguro (impossível DEBUG=True em prod)
- Fácil adicionar ambientes (staging, test)
- Padrão "Two Scoops of Django"

---

### 3. Requirements por Ambiente

**Problema Atual:**

```
requirements.txt (ÚNICO ARQUIVO)
├── Django==4.2.17
├── pytest==7.4.0        # Dev-only
├── pytest-django==4.5.0 # Dev-only
├── gunicorn==20.1.0     # Prod-only
└── ...
```

**Solução Proposta:**

```
requirements/
├── base.txt          # Comum (Django, DRF, etc)
├── development.txt   # Dev (pytest, ipython, etc)
├── production.txt    # Prod (gunicorn, sentry, etc)
└── test.txt          # Tests (factory-boy, faker, etc)
```

**Benefícios:**

- Builds produção mais leves
- Claras dependências de cada ambiente
- Facilita troubleshooting

---

### 4. Testes Isolados por App

**Problema Atual:**

```
Sem testes :(
```

**Solução Proposta:**

```
backend/apps/order/tests/
├── test_models.py       # Testes Order, OrderItem
├── test_views.py        # Testes checkout(), OrdersList
└── test_serializers.py  # Testes OrderSerializer

backend/apps/product/tests/
├── test_models.py
├── test_views.py
└── test_serializers.py
```

**Benefícios:**

- Testes próximos do código testado
- Fácil rodar testes isolados: `pytest backend/apps/order/`
- Padrão pytest-django
- Facilita >90% coverage

---

## Plano de Migração

### Fase 2: Modernização (Fev-Mar 2026)

**Semana 1: Preparação**

```
[2.1] Criar nova estrutura de diretórios
├── [ ] backend/apps, backend/config/settings
├── [ ] frontend/
└── [ ] docs/.github/workflows
```

**Semana 2: Migração Backend**

```
[2.2] Migrar Apps Django
├── [ ] order/   => backend/apps/
├── [ ] product/ => backend/apps/
├── [ ] Atualizar imports (order.models => apps.order.models)
└── [ ] Atualizar INSTALLED_APPS

[2.3] Migrar Config Django
├── [ ] terraviva/ => backend/config/
├── [ ] Split settings.py => base/dev/prod/test
├── [ ] Criar requirements/ por ambiente
└── [ ] Atualizar manage.py (apontar para config)

[2.4] Testar Backend
├── [ ] python manage.py check
├── [ ] python manage.py migrate
├── [ ] python manage.py runserver
└── [ ] Validar admin panel
```

**Semana 3: Migração Frontend**

```
[2.5] Migrar Frontend
├── [ ] terraviva_v/ => frontend/
├── [ ] Atualizar axios baseURL (apontar para backend)
├── [ ] Atualizar scripts package.json
└── [ ] Testar npm run serve
```

**Semana 4: Validação**

```
[2.6] Testes End-to-End
├── [ ] Fluxo completo: Home => Checkout => Success
├── [ ] Admin panel funcional
├── [ ] API endpoints OK
└── [ ] Frontend + Backend integrados

[2.7] Deploy Teste
├── [ ] Deploy backend (Render)
├── [ ] Deploy frontend (Netlify)
└── [ ] Validação produção
```

### Riscos e Mitigações

```
╔════════════════════════════════════════════════════════════╗
║  RISCO                      │ PROB  │ IMPACTO │ MITIGAÇÃO  ║
╠════════════════════════════════════════════════════════════╣
║  Imports quebrados          │ ALTA  │ MÉDIO   │ Testes     ║
║  Settings errados           │ MÉDIA │ ALTO    │ Validação  ║
║  Deploy falha               │ MÉDIA │ ALTO    │ Staging    ║
║  Rollback necessário        │ BAIXA │ ALTO    │ Git branch ║
╚════════════════════════════════════════════════════════════╝
```

**Estratégia de Rollback:**

```bash
# Criar branch para migração
git checkout -b feat/modular-architecture

# Se falhar, rollback instantâneo:
git checkout main
```

---

## Padrões Arquiteturais

### Nome Técnico: Modular Architecture

**Também conhecida como:**

- Domain-Driven Structure (quando apps = domínios)
- Two Scoops Layout (referência ao livro "Two Scoops of Django")
- Layered Monolith (quando bem estruturado)

### Características

```
Modular Architecture:
├── Separação por domínio (apps/)
│   └── Cada app = bounded context isolado
├── Configurações isoladas (config/)
│   └── Base + overrides por ambiente
├── Ambientes claramente separados
│   └── dev, test, staging, production
├── Backend e Frontend separados
│   └── API REST como contrato
└── Documentação centralizada
    └── Single source of truth (docs/)
```

### MVC e MVP

```
MVC/MVP = Padrão de UI/Presentation Layer
Modular = Padrão de organização de código/projeto

Terra Viva usa AMBOS:
├── Django MVC (Model-View-Template internamente)
├── Vue.js MVVM (Model-View-ViewModel)
└── Modular Architecture (organização do projeto)
```

### Referências

- [Two Scoops of Django](https://www.feldroy.com/books/two-scoops-of-django-3-x)
- [Django Best Practices](https://django-best-practices.readthedocs.io/)
- [Cookiecutter Django](https://github.com/cookiecutter/cookiecutter-django)

---

## Decisões Arquiteturais

Ver [decisions/](decisions/) para ADRs completos:

- [ADR-001: Separação Backend/Frontend](decisions/ADR-001-backend-frontend-separation.md)
- [ADR-002: Render.com + Netlify](decisions/ADR-002-render-netlify.md)
- [ADR-003: Supabase PostgreSQL](decisions/ADR-003-supabase-postgresql.md)
- **[ADR-006: Modular Architecture (Fase 2)](decisions/ADR-006-modular-architecture.md)** (planejado)

---

**Última revisão:** 07/01/2026
**Próxima revisão:** Após migração Fase 2
