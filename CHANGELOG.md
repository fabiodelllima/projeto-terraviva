# CHANGELOG

Todas as mudanças notáveis do projeto Terra Viva serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto adere ao [Semantic Versioning](https://semver.org/lang/pt-BR/).

---

## [Unreleased]

### Em Desenvolvimento

- Configuração de env vars (SECRET_KEY, STRIPE_KEY)
- Deploy backend em Render.com
- Deploy frontend em Netlify
- Deploy database em Supabase
- Automação GitHub Actions (Supabase keep-alive)
- Documentação ARCHITECTURE.md
- Documentação BUSINESS_RULES.md
- Documentação DEPLOYMENT.md

---

## [2.0.0] - 2026-01-07

### Contexto

Início da **revitalização completa** do projeto após 4 anos sem manutenção (2022-2025). O objetivo é transformar o projeto acadêmico de 2021 em case para portfólio profissional de produção.

### Adicionado

- **Documentação Profissional Completa**

  - README.md reformulado com metodologia hierárquica
  - docs/ROADMAP.md com planejamento Fase 1, 2, 3
  - CHANGELOG.md seguindo Keep a Changelog format
  - Estrutura docs/ criada

- **Configuração Deploy Separado**
  - netlify.toml atualizado para Django deployment
  - Planejamento arquitetura: Backend (Render) + Frontend (Netlify) + Database (Supabase)
  - Decisão arquitetural: Separação backend/frontend (ADR-001)
  - Workflow GitHub Actions para Supabase keep-alive (ping a cada 5 dias)

### Modificado

- **Backend Dependencies (Python)**

  - Python: 3.9 => 3.14.2
  - Django: 4.1.2 => 4.2.17 LTS
  - Pillow: 9.2.0 => 10.4.0 (compatibilidade Python 3.14)
  - psycopg2-binary: 2.9.4 => 2.9.10
  - cryptography: 38.0.1 => 43.0.3
  - urllib3: 1.26.12 => 2.2.3
  - requests: 2.28.1 => 2.32.3
  - certifi: 2022.9.24 => 2024.12.14
  - Django REST Framework: 3.14.0 => 3.15.2
  - djoser: 4.8.0 => 5.3.1
  - Stripe: 4.2.0 => 11.3.0

- **Frontend Dependencies (npm)**

  - Resolvidas 20 vulnerabilidades críticas/altas
  - @babel/\* packages atualizados (ReDoS, code execution fixes)
  - webpack e loader-utils (XSS, prototype pollution fixes)
  - semver, minimist, json5, braces (critical issues)
  - ws (DoS vulnerability)
  - Vulnerabilidades: 68 => 8 (todas moderate, dev-only)

- **Configuração Netlify**

  - netlify.toml: Configurado para Python/Django deployment
  - Build command: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
  - Publish directory: `staticfiles`
  - Python version: 3.13.11

- **Metodologia Desenvolvimento**
  - Git workflow: feature branch → develop → main
  - Formato commits: `type(scope): Description` (inglês)
  - Documentação: Docs-First approach

### Removido

- runtime.txt (redundante com .python-version)

### Corrigido

- Incompatibilidade Python 3.14 + Pillow 9.2.0
- Incompatibilidade Python 3.14 + psycopg2-binary 2.9.4
- Configuração Netlify conflitante (esperava Node.js, projeto é Django)

### Segurança

- Resolvidas 20 de 28 vulnerabilidades npm (68 → 8)
- 8 vulnerabilidades restantes: moderate severity, dev-only
  - postcss <8.4.31 (parsing error)
  - webpack-dev-server <=5.2.0 (source code theft via malicious site)
- **CRÍTICO:** SECRET_KEY e STRIPE_KEY ainda hardcoded (resolver em Fase 1)

### Técnico

- Branch atual: `chore/phase-1-restoration`
- Database planejado: Supabase PostgreSQL (500MB free forever)
  - Automação: GitHub Actions ping a cada 5 dias (evita pause)
- Backend deploy: Render.com (sleep 15min aceitável para portfólio)
- Frontend deploy: Netlify (já configurado)

---

## [1.0.0] - 2021-12-XX

### Contexto

Release inicial do projeto acadêmico **Coding4Hope**. Plataforma e-commerce desenvolvida para automatizar vendas de uma ONG, substituindo processos manuais por sistema online completo.

### Adicionado

- **Backend Django**

  - Django 4.1.2 + Django REST Framework
  - Apps: `product`, `order`
  - Models: Product, Category, Order, OrderItem
  - API REST completa (CRUD produtos, checkout, auth)
  - Admin panel integrado
  - Integração Stripe (pagamentos)
  - Geração automática de thumbnails (Pillow)
  - Autenticação via djoser + Token Authentication

- **Frontend Vue.js**

  - Vue.js 3.2.13 + Vue Router + Vuex
  - 10 páginas: Home, Product, Category, Search, Cart, Checkout, Success, Login, SignUp, MyAccount
  - 3 componentes: ProductBox, CartItem, OrderSummary
  - State management: carrinho persistente (localStorage)
  - Integração Stripe Elements
  - CSS framework: Bulma
  - Notificações: Bulma Toast

- **Funcionalidades Principais**

  - Catálogo de produtos com busca
  - Carrinho de compras
  - Checkout completo (dados pessoais + pagamento)
  - Histórico de pedidos
  - Autenticação (login/registro)
  - Admin panel para gestão

- **Infraestrutura Original**
  - Deploy: Heroku (backend + frontend)
  - Database: SQLite (dev), PostgreSQL (prod)
  - django-on-heroku configurado
  - Procfile para Heroku
  - CORS configurado

### Impacto

Projeto entregue com sucesso à ONG, demonstrando viabilidade técnica e impacto social mensurável. Sistema substituiu processos analógicos (planilhas Excel, anotações físicas) por plataforma digital completa, reduzindo ~40% do tempo gasto em tarefas repetitivas e permitindo vendas online.

---

## Legenda

### Tipos de Mudanças

- `Adicionado`: Novas funcionalidades
- `Modificado`: Mudanças em funcionalidades existentes
- `Removido`: Funcionalidades removidas
- `Corrigido`: Correções de bugs
- `Segurança`: Correções de vulnerabilidades
- `Descontinuado`: Funcionalidades que serão removidas no futuro

### Formato Versionamento

```
MAJOR.MINOR.PATCH

MAJOR: Mudanças incompatíveis de API
MINOR: Funcionalidades novas compatíveis
PATCH: Correções de bugs compatíveis
```

**Exemplo:**

- 1.0.0 => 1.0.1: Bug fix (patch)
- 1.0.1 => 1.1.0: Nova feature (minor)
- 1.1.0 => 2.0.0: Breaking change (major)

---

**Última atualização:** 07/01/2026  
**Versão atual:** 2.0.0 (Revitalização)
