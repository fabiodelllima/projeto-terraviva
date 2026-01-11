# Configuração de Ambiente

**Versão:** 2.1.0  
**Última atualização:** 11/01/2026

---

## Visão Geral

O projeto utiliza variáveis de ambiente para configurações sensíveis, seguindo a metodologia 12-Factor App.

---

## Variáveis de Ambiente

### Django Core

| Variável        | Obrigatória | Padrão                | Descrição                  |
| --------------- | ----------- | --------------------- | -------------------------- |
| `SECRET_KEY`    | Sim         | -                     | Chave criptográfica Django |
| `DEBUG`         | Não         | `False`               | Modo debug                 |
| `ALLOWED_HOSTS` | Não         | `localhost,127.0.0.1` | Hosts permitidos           |

### Database

| Variável       | Obrigatória | Padrão                 | Descrição                    |
| -------------- | ----------- | ---------------------- | ---------------------------- |
| `DATABASE_URL` | Não         | `sqlite:///db.sqlite3` | Connection string PostgreSQL |

### Supabase Storage

| Variável                  | Obrigatória | Padrão  | Descrição               |
| ------------------------- | ----------- | ------- | ----------------------- |
| `SUPABASE_URL`            | Não         | -       | URL do projeto Supabase |
| `SUPABASE_SERVICE_KEY`    | Não         | -       | Service role key        |
| `SUPABASE_STORAGE_BUCKET` | Não         | `media` | Nome do bucket          |

### Stripe

| Variável            | Obrigatória | Padrão | Descrição            |
| ------------------- | ----------- | ------ | -------------------- |
| `STRIPE_SECRET_KEY` | Não         | -      | Chave secreta Stripe |
| `STRIPE_PUBLIC_KEY` | Não         | -      | Chave pública Stripe |

### CORS

| Variável               | Obrigatória | Padrão                  | Descrição          |
| ---------------------- | ----------- | ----------------------- | ------------------ |
| `CORS_ALLOWED_ORIGINS` | Não         | `http://localhost:8080` | Origens permitidas |

---

## Desenvolvimento Local

```bash
cp .env.example .env
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
# Editar .env com a SECRET_KEY gerada
```

### Exemplo .env

```bash
SECRET_KEY=sua-chave-aqui
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
CORS_ALLOWED_ORIGINS=http://localhost:8080
```

---

## Produção

### Render.com (Backend)

```bash
SECRET_KEY=<nova-chave-producao>
DEBUG=False
ALLOWED_HOSTS=terraviva-api-bg8s.onrender.com
DATABASE_URL=postgresql://user:pass@host:5432/db
SUPABASE_URL=https://xxx.supabase.co
SUPABASE_SERVICE_KEY=<service_role_key>
SUPABASE_STORAGE_BUCKET=media
STRIPE_SECRET_KEY=sk_live_xxx
CORS_ALLOWED_ORIGINS=https://terraviva.vercel.app
```

### Vercel (Frontend)

```bash
VUE_APP_API_URL=https://terraviva-api-bg8s.onrender.com
VUE_APP_STRIPE_PUBLIC_KEY=pk_live_xxx
```

---

## Checklist de Segurança

- [ ] `.env` no `.gitignore`
- [ ] `SECRET_KEY` única para produção
- [ ] `DEBUG=False` em produção
- [ ] `ALLOWED_HOSTS` restrito
- [ ] `SUPABASE_SERVICE_KEY` nunca no frontend
- [ ] HTTPS habilitado

---

**Próxima revisão:** Após Fase 2
