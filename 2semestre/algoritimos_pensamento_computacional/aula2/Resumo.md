---
tipo: resumo
disciplina: Algoritmos e Pensamento Computacional
aula: 2
material: Slides - Algoritmos.pdf
slides: 1-225
tags:
  - algoritmos
  - logica-de-programacao
  - pseudocodigo
---

# Resumo — Algoritmos e Pensamento Computacional

> Resumo das 57 páginas do arquivo **Slides - Algoritmos.pdf**, que reúne 225 slides. O material apresenta os fundamentos da computação e avança até estruturas de dados, modularização e passagem de parâmetros.

## 1. Fundamentos da computação

Um computador é um equipamento eletrônico capaz de receber dados, processá-los lógica e aritmeticamente, armazená-los e produzir resultados. Sua organização básica inclui:

- **CPU**, formada pela unidade de controle, unidade lógica e aritmética e registradores;
- **memória principal**, como RAM e ROM;
- **memória secundária**, usada para armazenamento persistente;
- **dispositivos de entrada e saída**, responsáveis pela comunicação com o usuário e outros sistemas.

### Unidades de medida

- **Bit (b):** menor unidade de informação, representada por `0` ou `1`.
- **Byte (B):** conjunto de 8 bits, capaz de representar 256 combinações.
- As unidades seguintes crescem em potências de 2: KB, MB, GB, TB, PB, EB, ZB e YB.

A tabela **ASCII** padroniza a associação entre números e caracteres. O padrão original usa os códigos de 0 a 127; extensões posteriores aproveitaram os códigos seguintes para representar outros símbolos.

## 2. Programação, lógica e algoritmos

Programar é estabelecer uma comunicação controlada entre o ser humano e o computador por meio de uma linguagem compreensível pela máquina. A **lógica de programação** organiza e encadeia pensamentos e instruções para alcançar um objetivo.

Um **algoritmo** é uma sequência finita, ordenada e não ambígua de instruções para resolver um problema. Ele pode ser comparado a uma receita: recebe informações, executa passos e produz um resultado.

### Propriedades de um algoritmo

- **Finitude:** precisa terminar após uma quantidade finita de etapas.
- **Definição:** cada instrução deve ser precisa e sem ambiguidades.
- **Entrada:** pode receber valores antes ou durante a execução.
- **Saída:** deve produzir resultados relacionados às entradas.
- **Eficácia:** cada operação deve ser simples e executável em tempo finito.

O algoritmo de Euclides, usado para calcular o máximo divisor comum, é apresentado como um exemplo histórico: divisões sucessivas substituem os valores pelo divisor e pelo resto até que o resto seja zero.

## 3. Entrada, processamento e saída

Todo programa pode ser compreendido pelo modelo:

1. **Entrada:** dados fornecidos ao algoritmo.
2. **Processamento:** operações realizadas sobre esses dados.
3. **Saída:** informações resultantes do processamento.

Para resolver um problema, deve-se:

1. compreender o enunciado;
2. identificar as entradas;
3. identificar as saídas esperadas;
4. determinar como transformar as entradas em saídas;
5. construir o algoritmo;
6. testá-lo em diferentes situações.

Os slides aplicam esse método a exemplos como cálculo do preço de flores, médias ponderadas, estoque médio, reajuste salarial e conta de água. Um **teste de mesa** simula manualmente a execução do algoritmo com valores conhecidos para validar a lógica antes da implementação.

## 4. Formas de representar algoritmos

### Descrição narrativa

Explica os passos com linguagem cotidiana. É fácil de escrever, mas pode gerar ambiguidades.

### Fluxograma

Representa graficamente o fluxo do algoritmo. Os principais símbolos são:

- **terminal:** início ou fim;
- **entrada manual:** leitura de dados;
- **processamento:** cálculos e atribuições;
- **exibição:** saída de dados;
- **decisão:** escolha de caminhos a partir de uma condição;
- **processo predefinido:** chamada de uma sub-rotina;
- **conector:** continuação do fluxo em outro ponto;
- **preparação:** inicialização ou modificação de controles;
- **seta:** direção do fluxo.

### Pseudocódigo ou Portugol

É uma linguagem de projeto que descreve o algoritmo de forma textual, sem depender de uma linguagem de programação real. O material utiliza o padrão do **VisuAlg**, com comandos como `algoritmo`, `var`, `inicio`, `leia`, `escreva` e `fimalgoritmo`.

```text
algoritmo "SOMA_NUMEROS"
var
   A, B, X: inteiro
inicio
   leia(A)
   leia(B)
   X <- A + B
   escreva(X)
fimalgoritmo
```

O processo recomendado é: **entendimento → diagramação → codificação → teste**.

## 5. Tipos de dados, variáveis e constantes

### Tipos básicos

