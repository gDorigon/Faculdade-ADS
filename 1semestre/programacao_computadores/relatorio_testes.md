# RELATÓRIO DE TESTES DE MESA
## Sistema de Faturamento e Assinaturas de Clientes

**Disciplina:** Programação de Computadores  
**Professor:** Me. João Víctor Ramos  
**Entrega:** Projeto Final – Entrega 4  

---

**Integrantes:**

| Nome Completo | RA |
|---|---|
| ______________________________ | _________ |
| ______________________________ | _________ |
| ______________________________ | _________ |

---

## 1. Descrição do Sistema

Sistema desenvolvido em Python puro para gerenciamento de assinaturas de clientes.  
Permite cadastrar, pesquisar, listar e atualizar planos com vigência em meses e valores mensais.  
Utiliza um dicionário principal como banco de dados em memória.

---

## 2. Mapeamento Técnico dos Blocos de Exceção

| Bloco / Função | Risco Tratado | Tipo de Exceção |
|---|---|---|
| `ler_inteiro()` | Usuário digita letras ou Enter vazio em campo numérico inteiro | `ValueError` |
| `ler_float()` | Usuário digita letras em campo de valor decimal | `ValueError` |
| `validar_id()` | ID informado é zero ou negativo | `ValueError` (raise manual) |
| `validar_vigencia()` | Meses fora do intervalo 1–60 | `ValueError` (raise manual) |
| `validar_valor()` | Valor do plano igual a zero ou negativo | `ValueError` (raise manual) |
| `cadastrar_cliente()` | ID já existente no banco | `KeyError` |
| `pesquisar_cliente()` | ID não encontrado no banco | `KeyError` |
| `atualizar_assinatura()` | ID não encontrado ao tentar atualizar | `KeyError` |
| `listar_clientes()` | Banco vazio, nada para listar | `ValueError` |
| Menu principal | Opção digitada não é número | `ValueError` |

---

## 3. Tabela de Testes de Mesa

### 3.1 – Cadastro de Cliente

| # | Cenário de Teste | O Que o Usuário Digitou | Resultado Esperado | Resultado Obtido | Passou? |
|---|---|---|---|---|---|
| T01 | ID com letra | `abc` no campo ID | Mensagem de erro, laço repete | `[ERRO] Digite apenas números inteiros!` | ✅ |
| T02 | ID negativo | `-5` no campo ID | Erro de regra de negócio, não cadastra | `[ERRO] ID deve ser um número positivo maior que zero!` | ✅ |
| T03 | ID zero | `0` no campo ID | Erro de regra de negócio, não cadastra | `[ERRO] ID deve ser um número positivo maior que zero!` | ✅ |
| T04 | Vigência inválida (0 meses) | `0` em vigência | Erro, não cadastra | `[ERRO] Vigência deve ser entre 1 e 60 meses!` | ✅ |
| T05 | Vigência inválida (61 meses) | `61` em vigência | Erro, não cadastra | `[ERRO] Vigência deve ser entre 1 e 60 meses!` | ✅ |
| T06 | Valor zero | `0` no valor do plano | Erro, não cadastra | `[ERRO] Valor do plano deve ser maior que zero!` | ✅ |
| T07 | Valor negativo | `-10` no valor | Erro, não cadastra | `[ERRO] Valor do plano deve ser maior que zero!` | ✅ |
| T08 | ID duplicado | `1` (já cadastrado) | Erro, não sobrescreve | `[ERRO] Já existe um cliente com esse ID!` | ✅ |
| T09 | Nome vazio | Enter sem digitar | Mensagem de erro, laço repete | `[ERRO] Campo não pode ficar vazio!` | ✅ |
| T10 | Cadastro válido completo | ID=1, Nome=João, Plano=BASICO, 12 meses | Cadastra com sucesso | `Cliente #1 cadastrado com sucesso!` | ✅ |

---

### 3.2 – Pesquisa de Cliente

| # | Cenário de Teste | O Que o Usuário Digitou | Resultado Esperado | Resultado Obtido | Passou? |
|---|---|---|---|---|---|
| T11 | ID com letra | `x` no campo ID | Erro, laço repete | `[ERRO] Digite apenas números inteiros!` | ✅ |
| T12 | ID não cadastrado | `999` | Erro, informa não encontrado | `[ERRO] Cliente #999 não encontrado!` | ✅ |
| T13 | ID válido e cadastrado | `1` | Exibe a ficha completa do cliente | Ficha exibida corretamente | ✅ |

---

### 3.3 – Listagem

| # | Cenário de Teste | O Que o Usuário Digitou | Resultado Esperado | Resultado Obtido | Passou? |
|---|---|---|---|---|---|
| T14 | Listar com banco vazio | Opção 3 sem nenhum cadastro | Aviso de banco vazio | `[AVISO] Nenhum cliente cadastrado ainda!` | ✅ |
| T15 | Listar com clientes cadastrados | Opção 3 com dados existentes | Tabela com todos os clientes | Tabela exibida corretamente | ✅ |

---

### 3.4 – Atualização de Assinatura

| # | Cenário de Teste | O Que o Usuário Digitou | Resultado Esperado | Resultado Obtido | Passou? |
|---|---|---|---|---|---|
| T16 | Atualizar ID inexistente | `999` | Erro, informa não encontrado | `[ERRO] Cliente #999 não existe no sistema!` | ✅ |
| T17 | Atualizar com vigência 0 | `0` em meses | Erro de validação | `[ERRO] Vigência deve ser entre 1 e 60 meses!` | ✅ |
| T18 | Atualização válida | ID=1, PREMIUM, 6 meses | Dados atualizados com sucesso | `Assinatura do cliente #1 atualizada com sucesso!` | ✅ |

---

### 3.5 – Menu Principal

| # | Cenário de Teste | O Que o Usuário Digitou | Resultado Esperado | Resultado Obtido | Passou? |
|---|---|---|---|---|---|
| T19 | Opção com letra | `a` no menu | Erro, laço repete | `[ERRO] Digite apenas um número!` | ✅ |
| T20 | Opção fora do range | `9` | Informa opção inválida, repete | `[ERRO] Opção inválida. Escolha entre 0 e 4.` | ✅ |
| T21 | Enter vazio no menu | (Enter) | Erro, laço repete | `[ERRO] Digite apenas um número!` | ✅ |
| T22 | Sair do sistema | `0` | Encerra o programa | `Sistema encerrado. Até logo!` | ✅ |

---

## 4. Regras de Negócio com `raise` Manual

O sistema implementa **3 disparos manuais de exceção** conforme exigido:

```
1. validar_id(id_cliente)     → raise ValueError se id <= 0
2. validar_vigencia(meses)    → raise ValueError se meses < 1 ou meses > 60
3. validar_valor(valor)       → raise ValueError se valor <= 0
```

---

## 5. Uso do Ciclo Completo try/except/else/finally

Todas as 4 funções críticas utilizam o ciclo completo:

- **`try`**: contém apenas a linha de risco (validação ou acesso ao dicionário)
- **`except ValueError`**: captura erros de tipo e de regra de negócio
- **`except KeyError`**: captura chaves inexistentes no dicionário
- **`else`**: executa a ação principal somente se não houve erro
- **`finally`**: sempre registra o log de auditoria, independente do resultado

---

## 6. Conclusão

O sistema passou em todos os 22 cenários de teste previstos.  
Nenhuma entrada inválida causou encerramento inesperado do programa.  
Todos os blocos `try/except/else/finally` e disparos `raise` funcionaram conforme esperado.
