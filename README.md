# Terra Viva

![Status](https://img.shields.io/badge/Status-Em%20Revitaliza%C3%A7%C3%A3o-yellow)
![Python](https://img.shields.io/badge/Python-3.14.2-blue)
![Django](https://img.shields.io/badge/Django-4.2.17%20LTS-green)
![Vue.js](https://img.shields.io/badge/Vue.js-3.2.13-brightgreen)
![License](https://img.shields.io/badge/License-MIT-blue)

> **Plataforma de e-commerce full-stack** desenvolvida para automatizar vendas de uma ONG, substituindo processos manuais por sistema online completo. Sistema completo: catálogo de produtos, carrinho de compras, checkout com Stripe e gestão de pedidos.
>
> **Projeto acadêmico de 2021** revitalizado em **2026** como case para portfólio profissional.

**Revitalização 2026:**

| Aspecto              | 2021 (Original) | 2026 (Atual)        | 2026 (Meta)      |
| -------------------- | --------------- | ------------------- | ---------------- |
| **Status**           | ✓ Funcional     | ✗ Quebrado (4 anos) | ✓ Produção       |
| **Deploy**           | Heroku          | ✗ Não funciona      | Render + Netlify |
| **Vulnerabilidades** | Desconhecido    | 68 npm              | 0                |
| **Testes**           | 0%              | 0%                  | >90%             |
| **Documentação**     | README básico   | README básico       | Docs completa    |

---

## Índice

- [Sobre o Terra Viva](#sobre-o-terra-viva)
  - [Visão Geral](#visão-geral)
  - [Arquitetura](#arquitetura)
  - [Funcionalidades](#funcionalidades)
  - [Stack Tecnológico](#stack-tecnológico)
- [Contexto do Projeto](#contexto-do-projeto)
  - [Origem Acadêmica (2021)](#origem-acadêmica-2021)
  - [Hiato Técnico (2022-2025)](#hiato-técnico-2022-2025)
  - [Revitalização Profissional (2026)](#revitalização-profissional-2026)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Instalação e Configuração](#instalação-e-configuração)
  - [Requisitos](#requisitos)
  - [Backend (Django)](#backend-django)
  - [Frontend (Vue.js)](#frontend-vuejs)
- [Endpoints API](#endpoints-api)
- [Roadmap](#roadmap)
- [Documentação Técnica](#documentação-técnica)
- [Licença](#licença)

---

## Sobre o Terra Viva

### Visão Geral

**Terra Viva** é uma plataforma de e-commerce full-stack desenvolvida para automatizar vendas de uma ONG, substituindo processos manuais por sistema online completo. O sistema abrange o ciclo completo: catálogo de produtos, carrinho de compras, processamento de pagamentos via Stripe e gestão de pedidos.

**Domínio:** E-commerce para ONGs e organizações sem fins lucrativos

**Arquitetura:** API REST (Django) + SPA (Vue.js)

### Arquitetura

```
┌────────────────────────────────────────────────────────────────┐
│                      TERRA VIVA E-COMMERCE                     │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  ┌──────────────────┐          ┌──────────────────┐            │
│  │   VUE.JS SPA     │◄────────►│   DJANGO API     │            │
│  │   (Frontend)     │   REST   │   (Backend)      │            │
│  ├──────────────────┤          ├──────────────────┤            │
│  │ • Home           │          │ • Products       │            │
│  │ • Catálogo       │          │ • Categories     │            │
│  │ • Busca          │          │ • Orders         │            │
│  │ • Carrinho       │          │ • Auth (djoser)  │            │
│  │ • Checkout       │          │ • Admin Panel    │            │
│  │ • Perfil         │          │                  │            │
│  └──────────────────┘          └────────┬─────────┘            │
│                                         │                      │
│                                         ▼                      │
│                                ┌──────────────────┐            │
│                                │   SQLITE / PG    │            │
│                                │   (Database)     │            │
│                                └──────────────────┘            │
│                                         │                      │
│                                         ▼                      │
│                                ┌──────────────────┐            │
│                                │  STRIPE API      │            │
│                                │  (Pagamentos)    │            │
│                                └──────────────────┘            │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

### Funcionalidades

**Navegação e Catálogo:**

- Página inicial com 8 produtos mais recentes
- Listagem de produtos por categoria
- Detalhes de produto (imagem, descrição, preço)
- Busca por nome ou descrição (case-insensitive)
- Thumbnails gerados automaticamente (300x200px via Pillow)

**Carrinho e Checkout:**

- Carrinho de compras persistente (Vuex + localStorage)
- Adicionar/remover items
- Cálculo automático de totais
- Checkout com integração Stripe Elements
- Formulário de dados pessoais e endereço (validação client + server)

**Autenticação e Perfil:**

- Cadastro de usuário via djoser
- Login com Django Token Authentication
- Área "Minha Conta"
- Histórico de pedidos completo

**Administração:**

- Django Admin Panel integrado
- CRUD de produtos, categorias e pedidos
- Upload de imagens com preview
- Geração automática de thumbnails

### Stack Tecnológico

```
╔═══════════════════════════════════════════════════════════╗
║                    STACK ATUAL (2026)                     ║
╠═══════════════════════════════════════════════════════════╣
║                                                           ║
║  Backend (Python)                                         ║
║  ├── Python 3.14.2                                        ║
║  ├── Django 4.2.17 LTS (suporte até 04/2026)              ║
║  ├── Django REST Framework 3.15.2                         ║
║  ├── djoser 2.2.3 (autenticação + registro)               ║
║  ├── Pillow 10.4.0 (processamento imagens)                ║
║  ├── psycopg2-binary 2.9.10 (PostgreSQL driver)           ║
║  ├── Stripe 11.3.0 (pagamentos)                           ║
║  └── cryptography 43.0.3 (segurança)                      ║
║                                                           ║
║  Frontend (JavaScript)                                    ║
║  ├── Vue.js 3.2.13                                        ║
║  ├── Vue Router 4.0.3 (roteamento SPA)                    ║
║  ├── Vuex 4.0.0 (state management)                        ║
║  ├── Axios 1.1.3 (HTTP client)                            ║
║  ├── Bulma 0.9.4 (CSS framework)                          ║
║  ├── Bulma Toast 2.4.1 (notificações)                     ║
║  └── Vue CLI 5.0.0 (build tool)                           ║
║                                                           ║
║  Database                                                 ║
║  ├── SQLite (desenvolvimento)                             ║
║  └── PostgreSQL (produção - planejado)                    ║
║                                                           ║
║  Deploy (Planejado)                                       ║
║  ├── Backend: Render.com (free tier)                      ║
║  ├── Frontend: Netlify (free tier)                        ║
║  └── Database: Neon.tech ou Supabase                      ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
```

---

## Contexto do Projeto

### Origem Acadêmica (2021)

Terra Viva foi desenvolvido como projeto final do programa **Coding4Hope**, iniciativa acadêmica estruturada para promover transformação digital no terceiro setor. O programa focava em:

1. **Diagnóstico:** Identificar gargalos operacionais e processos não-automatizados em ONGs
2. **Análise de Requisitos:** Mapear necessidades reais e impacto potencial de soluções digitais
3. **Desenvolvimento:** Criar protótipos funcionais de sistemas que automatizassem workflows críticos
4. **Entrega:** Implementar soluções viáveis para organizações sem fins lucrativos

**Desafio Identificado:**

Uma ONG realizava gestão de vendas e inventário através de processos analógicos (planilhas Excel, anotações físicas), resultando em:

- Perda de eficiência operacional (~40% tempo gasto em tarefas repetitivas)
- Dificuldade no rastreamento de transações
- Impossibilidade de análise de dados históricos
- Limitação no alcance de vendas (apenas presencial)

**Solução Proposta:**

Plataforma e-commerce full-stack integrando:

- Backend Django (API REST + admin panel)
- Frontend Vue.js (SPA responsiva)
- Integração Stripe (pagamentos)
- Sistema de inventário automatizado
- Geração automática de thumbnails (otimização performance)

---

### Hiato Técnico (2022-2025)

Após conclusão acadêmica, o projeto entrou em estado de manutenção zero por **4 anos**:

**Débito Técnico Acumulado:**

| Categoria        | Problema                                      | Impacto              |
| ---------------- | --------------------------------------------- | -------------------- |
| **Dependencies** | Python 3.9 => 3.14 (breaking changes)         | Backend não inicia   |
| **Security**     | 68 CVEs em npm packages (6 critical, 19 high) | Build bloqueado      |
| **Framework**    | Django 4.1 => 4.2 (migrations incompatíveis)  | Database errors      |
| **Build Tool**   | Vue CLI deprecations                          | 8 vulnerabilidades   |
| **Deploy**       | Configuração Heroku + Netlify conflitante     | Ambos quebrados      |
| **Database**     | SQLite hardcoded                              | Não suporta produção |
| **Secrets**      | SECRET_KEY e STRIPE_KEY hardcoded             | Inseguro             |

**Status em janeiro/2026:**

- ✗ Backend Django: não inicia (incompatibilidade Python 3.14)
- ✗ Frontend Vue: falha no build (npm audit bloqueia CI/CD)
- ✗ Deploy Netlify: configuração espera Node.js, recebe Django
- ✗ Deploy Heroku: não funciona (Heroku eliminou free tier em 2022)

---

### Revitalização Profissional (2026)

Iniciativa de **janeiro/2026** para transformar projeto acadêmico em **case para portfólio profissional de produção**, com três objetivos primários:

**1. Restauração Operacional**

- Restabelecer funcionalidade completa de backend e frontend
- Resolver débito técnico acumulado (4 anos de breaking changes)
- Realizar primeiro deploy bem-sucedido desde 2021

**2. Modernização Tecnológica**

- Atualizar para stack atual (Python 3.14, Django 4.2 LTS, Vue 3.5)
- Migrar de Vue CLI para Vite (performance, DX, manutenibilidade)
- Eliminar vulnerabilidades de segurança (target: 0 CVEs)

**3. Profissionalização do Código**

- Implementar cobertura de testes >90% (backend + frontend)
- Documentar Business Rules e Architecture Decision Records
- Configurar CI/CD completo (GitHub Actions, testes automatizados)
- Adicionar observabilidade (logging estruturado, métricas)

**Cronograma:**

```
╔═══════════════════════════════════════════════════════════╗
║  FASE           │ DURAÇÃO    │ PERÍODO       │ STATUS     ║
╠═══════════════════════════════════════════════════════════╣
║  Fase 1         │ 2-3 sem    │ Jan 2026      │ ANDAMENTO  ║
║  Restauração    │            │               │            ║
║                 |            |               |            ║
║  Fase 2         │ 4-6 sem    │ Fev-Mar 2026  │ PLANEJADO  ║
║  Modernização   │            │               │            ║
║                 |            |               |            ║
║  Fase 3         │ Contínuo   │ Abr+ 2026     │ PLANEJADO  ║
║  Produção       │            │               │            ║
╚═══════════════════════════════════════════════════════════╝
```

**Detalhes:** Ver [docs/ROADMAP.md](docs/ROADMAP.md)

---

## Estrutura do Projeto

```
projeto-terraviva/
├── order/                      # App Django: Pedidos
│   ├── models.py               #   Order, OrderItem
│   ├── views.py                #   checkout(), OrdersList
│   ├── serializers.py          #   OrderSerializer
│   └── urls.py                 #   /api/v1/checkout/, /orders/
│
├── product/                    # App Django: Produtos
│   ├── models.py               #   Product, Category
│   ├── views.py                #   LatestProductsList, ProductDetail, search()
│   ├── serializers.py          #   ProductSerializer, CategorySerializer
│   └── urls.py                 #   /api/v1/products/*, /latest-products/
│
├── terraviva/                  # Configuração Django
│   ├── settings.py             #   Configurações principais
│   ├── urls.py                 #   URLs raiz
│   └── wsgi.py                 #   WSGI application
│
├── terraviva_v/                # Frontend Vue.js
│   ├── src/
│   │   ├── components/         #   ProductBox, CartItem, OrderSummary
│   │   ├── views/              #   10 páginas (Home, Cart, Checkout, etc)
│   │   ├── router/             #   Vue Router config
│   │   ├── store/              #   Vuex store (cart, auth)
│   │   ├── App.vue             #   Componente raiz
│   │   └── main.js             #   Entry point
│   ├── public/                 #   Static assets
│   └── package.json            #   Dependencies npm
│
├── media/                      # Uploads (imagens produtos)
├── db.sqlite3                  # Database desenvolvimento
├── requirements.txt            # Dependencies Python
├── netlify.toml                # Config deploy Netlify
└── manage.py                   # Django management
```

---

## Instalação e Configuração

### Requisitos

- Python 3.14+ (obrigatório)
- Node.js 16+ e npm
- Git

### Backend (Django)

```bash
# 1. Clone o repositório
git clone https://github.com/fabiodelllima/projeto-terraviva.git
cd projeto-terraviva

# 2. Crie ambiente virtual Python
python3.14 -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# 3. Instale dependências
pip install -r requirements.txt

# 4. Configure variáveis de ambiente (IMPORTANTE!)
# Crie arquivo .env na raiz do projeto:
cat > .env << 'EOF'
SECRET_KEY=your-secret-key-here
STRIPE_SECRET_KEY=sk_test_your_stripe_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
EOF

# 5. Execute migrations
python manage.py migrate

# 6. Crie superusuário (admin)
python manage.py createsuperuser

# 7. Execute servidor de desenvolvimento
python manage.py runserver

# Backend rodando em http://127.0.0.1:8000
# Admin panel: http://127.0.0.1:8000/admin
```

### Frontend (Vue.js)

```bash
# Em outro terminal:

# 1. Entre no diretório frontend
cd terraviva_v

# 2. Instale dependências
npm install

# 3. Execute servidor de desenvolvimento
npm run serve

# Frontend rodando em http://localhost:8080
```

**Fluxo Completo:**

1. Backend deve estar rodando em `http://127.0.0.1:8000`
2. Frontend acessa backend via axios (baseURL hardcoded)
3. Acesse `http://localhost:8080` no navegador

**Stripe Test Mode:**

- Use cartões de teste: `4242 4242 4242 4242`
- Qualquer CVC (ex: 123)
- Qualquer data futura (ex: 12/26)

---

## Endpoints API

```
╔═════════════════════════════════════════════════════════════════════════╗
║                          AUTENTICAÇÃO (djoser)                          ║
╠════════════╦═══════════════════════════════════╦════════════════════════╣
║  MÉTODO    ║  ENDPOINT                         ║  DESCRIÇÃO             ║
╠════════════╬═══════════════════════════════════╬════════════════════════╣
║  POST      ║  /api/v1/auth/users/              ║  Registro usuário      ║
║  POST      ║  /api/v1/auth/token/login/        ║  Login (retorna token) ║
║  POST      ║  /api/v1/auth/token/logout/       ║  Logout [AUTH]         ║
╚════════════╩═══════════════════════════════════╩════════════════════════╝
```

```
╔═══════════════════════════════════════════════════════════════════════╗
║                               PRODUTOS                                ║
╠════════════╦═══════════════════════════════════╦══════════════════════╣
║  MÉTODO    ║  ENDPOINT                         ║  DESCRIÇÃO           ║
╠════════════╬═══════════════════════════════════╬══════════════════════╣
║  GET       ║  /api/v1/latest-products/         ║  8 mais recentes     ║
║  POST      ║  /api/v1/products/search/         ║  Busca               ║
║  GET       ║  /api/v1/products/<cat>/<prod>/   ║  Detalhes produto    ║
║  GET       ║  /api/v1/products/<category>/     ║  Por categoria       ║
╚════════════╩═══════════════════════════════════╩══════════════════════╝
```

```
╔═══════════════════════════════════════════════════════════════════════╗
║                           PEDIDOS [AUTH]                              ║
╠════════════╦═══════════════════════════════════╦══════════════════════╣
║  MÉTODO    ║  ENDPOINT                         ║  DESCRIÇÃO           ║
╠════════════╬═══════════════════════════════════╬══════════════════════╣
║  POST      ║  /api/v1/checkout/                ║  Finalizar compra    ║
║  GET       ║  /api/v1/orders/                  ║  Histórico pedidos   ║
╚════════════╩═══════════════════════════════════╩══════════════════════╝
```

**Autenticação:**

Endpoints marcados `[AUTH]` requerem header:

```
Authorization: Token <seu_token_aqui>
```

**Exemplo Checkout:**

```bash
POST /api/v1/checkout/
Headers:
  Authorization: Token abc123...
  Content-Type: application/json

Body:
{
  "first_name": "João",
  "last_name": "Silva",
  "email": "joao@example.com",
  "phone": "11999999999",
  "address": "Rua Exemplo, 123",
  "zipcode": "01234-567",
  "place": "Centro",
  "stripe_token": "tok_visa",
  "items": [
    {
      "product": 1,
      "quantity": 2,
      "price": 29.90
    }
  ]
}
```

---

## Roadmap

Ver [docs/ROADMAP.md](docs/ROADMAP.md) para planejamento completo.

### Fase 1: Restauração (Jan 2026) - EM ANDAMENTO

```
[x] Diagnóstico completo (Python, Django, npm, Netlify)
[x] Atualização Python 3.14 + Django 4.2.17 LTS
[x] Resolução de 20 vulnerabilidades npm críticas (68 => 8)
[x] Correção configuração Netlify (Node.js => Django)
[ ] Configurar env vars (SECRET_KEY, STRIPE_KEY)
[ ] Deploy backend (Render.com)
[ ] Deploy frontend (Netlify)
[ ] Validação end-to-end
```

### Fase 2: Modernização (Fev-Mar 2026)

```
[ ] Migração Vue CLI => Vite
[ ] Atualização Vue.js 3.2 => 3.5+
[ ] Resolução 8 vulnerabilidades dev-only restantes
[ ] Suite de testes backend (pytest, >90% coverage)
[ ] Suite de testes frontend (Vitest, >90% coverage)
[ ] Documentação: Business Rules, ADRs, API docs
```

### Fase 3: Produção (Abr+ 2026)

```
[ ] CI/CD GitHub Actions
[ ] Observabilidade (logs, métricas, alertas)
[ ] Performance optimization
[ ] Features novas (analytics, relatórios)
```

---

## Documentação Técnica

| Documento                                   | Descrição                                         |
| ------------------------------------------- | ------------------------------------------------- |
| [ROADMAP.md](docs/ROADMAP.md)               | Planejamento completo da revitalização            |
| [ARCHITECTURE.md](docs/ARCHITECTURE.md)     | Stack técnico, decisões arquiteturais (planejado) |
| [BUSINESS_RULES.md](docs/BUSINESS_RULES.md) | Regras de negócio formalizadas (planejado)        |
| [DEPLOYMENT.md](docs/DEPLOYMENT.md)         | Instruções de deploy (planejado)                  |
| [decisions/](docs/decisions/)               | Architecture Decision Records (planejado)         |
| [CHANGELOG.md](CHANGELOG.md)                | Histórico de versões (planejado)                  |

---

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

## Você é livre para usar, copiar, modificar e distribuir este software para qualquer finalidade, inclusive comercial, desde que mantenha o aviso de copyright e a licença.

## Agradecimentos

- **Coding4Hope:** Programa acadêmico que originou o projeto
- **ONG Parceira:** Por confiar na solução proposta

---

## Disclaimer

Projeto independente para aprendizado e demonstração de habilidades em Full-Stack Development. Não há vínculo oficial com organizações mencionadas.

**Stripe:** Utilizado em modo de teste (test keys). Nenhuma transação real é processada.

---

**Última atualização em:** 07/01/2026  
**Versão:** 2.0.0 Revitalização