- **Inteiro:** números sem parte fracionária.
- **Real:** números que podem possuir parte fracionária.
- **Caractere:** um único símbolo.
- **Cadeia:** sequência de caracteres.
- **Lógico ou booleano:** apenas dois estados, como verdadeiro/falso.

Uma **variável** é uma posição identificada na memória cujo valor pode mudar. Ela armazena um valor por vez e precisa ter nome e tipo definidos. Nomes não devem conter espaços, começar com números nem coincidir com palavras reservadas.

Uma **constante** mantém o mesmo valor durante a execução. A atribuição costuma usar `=` para constantes e `<-` ou `:=` para variáveis.

## 6. Operadores e expressões

Os operadores aritméticos apresentados são exponenciação, raiz, multiplicação, divisão, adição e subtração. A precedência matemática deve ser respeitada, e os parênteses alteram a ordem de avaliação.

Fórmulas matemáticas precisam ser convertidas para uma expressão computacional linear. Por exemplo:

```text
area_triangulo <- (base * altura) / 2
```

Dois operadores importantes para números inteiros são:

- **DIV:** retorna o quociente inteiro da divisão. Exemplo: `7 DIV 2 = 3`.
- **MOD:** retorna o resto da divisão. Exemplo: `7 MOD 2 = 1`.

## 7. Estruturas sequenciais

Em uma estrutura sequencial, as instruções são executadas de cima para baixo, uma após a outra, sem desvios ou repetições. Mesmo em problemas simples, é importante identificar entradas, tipos, cálculos, saídas e casos de teste antes de escrever o código.

Os exercícios propõem leitura e exibição de dados, área da circunferência, salário líquido, conversão de moeda, soma de quadrados, comissão de vendas, estoque médio e reajustes percentuais.

## 8. Estruturas condicionais

Uma condição é uma expressão lógica cujo resultado é verdadeiro ou falso. Operadores relacionais, como `=`, `<>`, `>`, `<`, `>=` e `<=`, permitem comparar valores.

### Decisão simples

Executa um bloco somente quando a condição é verdadeira:

```text
se condicao entao
   instrucoes
fimse
```

### Decisão composta

Escolhe entre dois caminhos:

```text
se condicao entao
   instrucoes_se_verdadeiro
senao
   instrucoes_se_falso
fimse
```

### Decisões sequenciais e encadeadas

- **Sequenciais:** várias decisões independentes são executadas sucessivamente.
- **Encadeadas:** uma decisão fica dentro de outra e só é avaliada quando o fluxo externo permite.

Os exemplos verificam soma maior que 10, números positivos ou negativos, valores maiores que 100, peso ideal conforme sexo e paridade de números.

## 9. Operadores lógicos

Os operadores lógicos combinam ou invertem condições:

| Operador | Resultado |
| --- | --- |
| `NAO` | Inverte verdadeiro e falso. |
| `E` | Verdadeiro somente quando todas as condições são verdadeiras. |
| `OU` | Verdadeiro quando ao menos uma condição é verdadeira. |
| `XOU` | Verdadeiro quando exatamente uma condição é verdadeira. |

A ordem de precedência apresentada é: `NAO`, `E`, `OU` e `XOU`.

## 10. Decisão de múltipla escolha

Quando uma expressão pode assumir valores mutuamente exclusivos, usa-se `escolha/caso`, evitando uma sequência extensa de condições:

```text
escolha opcao
caso 1
   comandos
caso 2
   comandos
outrocaso
   comandos_padrao
fimescolha
```

O exemplo escolhe entre praia, cinema e churrasco; a atividade aplica a estrutura para classificar capitais brasileiras por região.

## 11. Estruturas de repetição

Laços repetem um bloco um número conhecido ou desconhecido de vezes.

### `ENQUANTO` — pré-teste

A condição é verificada antes da execução. O bloco pode não ser executado nenhuma vez e continua enquanto a condição for verdadeira.

```text
enquanto condicao faca
   instrucoes
fimenquanto
```

O exemplo gera a tabuada de um número usando um contador de 1 a 10.

### `REPITA...ATE` — pós-teste

O bloco é executado pelo menos uma vez e repetido até que a condição se torne verdadeira.

```text
repita
   instrucoes
ate condicao
```

O exemplo testa se números são pares ou ímpares até que o usuário digite zero. O material alerta que o `do...while` da linguagem C possui lógica de continuidade diferente: ele repete enquanto a condição é verdadeira.

### `PARA` — repetição com contagem

É usado quando a quantidade de repetições é conhecida:

```text
para contador de inicio ate fim passo incremento faca
   instrucoes
fimpara
```

O exemplo lê uma quantidade definida de notas, acumula a soma e calcula a média.

## 12. Estruturas homogêneas: vetores

Uma variável comum guarda apenas um valor. Um **vetor** reúne vários valores do mesmo tipo sob um único nome e usa um índice inteiro para identificar cada posição.

```text
medias: vetor[1..20] de real
```

