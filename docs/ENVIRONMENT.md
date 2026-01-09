# Configuração de Ambiente

**Versão:** 2.0.1  
**Última atualização em:** 09/01/2026

---

## Visão Geral

O projeto utiliza variáveis de ambiente para gerenciamento de configurações sensíveis e específicas de cada ambiente de execução. Esta abordagem segue a metodologia 12-Factor App, externalizando configurações do código-fonte.

**Estratégia de Configuração:**

- Desenvolvimento local: arquivos `.env` gerenciados via python-dotenv
- Produção: variáveis configuradas diretamente na plataforma de deploy

---

## Referência de Variáveis

### Configurações Core do Django

| Variável        | Obrigatória | Padrão                | Descrição                                                          |
| --------------- | ----------- | --------------------- | ------------------------------------------------------------------ |
| `SECRET_KEY`    | Sim         | None                  | Chave criptográfica do Django. Gerar com `get_random_secret_key()` |
| `DEBUG`         | Não         | `False`               | Ativa/desativa modo debug. Deve ser `False` em produção            |
| `ALLOWED_HOSTS` | Não         | `localhost,127.0.0.1` | Lista separada por vírgula de hosts/domínios permitidos            |

### Configuração de Database

| Variável       | Obrigatória | Padrão                 | Descrição                                                        |
| -------------- | ----------- | ---------------------- | ---------------------------------------------------------------- |
| `DATABASE_URL` | Não         | `sqlite:///db.sqlite3` | String de conexão do banco. PostgreSQL recomendado para produção |

### Serviços Externos

| Variável            | Obrigatória | Padrão | Descrição                                                    |
| ------------------- | ----------- | ------ | ------------------------------------------------------------ |
| `STRIPE_SECRET_KEY` | Não         | Empty  | Chave secreta da API Stripe para processamento de pagamentos |
| `STRIPE_PUBLIC_KEY` | Não         | Empty  | Chave pública da API Stripe para integração frontend         |

### Segurança e CORS

| Variável               | Obrigatória | Padrão                  | Descrição                                                  |
| ---------------------- | ----------- | ----------------------- | ---------------------------------------------------------- |
| `CORS_ALLOWED_ORIGINS` | Não         | `http://localhost:8080` | Lista separada por vírgula de origens permitidas para CORS |

---

## Configuração para Desenvolvimento Local

### Setup Inicial

```bash
# Copiar template
cp .env.example .env

# Gerar SECRET_KEY
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

# Editar .env e configurar SECRET_KEY
```

### Exemplo de `.env` para Desenvolvimento

```bash
SECRET_KEY=<gerar-com-get-random-secret-key>
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
STRIPE_SECRET_KEY=sk_test_<sua-chave-teste>
STRIPE_PUBLIC_KEY=pk_test_<sua-chave-teste>
CORS_ALLOWED_ORIGINS=http://localhost:8080
```

### Validação da Configuração

```bash
# Verificar se configurações carregam corretamente
python manage.py check

# Verificar SECRET_KEY
python manage.py shell -c "from django.conf import settings; print('SECRET_KEY carregada:', bool(settings.SECRET_KEY))"
```

---

## Deploy em Produção

### Render.com (Backend)

Configurar variáveis de ambiente no dashboard do Render:

```bash
SECRET_KEY=<gerar-nova-chave-producao>
DEBUG=False
ALLOWED_HOSTS=<sua-app>.onrender.com
DATABASE_URL=<connection-string-postgres>
STRIPE_SECRET_KEY=<chave-producao-stripe>
STRIPE_PUBLIC_KEY=<chave-producao-stripe>
CORS_ALLOWED_ORIGINS=https://<seu-frontend>.netlify.app
```

### Netlify (Frontend)

Configurar variáveis de ambiente no dashboard do Netlify:

```bash
VUE_APP_API_URL=https://<seu-backend>.onrender.com
VUE_APP_STRIPE_PUBLIC_KEY=<chave-producao-stripe>
```

### Supabase (Database)

Obter connection string do PostgreSQL no dashboard do Supabase e configurar como `DATABASE_URL` no Render.

Formato: `postgresql://user:password@host:5432/database`

---

## Considerações de Segurança

### Checklist de Produção

- [ ] Arquivo `.env` excluído do controle de versão (verificar `.gitignore`)
- [ ] `SECRET_KEY` gerada com `get_random_secret_key()` do Django
- [ ] `DEBUG=False` configurado em produção
- [ ] `ALLOWED_HOSTS` restrito aos domínios reais
- [ ] Database configurado com PostgreSQL (não SQLite)
- [ ] Credenciais Stripe usando chaves de produção (não test mode)
- [ ] `CORS_ALLOWED_ORIGINS` restrito apenas a domínios confiáveis
- [ ] HTTPS/SSL habilitado em todos os domínios
- [ ] Variáveis de ambiente configuradas na plataforma de deploy

### Troubleshooting Comum

**ImproperlyConfigured: SECRET_KEY must not be empty**

- Causa: Arquivo `.env` ausente ou `SECRET_KEY` não configurada
- Solução: Criar `.env` a partir do template e configurar `SECRET_KEY`

**Module 'dotenv' not found**

- Causa: Pacote `python-dotenv` não instalado
- Solução: Executar `pip install python-dotenv`

**Warning: STRIPE_SECRET_KEY not configured**

- Causa: Integração Stripe não configurada (não-crítico)
- Solução: Opcional - configurar credenciais Stripe se processamento de pagamento for necessário

---

## Referências

- [Django Settings Best Practices](https://django-best-practices.readthedocs.io/en/latest/configuration.html)
- [12-Factor App: Config](https://12factor.net/config)
- [Documentação python-dotenv](https://pypi.org/project/python-dotenv/)

---

**Próxima Revisão:** Após conclusão do deploy Fase 1
