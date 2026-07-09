# 🚀 SASS-X Sentinel — Primeiros Passos

> **Bem-vindo!** Sentinel é um **sistema de auditoria inteligente** que detecta vulnerabilidades, bugs, problemas arquiteturais e propõe soluções com código pronto. Pronto em **10 minutos**.

---

## 1️⃣ O que é Sentinel (30 segundos)

Você descreve um problema (ou aponta um arquivo/trecho). Sentinel:
1. **Analisa** o código com especialistas
2. **Encontra** vulnerabilidades + padrões ruins + bugs
3. **Propõe** soluções com código pronto (`before → after`)
4. **Entrega** relatório completo + roadmap de correção

**Tudo é:**
- ✅ Baseado em **evidência** (arquivo:linha)
- ✅ **Serial** (uma análise por vez)
- ✅ **Rastreável** (relatório gravado)

---

## 2️⃣ Arquitetura 6-Camadas (Validada ✅)

Sentinel funciona em **6 camadas** que você não precisa entender agora, mas são importantes:

```
┌─────────────────────────────────────────┐
│ L1: Orquestrador + Planejamento          │
│ L2: Token Budget + Cache (85% economia)  │
│ L3: Knowledge Graph + Padrões            │
│ L4: Agentes Especializados (paralelo)   │
├─ Segurança (OWASP, LGPD, Secrets)      │
├─ Qualidade (Bugs, SOLID, Code Smell)    │
├─ Observabilidade (APM, Logs)            │
├─ Arquitetura (Design Patterns)          │
├─ Performance (Gargalos)                 │
├─ E mais...                              │
│ L5: Consolidação + Validação            │
│ L6: Human Approval (CRÍTICO)            │
└─────────────────────────────────────────┘
```

**Status:** ✅ **24/24 testes PASSED** — Production-Ready

---

## 3️⃣ Primeiros 5 Minutos

### A. Prepare o Ambiente

```powershell
# Clone/abra esta pasta
cd c:\Estudos\sentinela-autonomo-engenharia-software

# Abra com seu assistente de IA (ex.: GitHub Copilot, Cursor)
# O arquivo SENTINEL.md carrega automaticamente
```

### B. Execute o Teste de Validação

```powershell
# Veja Sentinel em ação (3 cenários reais)
cd .saes\agents
python -m pytest tests/test_git_commit_e2e_scenarios.py -v -s
```

**Esperado:** `6 passed in 0.15s` ✅

### C. Leia os Resultados

```
workspace/
└─ teste-e2e-sentinel-3-cenarios/
   ├─ README.md                      ← Quick Start por perfil
   ├─ RELATORIO_E2E_SENTINEL.md      ← 13 achados completos
   ├─ QUADRO_COMPARATIVO_E2E.md      ← Análise visual + priorização
   ├─ SENTINELA_SUMARIO_EXECUTIVO.md ← Solutions pronta (código)
   └─ STATUS_VALIDACAO_COMPLETA.md   ← Timeline + metrics
```

---

## 4️⃣ Como Usar Sentinel

### Opção A: Análise Rápida (Read-Only)

```
Abra seu assistente de IA e digite:

"Audita meu endpoint POST /api/clientes do controller ClienteController.java"

Sentinel vai:
1. ✅ Encontrar vulnerabilidades
2. ✅ Propor soluções
3. ✅ Gerar relatório
```

### Opção B: Análise Completa (com Recomendações)

```
Descreva o contexto:

"Temos um sistema de cobrança em Spring Boot.
Há chamadas para API de pagamento externa (delays/timeouts).
Processamento em Kafka. Preciso saber se está resiliente."

Sentinel vai:
1. 📊 Mapear fluxo completo
2. 🔴 Encontrar CRÍTICOS (ex: sem circuit breaker)
3. 🟡 Encontrar ALTOs (ex: sem retry policy)
4. 🟢 Sugerir TUDO (com código)
```

---

## 5️⃣ Entender os Resultados

Sentinel entrega achados assim:

```json
{
  "id": "OWASP-001",
  "titulo": "SQL Injection no filtro de clientes",
  "severidade": "CRITICO",
  "arquivo": "src/java/ClienteRepository.java",
  "linha": 47,
  "evidencia": "String query = \"SELECT * FROM CLIENTES WHERE email='\" + email + \"'\"",
  "impacto": "Ataque SQL injection permite ler/deletar dados",
  "correcao": "Use PreparedStatement ou JPA com @Query + parameterização",
  "confianca": "ALTA"
}
```

### Régua de Severidade