Para acessar um elemento, são necessários o nome do vetor e seu índice, como `medias[5]`. O índice pode ser uma constante, uma variável ou uma expressão que resulte em inteiro positivo. Laços são usados para percorrer, preencher e processar vetores.

Vetores relacionados podem compartilhar o mesmo índice. Por exemplo, três vetores podem armazenar a primeira nota, a segunda nota e a média de cada aluno.

## 13. Estruturas homogêneas: matrizes

Uma **matriz** também contém dados de um único tipo, mas possui duas ou mais dimensões. Uma matriz bidimensional pode ser entendida como uma tabela de linhas e colunas:

```text
notas: vetor[1..20, 1..3] de real
```

Nesse exemplo, cada linha representa um aluno e cada coluna representa uma nota ou média. O acesso exige um índice para cada dimensão. Matrizes normalmente são percorridas com laços aninhados: um para as linhas e outro para as colunas.

Quando os dados possuem tipos diferentes, pode-se combinar estruturas: um vetor de nomes, do tipo cadeia, e uma matriz de notas, do tipo real.

## 14. Modularização

Modularizar é dividir um problema grande em módulos menores, também chamados de subalgoritmos ou sub-rotinas. Isso melhora organização, legibilidade, manutenção e reutilização.

- **Procedimento:** executa uma tarefa e pode receber parâmetros, mas não precisa retornar um valor.
- **Função:** pode receber parâmetros e retorna um único valor ao algoritmo chamador.

### Escopo de variáveis

- **Global:** declarada no programa principal e acessível pelas partes do programa que estejam dentro de seu escopo.
- **Local:** declarada dentro de uma sub-rotina e acessível somente nela.

Variáveis locais podem ter o mesmo nome de variáveis de outros escopos, mas representam posições diferentes na memória. Deve-se observar o local da declaração para saber qual variável está sendo usada.

## 15. Passagem de parâmetros

A comunicação entre o programa principal e as sub-rotinas acontece por parâmetros:

- **Por valor:** a sub-rotina recebe uma cópia. Alterações internas não modificam a variável original; é um parâmetro de entrada.
- **Por referência:** a sub-rotina recebe uma referência ao endereço da variável. Alterações internas modificam a variável original; é um parâmetro de entrada e saída.

No pseudocódigo apresentado, a palavra `VAR` antes do parâmetro indica passagem por referência.

## 16. Estruturas heterogêneas: registros

Um **registro** reúne campos relacionados que podem possuir tipos diferentes. Ele representa um objeto, como um aluno, com nome, turma, sala e notas. Em C, o conceito corresponde a uma `struct`; o material informa que o VisuAlg não implementa registros heterogêneos.

```text
tipo cadastro_aluno = registro
   nome: cadeia
   turma: caractere
   sala: inteiro
   notas: vetor[1..4] de real
fim_registro
```

É possível combinar registros com vetores e matrizes, criando, por exemplo, um vetor de 50 alunos, cada um com seus próprios campos e um vetor de notas. Tipos derivados definidos pelo programador ajudam a reutilizar essas estruturas.

O exercício final propõe uma tabela de cargos e salários: o usuário informa um código de 1 a 7, o programa encontra o registro correspondente e exibe cargo e salário, ou informa que o código é inválido.

## 17. Síntese para revisão

- Um algoritmo deve ser finito, preciso, eficaz e produzir saídas coerentes com suas entradas.
- Antes de programar, entenda o problema e separe entrada, processamento e saída.
- Fluxogramas mostram o fluxo visualmente; pseudocódigo descreve a solução textualmente.
- Variáveis mudam; constantes permanecem fixas; ambas devem ter tipos adequados.
- Estruturas sequenciais executam instruções em ordem.
- Condicionais selecionam caminhos a partir de expressões booleanas.
- Laços repetem instruções: `ENQUANTO`, `REPITA...ATE` e `PARA` atendem situações diferentes.
- Vetores possuem uma dimensão; matrizes possuem múltiplas dimensões; ambos armazenam dados homogêneos.
- Registros agrupam dados heterogêneos relacionados.
- Funções, procedimentos e parâmetros permitem dividir o programa em partes menores e reutilizáveis.

## Atividades apresentadas no material

Os slides propõem exercícios de descrição lógica, fluxogramas, teste de mesa, cálculos matemáticos, médias, salários, comissões, decisões, operadores lógicos, múltipla escolha, tabuadas, paridade, vetores, matrizes, modularização e registros. Também apresentam o teste lógico das cinco casas, conhecido como “Teste de Einstein”, para praticar análise de restrições.

## Referências indicadas nos slides

O material recomenda principalmente obras de Joyanes Aguilar, Edelweiss e Castro, Soffner, Ascencio e Campos, Cormen, Forbellone, Goodrich e Tamassia, Manzano e Oliveira, Piva Junior, Puga e Rissetti, entre outros autores de algoritmos, lógica de programação e estruturas de dados.
