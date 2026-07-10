# 🤖 Sistema Multi-Agentes

O coração do Sentinel é seu sistema de múltiplos agentes especializados. Cada agente é um especialista focado em detectar um tipo específico de problema, trabalhando em paralelo para uma análise rápida e abrangente.

## O que é um Agente?

Um agente é um especialista que detecta um tipo de problema. Por exemplo, o agente `OWASP` foca em vulnerabilidades de segurança, enquanto o `CleanCode` busca por "code smells".

## Especialistas Disponíveis

| Especialista | Detecta | Exemplo |
|---|---|---|
| **BugHunter** | Bugs reais | Null pointer, lógica errada |
| **OWASP** | Vulnerabilidades web | SQL Injection, XSS, CSRF |
| **SecureCode** | Práticas inseguras | Hard-coded secrets, crypto fraca |
| **Performance** | Gargalos | N+1, loops desnecessários |
| **CleanCode** | Code smell | Métodos gigantes, duplicação |
| **SOLID** | Design patterns | Violações SRP, OCP, DIP |
| **Observability** | Logging/Tracing | Eventos silenciosos, contexto perdido |
| **RootCause** | Raiz de crashes | Stack trace → diagnóstico |
