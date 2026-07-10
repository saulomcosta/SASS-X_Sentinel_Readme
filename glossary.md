# 📚 Glossário de Termos

Referência rápida de conceitos usados no sistema SASS-X Sentinel.

---

### Achado
**Resumo:** Descoberta estruturada de um problema no código.
**Detalhe:** Contém: ID, título, severidade, arquivo:linha, evidência (trecho real), impacto, correção proposta (before→after), confiança e esforço estimado. Obedece ao Contrato Único de Achados.

---

### Agente
**Resumo:** Especialista que detecta um tipo de problema.
**Detalhe:** Ex: OWASP (segurança), BugHunter (bugs), CleanCode (qualidade), Performance (gargalos).

---

### 6 Camadas
**Resumo:** Arquitetura em paralelo do Sentinel.
**Detalhe:** L1: Orquestrador | L2: Token Budget | L3: Knowledge Graph | L4: Agentes (paralelo) | L5: Consolidação | L6: Human Approval.

---

### Consolidação
**Resumo:** Juntar achados de múltiplos agentes e remover duplicatas.
**Detalhe:** L5: dedup por (arquivo, linha, categoria), priorização por severity.

---

### Contrato Único
**Resumo:** Formato padrão que TODOS os agentes usam para reportar achados.
**Detalhe:** JSON com campos obrigatórios (id, titulo, severidade, etc). Garante consolidação automática.

---

### Diário
**Resumo:** Trilha de auditoria + checkpoints por etapa.
**Detalhe:** Permite retomar análise interrompida sem refazer tudo. Registra cada nível + decisões.

---

### Evidência
**Resumo:** Prova concreta de um achado (código real ou trace).
**Detalhe:** Sem evidência não há achado. Deve incluir arquivo:linha e trecho exato.

---

### Orquestrador
**Resumo:** Componente que coordena os agentes.
**Detalhe:** Entende a demanda, dispara agentes relevantes em paralelo (L4) e consolida os achados.

---

### Pausa & Retomada
**Resumo:** Parar análise e voltar depois do mesmo ponto.
**Detalhe:** Gatilho `/retomar` + caminho do diário = continua sem perder estado.

---

### Read-Only
**Resumo:** Análise sem alterar código (maioria dos agentes).
**Detalhe:** Agentes read-only só detectam e propõem. Código só é alterado com aprovação humana.

---

### Relatório
**Resumo:** Documento final carimbado com todos os achados.
**Detalhe:** Gravado em `workspace/ISSUE<N>/relatorio/` com timestamp. Contém achados, plano por sprint, soluções.

---

### Reprocessamento
**Resumo:** Refazer análise se houver pendências.
**Detalhe:** Máximo 3 ciclos. Se agente falhar ou confiança baixa, re-dispara só o pendente.

---

### Severidade
**Resumo:** Nível de urgência de um achado.
**Detalhe:** CRÍTICO (falha imediata), ALTO (sprint atual), MÉDIO (backlog normal), BAIXO/INFO (nice-to-have).
