# 🔒 Segurança

A segurança é um pilar fundamental do SASS-X Sentinel, com agentes dedicados a encontrar e ajudar a corrigir vulnerabilidades.

## Agentes de Segurança

| Especialista | Foco | Exemplo de Detecção |
|---|---|---|
| **OWASP** | Top 10 vulnerabilidades web | SQL Injection, Cross-Site Scripting (XSS), Cross-Site Request Forgery (CSRF). |
| **SecureCode** | Práticas de codificação insegura | Segredos "hard-coded", uso de algoritmos de criptografia fracos, configuração insegura. |
| **LGPD** | Conformidade com a Lei Geral de Proteção de Dados | Detecção de tratamento inadequado de dados pessoais. |

## Exemplo de Achado de Segurança

Um achado de segurança típico inclui a evidência clara (o trecho de código vulnerável), o impacto no negócio e uma proposta de correção com código seguro.

```java
// ❌ ANTES (vulnerável)
String query = "SELECT * FROM CLIENTES WHERE email='" + email + "'";

// ✅ DEPOIS (seguro)
String query = "SELECT * FROM CLIENTES WHERE email = ?";
PreparedStatement pstmt = connection.prepareStatement(query);
pstmt.setString(1, email);
```
