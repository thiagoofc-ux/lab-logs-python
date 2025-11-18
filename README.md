# Log Analyzer — Python

Ferramenta de análise de logs de autenticação do Windows, criada para identificar atividades suspeitas como brute force, logins incomuns, acessos de usuários desabilitados e múltiplos IPs em janela curta.

---

##  Funcionalidades

-  Detecção de brute force  
-  Logins realizados na madrugada  
-  Tentativas de login por usuários desabilitados  
-  Acessos massivos por múltiplos IPs em poucos minutos  
-  Leitura automática de logs no formato texto  
-  Ignora linhas vazias automaticamente  

---

##  Estrutura do Projeto

```
log_analyzer.py
exemplo_logs.txt
README.md
```

---

##  Formato dos Logs

Cada linha deve seguir:

```
YYYY-MM-DD HH:MM:SS | USERNAME | IP | STATUS
```

Exemplo:

```
2025-01-10 14:22:51 | user1 | 192.168.0.10 | FAILED
```

---

##  exemplo_logs.txt (atualizado)

```
2025-01-10 01:45:10 | admin | 192.168.0.5 | SUCCESS
2025-01-10 14:22:51 | user1 | 192.168.0.10 | FAILED
2025-01-10 14:22:55 | user1 | 192.168.0.10 | FAILED
2025-01-10 14:23:01 | user1 | 192.168.0.10 | FAILED
2025-01-10 14:23:12 | user1 | 192.168.0.10 | FAILED
2025-01-10 14:23:44 | user1 | 192.168.0.10 | FAILED

2025-01-11 02:10:55 | user2 | 192.168.0.20 | SUCCESS

2025-01-11 08:00:40 | guest | 10.0.0.10 | SUCCESS
2025-01-11 08:30:20 | old_user | 10.0.0.20 | SUCCESS

2025-01-11 09:00:00 | user3 | 8.8.8.1 | SUCCESS
2025-01-11 09:00:30 | user3 | 8.8.4.4 | SUCCESS
2025-01-11 09:01:10 | user3 | 1.1.1.1 | SUCCESS
2025-01-11 09:01:50 | user3 | 1.0.0.1 | SUCCESS
2025-01-11 09:02:05 | user3 | 200.200.200.200 | SUCCESS
```

---

##  Como Executar

```bash
python log_analyzer.py
```

---

##  Exemplo de Saída

```
=== ALERTAS DETECTADOS ===
[BRUTE FORCE] Usuário user1 teve 5 falhas em 5 minutos.
[MADRUGADA] Login suspeito: admin às 2025-01-10 01:45:10
[MADRUGADA] Login suspeito: user2 às 2025-01-11 02:10:55
[DESABILITADO] Usuário desabilitado fez login: guest (2025-01-11 08:00:40)
[DESABILITADO] Usuário desabilitado fez login: old_user (2025-01-11 08:30:20)
[ACESSOS MASSIVOS] Usuário user3 acessou de 5 IPs diferentes em 3 minutos.
```

---

##  Como Funciona

- **Brute Force:** analisa falhas consecutivas dentro de uma janela de tempo  
- **Madrugada:** qualquer login antes das 05:00  
- **Usuários desabilitados:** lista configurável  
- **Massivo por IP:** identifica múltiplos IPs em pouco tempo para o mesmo usuário  

---



##  Licença

Uso livre para estudos e laboratórios de Segurança da Informação.

