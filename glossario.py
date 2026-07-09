"""
SASS-X Sentinel — Glossário de Termos

Referência rápida de conceitos usados no sistema.
"""

GLOSSARIO = {
    "Achado": {
        "resumo": "Descoberta estruturada de um problema no código",
        "detalhe": "Contém: ID, título, severidade, arquivo:linha, evidência (trecho real), impacto, correção proposta (before→after), confiança e esforço estimado. Obedece ao Contrato Único de Achados.",
        "exemplo": "OWASP-001: SQL Injection em ClienteRepository.java:47"
    },
    "Severidade": {
        "resumo": "Nível de urgência de um achado",
        "detalhe": "CRÍTICO (falha imediata), ALTO (sprint atual), MÉDIO (backlog normal), BAIXO/INFO (nice-to-have)",
        "exemplo": "CRÍTICO = sem circuit breaker → cascata de falhas"
    },
    "Contrato Único": {
        "resumo": "Formato padrão que TODOS os agentes usam para reportar achados",
        "detalhe": "JSON com campos obrigatórios (id, titulo, severidade, arquivo, linha, evidencia, impacto, correcao, confianca, esforco). Garante consolidação automática.",
        "exemplo": "{ 'id': 'OWASP-001', 'severidade': 'CRITICO', ... }"
    },
    "Evidência": {
        "resumo": "Prova concreta de um achado (código real ou trace)",
        "detalhe": "Sem evidência não há achado. Deve incluir arquivo:linha e trecho exato.",
        "exemplo": "arquivo: ClienteRepository.java | linha: 47 | trecho: String query = 'SELECT...' + email"
    },
    "6 Camadas": {
        "resumo": "Arquitetura em paralelo do Sentinel",
        "detalhe": "L1: Orquestrador | L2: Token Budget | L3: Knowledge Graph | L4: Agentes (paralelo) | L5: Consolidação | L6: Human Approval",
        "exemplo": "Um commit dispara L1→L4 (paralelo)→L5→L6"
    },
    "Agente": {
        "resumo": "Especialista que detecta um tipo de problema",
        "detalhe": "Ex: OWASP (segurança), BugHunter (bugs), CleanCode (qualidade), Performance (gargalos)",
        "exemplo": "BugHunter detecta null pointer | OWASP detecta SQL injection"
    },
    "Orquestrador": {
        "resumo": "Componente que coordena os agentes",
        "detalhe": "Entende a demanda, dispara agentes relevantes em paralelo (L4) e consolida os achados",
        "exemplo": "Você: 'Audita meu código' → Orquestrador dispara OWASP + Quality + Observability em paralelo"
    },
    "Read-Only": {
        "resumo": "Análise sem alterar código (maioria dos agentes)",
        "detalhe": "Agentes read-only só detectam e propõem. Código só é alterado com aprovação humana.",
        "exemplo": "BugHunter detecta bug → você aprova → refactoring-agent implementa"
    },
    "Consolidação": {
        "resumo": "Juntar achados de múltiplos agentes e remover duplicatas",
        "detalhe": "L5: dedup por (arquivo, linha, categoria), priorização por severity",
        "exemplo": "OWASP e BugHunter ambos encontram SQL injection → consolida como 1 achado"
    },
    "Reprocessamento": {
        "resumo": "Refazer análise se houver pendências",
        "detalhe": "Máximo 3 ciclos. Se agente falhar ou confiança baixa, re-dispara só o pendente.",
        "exemplo": "Ciclo 1: alguns agentes falharam → Ciclo 2: retry → Ciclo 3: consolidação final"
    },
    "Relatório": {
        "resumo": "Documento final carimbado com todos os achados",
        "detalhe": "Gravado em workspace/ISSUE<N>/relatorio/ com timestamp. Contém achados, plano por sprint, soluções.",
        "exemplo": "2026-06-09_1432_auditoria_modulo-cobranca.md"
    },
    "Diário": {
        "resumo": "Trilha de auditoria + checkpoints por etapa",
        "detalhe": "Permite retomar análise interrompida sem refazer tudo. Registra cada nível + decisões.",
        "exemplo": "ISSUE123-2026-06-09_1432.md (Nível 0 → Nível 1 → ... → Nível 4)"
    },
    "Pausa & Retomada": {
        "resumo": "Parar análise e voltar depois do mesmo ponto",
        "detalhe": "Gatilho /retomar + caminho do diário = continua sem perder estado",
        "exemplo": "/retomar workspace/ISSUE123/relatorio/ISSUE123-2026-06-09_1432.md"
    }
}

if __name__ == "__main__":
    print("📚 SASS-X Sentinel — Glossário de Termos")
    print("=" * 60)
    for termo, info in GLOSSARIO.items():
        print(f"\n📌 {termo}")
        print(f"   Resumo: {info['resumo']}")
        print(f"   Detalhe: {info['detalhe']}")
        print(f"   Exemplo: {info['exemplo']}")