| Nível | O que fazer | Timeline |
|-------|-----------|----------|
| 🔴 **CRÍTICO** | Parar tudo e corrigir | Imediato |
| 🟠 **ALTO** | Próxima sprint | 1-2 semanas |
| 🟡 **MÉDIO** | Backlog normal | 1 mês |
| 🟢 **BAIXO** | Nice to have | Sem pressa |

---

## 6️⃣ Quando Sentinel Propõe Código

Se o achado tiver solução pronta, Sentinel entrega:

```java
// ❌ ANTES (vulnerável)
String query = "SELECT * FROM CLIENTES WHERE email='" + email + "'";
Statement stmt = connection.createStatement();
ResultSet rs = stmt.executeQuery(query);

// ✅ DEPOIS (seguro)
String query = "SELECT * FROM CLIENTES WHERE email = ?";
PreparedStatement pstmt = connection.prepareStatement(query);
pstmt.setString(1, email);
ResultSet rs = pstmt.executeQuery();
```

**Você decide:** aceita a proposta ou pede ajustes.

---

## 7️⃣ Conhecer Seus Especialistas

Sentinel tem especialistas para diferentes problemas:

| Especialista | Detecta | Exemplo |
|------|---------|---------|
| **BugHunter** | Bugs reais | Null pointer, lógica errada |
| **OWASP** | Vulnerabilidades web | SQL Injection, XSS, CSRF |
| **SecureCode** | Práticas inseguras | Hard-coded secrets, crypto fraca |
| **Performance** | Gargalos | N+1, loops desnecessários |
| **CleanCode** | Code smell | Métodos gigantes, duplicação |
| **SOLID** | Design patterns | Violações SRP, OCP, DIP |
| **Observability** | Logging/Tracing | Eventos silenciosos, contexto perdido |
| **RootCause** | Raiz de crashes | Stack trace → diagnóstico |

---

## 8️⃣ Guia Rápido: De Um Git Commit a Insights

```powershell
# 1. Você faz commit
git add -A
git commit -m "feat: Ajuste de código no endpoint"

# 2. Sentinel é acionado automaticamente
# (se houver CI/CD ou hook local)

# 3. Analisa os arquivos alterados
# 4. Gera achados (em paralelo, 6-10s)
# 5. Consolida em relatório

# 6. Você lê relatório
cat workspace/ISSUE<N>/relatorio/2026-06-09_1432_feature_xxx.md

# 7. Aprova as soluções
# 8. Implementação automática (se MÉDIO/BAIXO)
# 9. Merge para develop/main
```

---

## 9️⃣ Relatórios — Onde Está Tudo

Toda análise gera um **relatório assinado**:

```
workspace/
├─ ISSUE123/
│  └─ relatorio/
│     ├─ 2026-06-09_1432_feature_cobranca.md  ← Relatório final
│     └─ ISSUE123-2026-06-09_1432.md          ← Diário de bordo
│
└─ _INDICE.md                                 ← Ledger (controla fila)
```

**Conteúdo do relatório:**
- ✅ Todos os achados (tabela estruturada)
- ✅ Evidência + impacto
- ✅ Soluções (before/after)
- ✅ Roadmap (priorização por severidade)
- ✅ Tempo estimado

---

## 🔟 As 5 Regras de Ouro

1. **Evidência sempre** → Sem `arquivo:linha`, não vale.
2. **Read-only por padrão** → Código só com sua aprovação.
3. **Uma análise por vez** → Serial (evita race condition).
4. **Checkpoint em cada etapa** → Pode pausar e retomar.
5. **Gatilhos só de você** → Ninguém tira decisões por você.

---

## 📚 Mais Informações

| Documento | Para Quem | Leia |
|-----------|-----------|------|
| **README.md** | Todos | Visão geral + status |
| **SENTINEL.md** | Tech leads | Regras e protocolos |
| **[workspace/teste-e2e-sentinel-3-cenarios/](workspace/teste-e2e-sentinel-3-cenarios/)** | Arquitetos | 3 exemplos reais |
| **[docs/glossario.md](docs/glossario.md)** | Todos | Termos técnicos |

---

## 🆘 Precisa de Ajuda?

```
1. Leia RELATORIO_E2E_SENTINEL.md (exemplo completo)
2. Veja se um dos 3 cenários de teste se parece com seu caso
3. Se ainda ficar dúvida, descreva seu problema em linguagem natural:
   "Quero detectar SQL injection no meu código Java"
   Sentinel entende e roteia ao especialista correto.
```

---

**Pronto para começar?**

```
👉 Execute: python -m pytest .saes/agents/tests/test_git_commit_e2e_scenarios.py -v -s
👉 Leia:    workspace/teste-e2e-sentinel-3-cenarios/README.md
👉 Peça:    "Audita meu código [arquivo ou descrição]"
```

**SASS-X Sentinel v4.0** — Production-Ready ✅


