# Terra Viva

![Status](https://img.shields.io/badge/Status-Em%20Produ%C3%A7%C3%A3o-brightgreen)
![Python](https://img.shields.io/badge/Python-3.14-blue)
![Django](https://img.shields.io/badge/Django-5.2.10-green)
![Vue.js](https://img.shields.io/badge/Vue.js-3.2.13-brightgreen)
![License](https://img.shields.io/badge/License-MIT-blue)

Plataforma de e-commerce full-stack desenvolvida para automatizar vendas de uma ONG, substituindo processos manuais por um sistema online completo. O sistema integra catálogo de produtos, carrinho de compras, checkout com Stripe e gestão de pedidos.

> Projeto acadêmico de 2021 revitalizado em 2026 como case para portfólio profissional.

**Links de Produção:**

- **Frontend:** <https://terraviva.vercel.app>
- **Backend API:** <https://terraviva-api-bg8s.onrender.com>

---

## Índice

- [Sobre o Projeto](#sobre-o-projeto)
- [Arquitetura](#arquitetura)
- [Stack Tecnológico](#stack-tecnológico)
- [Funcionalidades](#funcionalidades)
- [Instalação Local](#instalação-local)
- [Endpoints API](#endpoints-api)
- [Roadmap](#roadmap)
- [Documentação](#documentação)

---

## Sobre o Projeto

**Terra Viva** foi desenvolvido como projeto do programa **Coding4Hope** (2021), uma iniciativa acadêmica para promover transformação digital no terceiro setor.

**Desafio:** Uma ONG realizava gestão de vendas através de processos analógicos (planilhas, anotações), resultando em perda de eficiência e limitação no alcance de vendas.

**Solução:** Plataforma e-commerce full-stack com catálogo de produtos, carrinho, checkout integrado com Stripe e gestão de pedidos via admin panel.

### Revitalização em 2026

Após 4 anos sem manutenção (2022-2025), o projeto foi revitalizado em janeiro de 2026:

| Aspecto  | 2021 (Original) | 2026 (Atual)           |
| -------- | --------------- | ---------------------- |
| Status   | Funcional       | Em Produção            |
| Backend  | Heroku          | Render.com             |
| Frontend | Heroku          | Vercel                 |
| Database | SQLite          | Supabase PostgreSQL    |
| Storage  | Local           | Supabase Storage (CDN) |
| Django   | 4.1.2           | 5.2.10                 |
| Python   | 3.9             | 3.14                   |

---

## Arquitetura

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        TERRA VIVA INFRASTRUCTURE                        │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│                           ┌─────────────┐                               │
│                           │   CLIENT    │                               │
│                           │   Browser   │                               │
│                           └──────┬──────┘                               │
│                                  │                                      │
│                    ┌─────────────┴─────────────┐                        │
│                    │                           │                        │
│                    ▼                           ▼                        │
│         ┌──────────────────┐       ┌──────────────────┐                 │
│         │     VERCEL       │       │    RENDER.COM    │                 │
│         │   ────────────   │       │   ────────────   │                 │
│         │   Vue.js SPA     │       │   Django API     │                 │
│         │   ────────────   │       │   ────────────   │                 │
│         │   CDN: Global    │       │   gunicorn       │                 │
│         │   SSL: Auto      │       │   WhiteNoise     │                 │
│         └──────────────────┘       └────────┬─────────┘                 │
│                                             │                           │
│                              ┌──────────────┴──────────────┐            │
│                              │                             │            │
│                              ▼                             ▼            │
│                   ┌──────────────────┐         ┌──────────────────┐     │
│                   │    SUPABASE      │         │    SUPABASE      │     │
│                   │    PostgreSQL    │         │    Storage       │     │
│                   │   ────────────   │         │   ────────────   │     │
│                   │   500MB free     │         │   1GB free       │     │
│                   │   Persistent     │         │   CDN (285 POPs) │     │
│                   └──────────────────┘         └──────────────────┘     │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Stack Tecnológico

```
╔═══════════════════════════════════════════════════════════╗
║                    STACK v2.1.0                           ║
╠═══════════════════════════════════════════════════════════╣
║                                                           ║
║  Backend                                                  ║
║  ├── Python 3.14                                          ║
║  ├── Django 5.2.10                                        ║
║  ├── Django REST Framework 3.15.2                         ║
║  ├── djoser 2.2.3 (autenticação)                          ║
║  ├── Pillow 12.1.0 (imagens)                              ║
║  ├── supabase 2.27.1 (storage)                            ║
║  ├── Stripe 11.3.0 (pagamentos)                           ║
║  └── gunicorn + WhiteNoise                                ║
║                                                           ║
║  Frontend                                                 ║
║  ├── Vue.js 3.2.13                                        ║
║  ├── Vue Router 4.0.3                                     ║
║  ├── Vuex 4.0.0                                           ║
║  ├── Axios 1.1.3                                          ║
║  └── Bulma 0.9.4                                          ║
║                                                           ║
║  Infraestrutura                                           ║
║  ├── Backend: Render.com                                  ║
║  ├── Frontend: Vercel                                     ║
║  ├── Database: Supabase PostgreSQL                        ║
║  └── Storage: Supabase Storage (CDN)                      ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
```

---

## Funcionalidades

**Catálogo e Navegação:**

- Página inicial com produtos recentes
- Listagem por categoria
- Busca por nome/descrição
- Thumbnails automáticos (300x200px)

**Carrinho e Checkout:**

- Carrinho persistente (Vuex + localStorage)
- Checkout com Stripe Elements
- Validação client + server

**Autenticação:**

- Registro/Login via djoser
- Token Authentication
- Histórico de pedidos

**Administração:**

- Django Admin Panel
- CRUD de produtos e categorias
- Upload de imagens para CDN

---

## Instalação Local

### Requisitos

- Python 3.14+
- Node.js 16+
- Git

### Backend

```bash
git clone https://github.com/fabiodelllima/projeto-terraviva.git
cd projeto-terraviva

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt

cp .env.example .env
# Editar .env com suas credenciais

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### Frontend

```bash
cd terraviva_v
npm install
npm run serve
```

**Stripe Test Mode:** Use cartão `4242 4242 4242 4242`, qualquer CVC e data futura.

---

## Endpoints API

```
AUTENTICAÇÃO
POST   /api/v1/auth/users/           Registro
POST   /api/v1/auth/token/login/     Login
POST   /api/v1/auth/token/logout/    Logout [AUTH]

PRODUTOS
GET    /api/v1/latest-products/      8 mais recentes
POST   /api/v1/products/search/      Busca
GET    /api/v1/products/<cat>/<id>/  Detalhes
GET    /api/v1/products/<category>/  Por categoria

PEDIDOS [AUTH]
POST   /api/v1/checkout/             Finalizar compra
GET    /api/v1/orders/               Histórico
```

---

## Roadmap

### Fase 1: Restauração (Jan 2026) - CONCLUÍDA

- [x] Deploy backend (Render.com)
- [x] Deploy frontend (Vercel)
- [x] Database PostgreSQL (Supabase)
- [x] Storage persistente (Supabase Storage)
- [x] Django 5.2.10 (compatibilidade Python 3.14)
- [ ] Validação end-to-end frontend

### Fase 2: Modernização (Fev-Mar 2026)

- [ ] Migração Vue CLI para Vite
- [ ] Vue.js 3.2 para 3.5+
- [ ] Testes >90% coverage
- [ ] CI/CD GitHub Actions

### Fase 3: Produção (Abr+ 2026)

- [ ] Observabilidade (Sentry)
- [ ] Performance optimization
- [ ] Features novas

Ver [docs/ROADMAP.md](docs/ROADMAP.md) para detalhes.

---

## Documentação

| Documento                               | Descrição                 |
| --------------------------------------- | ------------------------- |
| [ROADMAP.md](docs/ROADMAP.md)           | Planejamento das fases    |
| [ARCHITECTURE.md](docs/ARCHITECTURE.md) | Stack e decisões técnicas |
| [ENVIRONMENT.md](docs/ENVIRONMENT.md)   | Variáveis de ambiente     |
| [CHANGELOG.md](CHANGELOG.md)            | Histórico de versões      |

---

## Licença

[MIT License](LICENSE)

---

**Versão:** 2.1.0  
**Última atualização:** 11/01/2026
