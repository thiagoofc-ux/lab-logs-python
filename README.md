# Log Analyzer — Projeto 3

Ferramenta simples de análise de logs desenvolvida em Python para detectar eventos suspeitos em registros de autenticação.

---

##  Funcionalidades

###  Detecção de Brute Force
- Conta falhas de login por usuário.
- Gera alerta quando o número de falhas ultrapassa o limite definido.

###  Logins de Madrugada
- Logins entre **00:00 e 05:00** são sinalizados como comportamento incomum.

###  Usuários Desabilitados
- Verifica tentativas de login realizadas por contas desativadas.

---

##  Estrutura do Projeto

```
log_analyzer.py   # Script principal de análise
exemplo_logs.txt  # Arquivo com logs de teste
README.md         # Documentação do projeto
```

---

## ▶ Como Executar

Certifique-se de ter Python instalado e execute o script:

```bash
python3 log_analyzer.py
```

Os alertas aparecerão diretamente no terminal.

---

##  Exemplo de Saída

```text
[ALERTA] Possível brute force detectado no usuário 'ana'. Falhas: 5
[ALERTA] Login de madrugada detectado. Usuário 'jose' às 2024-11-18 03:22:15
[ALERTA] Usuário desabilitado 'guest' tentou login (FAILED)
```

---

##  Personalizações

Dentro do arquivo **log_analyzer.py**, você pode ajustar:

- Lista de usuários desabilitados  
- Horário considerado madrugada  
- Limite para detecção de brute force  

---

##  Próximos Passos (Sugestões)

- Enviar alertas por e-mail via SMTP.
- Criar dashboard em Flask.
- Integrar com Splunk, Elastic ou SIEMs.
- Criar coleta automática de logs do Windows via WMI ou WinEvent API.

---

##  Licença

Este projeto é open-source e pode ser utilizado para estudos, treinamentos e laboratórios de segurança.

