# ROADMAP

**Projeto:** Terra Viva  
**Versão:** 2.0.0 Revitalização em 2026

---

## Índice

- [Visão Geral](#visão-geral)
- [Estado Atual](#estado-atual)
- [Arquitetura](#arquitetura)
- [Fase 1: Restauração](#fase-1-restauração)
- [Fase 2: Modernização](#fase-2-modernização)
- [Fase 3: Produção](#fase-3-produção)
- [Cronograma](#cronograma)
- [Decisões de Infraestrutura](#decisões-de-infraestrutura)
- [Riscos e Mitigações](#riscos-e-mitigações)

---

## Visão Geral

Transformar projeto acadêmico de 2021 (quebrado há 4+ anos) em portfólio profissional de produção com stack moderna e deploy funcional em plataformas que oferecem Free Tier.

### Objetivos Principais

```
┌────────────────────────────────────────────────────────────┐
│  OBJETIVO                  │ STATUS    │ PRIORIDADE        │
├────────────────────────────────────────────────────────────┤
│  Deploy funcional (back)   │ PENDENTE  │ CRÍTICO           │
│  Deploy funcional (front)  │ PENDENTE  │ CRÍTICO           │
│  Modernizar stack          │ PARCIAL   │ ALTO              │
│  Eliminar vulnerabilidades │ PARCIAL   │ ALTO              │
│  Implementar testes        │ PENDENTE  │ MÉDIO             │
│  Documentar completamente  │ ANDAMENTO │ MÉDIO             │
│  CI/CD automatizado        │ PENDENTE  │ BAIXO             │
└────────────────────────────────────────────────────────────┘
```

### Filosofia de Desenvolvimento

- **Incremental:** Deploy funcional primeiro, otimizações depois
- **Pragmático:** Free tier suficiente para portfólio, não precisa ser enterprise-grade
- **Documentado:** Decisões arquiteturais registradas em ADRs
- **Testado:** >90% coverage como meta na Fase 2

---

## Estado Atual

### Status por Componente

```
╔═══════════════════════════════════════════════════════════╗
║  BACKEND (Django 4.2.17 LTS + Python 3.14.2)              ║
╠═══════════════════════════════════════════════════════════╣
║  [x] Python 3.14.2 compatível                             ║
║  [x] Django 4.2.17 LTS atualizado                         ║
║  [x] Dependencies críticas atualizadas (Pillow, psycopg)  ║
║  [ ] SECRET_KEY comentada (CRÍTICO)                       ║
║  [ ] STRIPE_KEY hardcoded (CRÍTICO)                       ║
║  [ ] DEBUG=True (INSEGURO)                                ║
║  [ ] ALLOWED_HOSTS=[] (DEPLOY FALHA)                      ║
║  [ ] Deploy quebrado há 4+ anos                           ║
║  [ ] SQLite (produção precisa PostgreSQL)                 ║
║  [ ] Configuração conflitante (Heroku vs Netlify)         ║
╚═══════════════════════════════════════════════════════════╝

╔═══════════════════════════════════════════════════════════╗
║  FRONTEND (Vue.js 3.2.13 + Vue CLI 5.0)                   ║
╠═══════════════════════════════════════════════════════════╣
║  [x] Vulnerabilidades: 68 => 8 (críticas resolvidas)      ║
║  [ ] Vue.js 3.2.13 (2021, desatualizado)                  ║
║  [ ] Vue CLI 5.0 (8 vulnerabilidades dev-only)            ║
║  [ ] axios.baseURL hardcoded (localhost)                  ║
║  [ ] Deploy não configurado                               ║
║  [ ] Sem testes                                           ║
╚═══════════════════════════════════════════════════════════╝

╔═══════════════════════════════════════════════════════════╗
║  INFRAESTRUTURA                                           ║
╠═══════════════════════════════════════════════════════════╣
║  [ ] Procfile (Heroku) + netlify.toml (Netlify) CONFLITO  ║
║  [ ] django-on-heroku instalado mas sem Heroku            ║
║  [ ] Netlify redirects para functions inexistentes        ║
║  [ ] CORS configurado apenas para localhost:8080          ║
║  [ ] Sem CI/CD                                            ║
╚═══════════════════════════════════════════════════════════╝
```

### Débito Técnico Acumulado

| Categoria     | Item                    | Impacto | Estimativa  |
| ------------- | ----------------------- | ------- | ----------- |
| **Segurança** | SECRET_KEY exposta      | CRÍTICO | 1h          |
| **Segurança** | STRIPE_KEY hardcoded    | CRÍTICO | 1h          |
| **Segurança** | 8 CVEs npm dev-only     | BAIXO   | 2-4 semanas |
| **Config**    | settings.py produção    | ALTO    | 2-3h        |
| **Deploy**    | Infraestrutura quebrada | CRÍTICO | 1-2 dias    |
| **Frontend**  | baseURL hardcoded       | ALTO    | 1h          |
| **Database**  | SQLite => PostgreSQL    | MÉDIO   | 2-3h        |
| **Testes**    | 0% coverage             | MÉDIO   | 2-4 semanas |
| **Docs**      | README básico           | BAIXO   | 1-2 dias    |

---

## Arquitetura

### Diagrama da Infraestrutura

```
        ┌────────────────────────────────────────┐
        │         CLOUDFLARE DNS (Futuro)        │
        │         SSL/CDN (Opcional)             │
        └──────────────┬─────────────────────────┘
                       │
           ┌───────────┴───────────┐
           │                       │
           ▼                       ▼
┌──────────────────────┐  ┌──────────────────────┐
│   NETLIFY (Free)     │  │   RENDER.COM (Free)  │
│   ───────────────    │  │   ────────────────   │
│   Frontend SPA       │  │   Django API         │
│   Vue.js Build       │  │   + gunicorn         │
│   Static Files       │  │   + WhiteNoise       │
│   ─────────────      │  │   ─────────────      │
│   ✓ CDN Global       │  │   ! Sleep 15min      │
│   ✓ SSL Auto         │  │   ✓ SSL Auto         │
│   ✓ Deploy Git       │  │   ✓ Deploy Git       │
└──────────────────────┘  └──────────┬───────────┘
                                     │
                          ┌──────────┴───────────┐
                          │                      │
                          ▼                      ▼
                 ┌─────────────────┐   ┌─────────────────┐
                 │  NEON.TECH or   │   │  STRIPE API     │
                 │  SUPABASE       │   │  (Pagamentos)   │
                 │  ─────────────  │   │  ─────────────  │
                 │  PostgreSQL     │   │  Webhook Future │
                 │  ─────────────  │   └─────────────────┘
                 │  ✓ Free forever │
                 │  ✓ 3GB storage  │
                 │  ✓ Backups auto │
                 └─────────────────┘
```

### Stack Tecnológico Final

```
╔═══════════════════════════════════════════════════════════╗
║                    STACK PROPOSTA v2.0.0                  ║
╠═══════════════════════════════════════════════════════════╣
║                                                           ║
║  Backend (Python)                                         ║
║  ├── Python 3.14.2                                        ║
║  ├── Django 4.2.17 LTS (suporte até 04/2026)              ║
║  ├── Django REST Framework 3.15.2                         ║
║  ├── djoser 2.2.3 (auth)                                  ║
║  ├── gunicorn (WSGI server)                               ║
║  ├── psycopg2-binary 2.9.10                               ║
║  ├── Pillow 10.4.0                                        ║
║  ├── Stripe 11.3.0                                        ║
║  └── WhiteNoise (static files)                            ║
║                                                           ║
║  Frontend (JavaScript)                                    ║
║  ├── Vue.js 3.5+ (upgrade planejado)                      ║
║  ├── Vite (migração planejada)                            ║
║  ├── Vue Router 4.x                                       ║
║  ├── Pinia (Vuex successor)                               ║
║  ├── Axios 1.x                                            ║
║  └── Bulma CSS                                            ║
║                                                           ║
║  Database                                                 ║
║  ├── PostgreSQL 15+ (Neon.tech ou Supabase)               ║
║  └── Migrations via Django ORM                            ║
║                                                           ║
║  Infraestrutura                                           ║
║  ├── Backend: Render.com Web Service                      ║
║  ├── Frontend: Netlify                                    ║
║  ├── Database: Neon.tech ou Supabase                      ║
║  ├── CI/CD: GitHub Actions (Fase 3)                       ║
║  └── Monitoring: Sentry (Fase 3, opcional)                ║
║                                                           ║
║  Qualidade (Fase 2)                                       ║
║  ├── pytest + pytest-django                               ║
║  ├── pytest-cov (>90% target)                             ║
║  ├── Vitest (frontend)                                    ║
║  ├── ruff (linter)                                        ║
║  └── mypy (type checker)                                  ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
```

---

## Fase 1: Restauração

**Objetivo:** Deploy funcional backend + frontend (quebrado desde 2022)

**Duração Estimada:** 2-3 semanas (jan/2026)

**Critérios de Sucesso:**

- ✓ Backend rodando em Render.com
- ✓ Frontend rodando em Netlify
- ✓ Fluxo completo funcional: Home => Produto => Carrinho => Checkout => Success
- ✓ Integração Stripe funcionando
- ✓ PostgreSQL configurado
- ✓ HTTPS em ambos

### Tarefas Backend

```
[1.1] Configuração Produção (2-3 horas)
├── [✗] Criar .env.example com todas variáveis
├── [✗] Mover SECRET_KEY para env var
├── [✗] Mover STRIPE_SECRET_KEY para env var
├── [✗] Configurar ALLOWED_HOSTS dinâmico
├── [✗] DEBUG = False em produção
├── [✗] Configurar CORS para domínio Netlify
├── [✗] Adicionar gunicorn no requirements.txt
└── [✗] Remover django-on-heroku

[1.2] Database Migration (2-3 horas)
├── [✗] Criar conta Neon.tech ou Supabase
├── [✗] Criar PostgreSQL database
├── [✗] Configurar DATABASE_URL
├── [✗] Testar conexão local
├── [✗] Rodar migrations
└── [✗] Popular com dados de exemplo (opcional)

[1.3] Deploy Render (2-4 horas)
├── [✗] Criar conta Render.com
├── [✗] Criar Web Service (conectar GitHub)
├── [✗] Configurar env vars (SECRET_KEY, STRIPE_KEY, DATABASE_URL)
├── [✗] Configurar build command
├── [✗] Configurar start command (gunicorn)
├── [✗] Deploy inicial
└── [✗] Testar endpoints via Postman/cURL

[1.4] Validação Backend (1-2 horas)
├── [✗] GET /api/v1/latest-products/ → 200 OK
├── [✗] POST /api/v1/auth/users/ → Criar usuário
├── [✗] POST /api/v1/auth/token/login/ → Obter token
├── [✗] POST /api/v1/checkout/ → Processar pagamento (Stripe test mode)
└── [✗] Admin panel acessível
```

### Tarefas Frontend

```
[1.5] Configuração Env Vars (1 hora)
├── [✗] Criar .env.local
├── [✗] Criar .env.production
├── [✗] Adicionar VUE_APP_API_URL
├── [✗] Adicionar VUE_APP_STRIPE_PUBLIC_KEY
└── [✗] Atualizar axios baseURL para usar env var

[1.6] Deploy Netlify (1-2 horas)
├── [✗] Configurar build settings (npm run build)
├── [✗] Configurar publish directory (dist/)
├── [✗] Adicionar env vars no Netlify
├── [✗] Deploy inicial
└── [✗] Configurar redirects SPA (/_redirects ou netlify.toml)

[1.7] Validação Frontend (1-2 horas)
├── [✗] Home carrega produtos
├── [✗] Busca funciona
├── [✗] Adicionar ao carrinho
├── [✗] Login/Signup
├── [✗] Checkout completo
└── [✗] Success page após pagamento
```

### Cleanup Configs

```
[1.8] Remover Configurações Obsoletas (30min)
├── [✗] Remover Procfile (Heroku)
├── [✗] Remover django-on-heroku de requirements.txt
├── [✗] Atualizar netlify.toml (remover redirects Django)
└── [✗] Atualizar .gitignore (.env*, .venv/, etc)
```

### Documentação Fase 1

```
[1.9] Documentar Setup (2-3 horas)
├── [✗] README.md completo
├── [✗] docs/DEPLOYMENT.md (instruções deploy)
├── [✗] docs/ENVIRONMENT.md (env vars)
├── [✗] docs/ARCHITECTURE.md (diagrama infraestrutura)
└── [✗] CHANGELOG.md (registrar mudanças)
```

---

## Fase 2: Modernização

**Objetivo:** Stack moderno, vulnerabilidades zero, testes >90%

**Duração Estimada:** 4-6 semanas (fev-mar/2026)

**Critérios de Sucesso:**

- ✓ Vue.js 3.5+
- ✓ Vite como build tool
- ✓ 0 vulnerabilidades npm
- ✓ >90% test coverage backend
- ✓ >90% test coverage frontend
- ✓ Business Rules documentadas
- ✓ ADRs criados

### Tarefas Frontend

```
[2.1] Migração Vue CLI → Vite (1-2 semanas)
├── [✗] Criar branch feat/migrate-to-vite
├── [✗] Instalar Vite + plugins
├── [✗] Migrar vite.config.js
├── [✗] Atualizar imports (@ → relative paths se necessário)
├── [✗] Testar build local
├── [✗] Atualizar scripts package.json
├── [✗] Deploy teste
└── [✗] Merge para develop

[2.2] Atualização Vue.js (1 semana)
├── [✗] Atualizar Vue 3.2 → 3.5+
├── [✗] Atualizar Vue Router
├── [✗] Migrar Vuex → Pinia
├── [✗] Testar compatibilidade
└── [✗] Deploy

[2.3] Resolução Vulnerabilidades (1-2 semanas)
├── [✗] Tentar npm audit fix --force
├── [✗] Avaliar breaking changes
├── [✗] Atualizar dependências manualmente se necessário
└── [✗] Validar 0 vulnerabilidades

[2.4] Testes Frontend (2-3 semanas)
├── [✗] Configurar Vitest
├── [✗] Testes unitários componentes (>90%)
├── [✗] Testes integração (routes, store)
├── [✗] E2E com Playwright ou Cypress (smoke tests)
└── [✗] CI rodando testes
```

### Tarefas Backend

```
[2.5] Testes Backend (2-3 semanas)
├── [✗] Configurar pytest + pytest-django
├── [✗] Testes models (Product, Order, Category)
├── [✗] Testes views/endpoints (API completa)
├── [✗] Testes serializers
├── [✗] Testes integração (Stripe mock)
├── [✗] Coverage >90%
└── [✗] CI rodando testes

[2.6] Qualidade Código (1 semana)
├── [✗] Configurar ruff (linter + formatter)
├── [✗] Configurar mypy (type hints)
├── [✗] Pre-commit hooks
├── [✗] Aplicar em toda codebase
└── [✗] CI validando qualidade
```

### Documentação Fase 2

```
[2.7] Business Rules & ADRs (1-2 semanas)
├── [✗] docs/BUSINESS_RULES.md
│   ├── BR-PRODUCT-001: Validação produto
│   ├── BR-ORDER-001: Fluxo checkout
│   ├── BR-AUTH-001: Autenticação
│   └── BR-PAYMENT-001: Integração Stripe
├── [✗] docs/decisions/ (ADRs)
│   ├── ADR-001: Separação Backend/Frontend
│   ├── ADR-002: Render.com + Netlify
│   ├── ADR-003: Neon.tech para PostgreSQL
│   ├── ADR-004: Vite ao invés de Vue CLI
│   └── ADR-005: Pinia ao invés de Vuex
└── [✗] docs/DATA_GUIDE.md (dicionário dados)
```

---

## Fase 3: Produção

**Objetivo:** CI/CD, observabilidade, features novas

**Duração Estimada:** Contínuo (a partir abr/2026)

### Tarefas Infraestrutura

```
[3.1] CI/CD GitHub Actions (1-2 semanas)
├── [✗] Pipeline backend (lint → test → deploy)
├── [✗] Pipeline frontend (lint → test → build → deploy)
├── [✗] Deploy automático em push para main
├── [✗] Deploy preview em PRs
└── [✗] Notificações (Slack/Discord)

[3.2] Observabilidade (1 semana)
├── [✗] Sentry (error tracking)
├── [✗] Logs estruturados (Django)
├── [✗] Métricas básicas (requests, errors)
└── [✗] Alertas (downtime, erros críticos)

[3.3] Performance (1-2 semanas)
├── [✗] Django Debug Toolbar (dev)
├── [✗] Queries N+1 optimization
├── [✗] Cache (Redis futuro)
├── [✗] Frontend bundle optimization
└── [✗] Lighthouse CI (performance tracking)
```

### Features Novas

```
[3.4] Melhorias UX (backlog)
├── [✗] Dashboard admin customizado
├── [✗] Relatórios vendas
├── [✗] Gestão estoque
├── [✗] Categorias dinâmicas (navbar)
├── [✗] Filtros avançados produtos
├── [✗] Avaliações produtos
└── [✗] Wishlist

[3.5] Integrações (backlog)
├── [✗] Email marketing (Mailgun/SendGrid)
├── [✗] Analytics (Google Analytics)
├── [✗] SEO optimization
└── [✗] Webhooks Stripe (confirmação pagamento)
```

---

## Cronograma

```
╔═══════════════════════════════════════════════════════════╗
║  FASE        │ DURAÇÃO    │ PERÍODO         │ STATUS      ║
╠═══════════════════════════════════════════════════════════╣
║  Fase 1      │ 2-3 sem    │ Jan 2026        │ ANDAMENTO   ║
║  Fase 2      │ 4-6 sem    │ Fev-Mar 2026    │ PLANEJADO   ║
║  Fase 3      │ Contínuo   │ Abr+ 2026       │ PLANEJADO   ║
╚═══════════════════════════════════════════════════════════╝
```

### Timeline Detalhado

```
2026
────────────────────────────────────────────────────────────
JAN  │ ████████ Fase 1: Restauração
     │ └─ Semana 1-2: Backend config + deploy Render
     │ └─ Semana 2-3: Frontend config + deploy Netlify
     │
FEV  │ ████████ Fase 2: Modernização (início)
     │ └─ Semana 1-2: Migração Vite
     │ └─ Semana 3-4: Atualização Vue.js + Pinia
     │
MAR  │ ████████ Fase 2: Modernização (cont)
     │ └─ Semana 1-2: Testes backend
     │ └─ Semana 3-4: Testes frontend + docs
     │
ABR+ │ ████████ Fase 3: Produção (features contínuas)
     │ └─ CI/CD, observabilidade, otimizações
────────────────────────────────────────────────────────────
```

---

## Decisões de Infraestrutura

### ADR-001: Separação Backend/Frontend

**Status:** Aceito  
**Data:** 07/01/2026  
**Contexto:**

Projeto original tinha configuração ambígua (Heroku + tentativa Netlify). Precisamos definir arquitetura clara.

**Decisão:**

Separar completamente backend e frontend em deployments independentes.

**Consequências:**

```
Positivas:
├─ Escalabilidade independente
├─ Deploy independente (frontend changes não afetam backend)
├─ Padrão moderno (SPA + API)
└─ Mais fácil adicionar outros clientes (mobile app futuro)

Negativas:
├─ CORS precisa ser configurado
├─ Dois deployments para gerenciar
└─ Env vars duplicadas (API_URL, STRIPE_KEY)
```

**Alternativas Consideradas:**

- Monolito no Heroku (descartado: Heroku parou de oferecer free tier)
- Tudo no Netlify Functions (descartado: overengineering)

---

### ADR-002: Render.com para Backend

**Status:** Aceito  
**Data:** 07/01/2026  
**Contexto:**

Precisamos plataforma gratuita para backend Django com PostgreSQL.

**Decisão:**

Usar Render.com Web Service (free tier) + Neon.tech/Supabase PostgreSQL.

**Razões:**

```
Render.com:
✓ Free tier genuíno (750h/mês suficiente)
✓ PostgreSQL grátis (90 dias, mas Neon resolve)
✓ Interface similar Heroku (fácil migração)
✓ Deploy automático via Git
✓ SSL automático
✓ Comunidade ativa

Limitações Aceitáveis:
~ Sleep após 15min (ok para portfólio)
~ 512MB RAM (suficiente Django simples)
~ 0.1 CPU (suficiente baixo tráfego)
```

**Alternativas Consideradas:**

| Opção          | Prós            | Contras                     | Decisão |
| -------------- | --------------- | --------------------------- | ------- |
| Railway        | $5 crédito/mês  | Acaba rápido                | ✗       |
| Fly.io         | Bom free tier   | Excesso de refatorações     | ✗       |
| PythonAnywhere | Free Django     | MySQL apenas, limitado      | ✗       |
| Vercel         | Ótimo free tier | Serverless excessivo Django | ✗       |

---

### ADR-003: Neon.tech para PostgreSQL

**Status:** Aceito  
**Data:** 07/01/2026  
**Contexto:**

Render PostgreSQL free expira após 90 dias. Precisamos solução permanente.

**Decisão:**

Usar Neon.tech PostgreSQL free tier (3GB, permanente).

**Razões:**

```
Neon.tech:
✓ Free forever (não expira)
✓ 3GB storage (suficiente para portfólio)
✓ Backups automáticos
✓ Branching (dev/staging/prod)
✓ Serverless (não precisa gerenciar)

Alternativa: Supabase
✓ 500MB free (menor, mas ok)
✓ Inclui auth/storage extras
~ Mais completo (overkill para necessidade)
```

---

### ADR-004: Netlify para Frontend

**Status:** Aceito  
**Data:** 07/01/2026  
**Contexto:**

Projeto já usa Netlify mas configuração estava quebrada.

**Decisão:**

Manter Netlify, corrigir configuração.

**Razões:**

```
✓ Já configurado (conta existe)
✓ Free tier excelente (100GB bandwidth)
✓ Deploy automático Git
✓ SSL automático
✓ CDN global
✓ Preview deploys em PRs
```

**Alternativas:**

- Vercel (similar, sem necessidade de troca)
- GitHub Pages (suporte abaixo do necessário para SPA routing)

---

## Riscos e Mitigações

### Riscos Técnicos

```
╔═══════════════════════════════════════════════════════════╗
║  OPÇÃO            │ FREE TIER      │ RENOVAR?  │ DECISÃO  ║
╠═══════════════════════════════════════════════════════════╣
║  Neon.tech        │ 3GB PostgreSQL │ Não       │ ÓTIMO    ║
║  Supabase         │ 500MB Postgres │ Não       │ ÓTIMO    ║
║  PlanetScale      │ 5GB MySQL      │ Não       │ ÓTIMO    ║
║  Oracle Cloud     │ 20GB Oracle DB │ Não       │ ÓTIMO    ║
║  Render Postgres  │ 1GB Postgres   │ 90 dias   │ RUIM     ║
╚═══════════════════════════════════════════════════════════╝
```

### Mitigações

**Render Sleep:**

```
Aceitável para portfólio. Alternativas futuras:
├─ Upgrade para Render Starter ($7/mês)
├─ Migrar para VPS (DigitalOcean $5/mês)
└─ Implementar cron ping (não recomendado ToS)
```

**Database Backup:**

```
Rotina automática:
├─ Script semanal: pg_dump => S3/Google Drive
├─ Antes migrations: backup manual obrigatório
└─ Dados críticos: export CSV periódico
```

**Breaking Changes:**

```
Estratégia:
├─ Feature branch isolada
├─ Testes extensivos antes merge
├─ Deploy staging primeiro
└─ Rollback plan (git revert)
```

---

## Referências

### Documentação Externa

- [Render.com Docs](https://render.com/docs)
- [Neon.tech Docs](https://neon.tech/docs)
- [Netlify Docs](https://docs.netlify.com)
- [Django Deployment Checklist](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/)
- [Vue.js Production Deployment](https://vuejs.org/guide/best-practices/production-deployment.html)

### Documentação Interna

- [ARCHITECTURE.md](ARCHITECTURE.md) - Stack técnico detalhado
- [BUSINESS_RULES.md](BUSINESS_RULES.md) - Regras de negócio (Fase 2)
- [DEPLOYMENT.md](DEPLOYMENT.md) - Instruções deploy (Fase 1)
- [decisions/](decisions/) - ADRs completos

---

**Última revisão em:** 07/01/2026  
**Próxima revisão em:** Após conclusão da Fase 1
