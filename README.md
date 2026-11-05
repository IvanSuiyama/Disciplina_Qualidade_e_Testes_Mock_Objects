# Mock Objects

**Disciplina:** Qualidade e Testes
**Tema:** Dublês de Teste (Mock Objects)
**Base:** projeto `custom-stack.zip` disponibilizado na semana de aula

---

## Sobre este repositório

Este repositório contém a solução do desafio de Mock Objects. O projeto original veio do
`custom-stack.zip` e foi mantido **na estrutura em que foi extraído**. Por isso
existe a pasta duplicada `custom-stack/custom-stack`: a primeira é apenas o
diretório criado pelo zip; a segunda é o projeto de fato.

A raiz do repositório Git é esta pasta. O enunciado (`exercicio.txt`) e os
links de referência (`link.txt`) ficam apenas localmente e não são versionados.

---

## Estrutura

```
.
├── README.md                  ← este arquivo
├── exercicio.txt              ← enunciado original
├── link.txt                   ← links de referência
├── .gitignore
└── custom-stack/
    ├── __MACOSX/              ← lixo gerado pelo zip (ignorado pelo Git)
    └── custom-stack/          ← PROJETO DO EXERCÍCIO
        ├── README.md
        ├── requirements.txt
        ├── src/
        │   ├── __init__.py
        │   ├── custom_stack_class.py
        │   └── number_asc_order.py
        ├── test/
        │   ├── __init__.py
        │   ├── custom_stack_test.py
        │   └── number_asc_order_test.py
        └── .vscode/
            └── settings.json
```

O código do exercício fica em:

```
custom-stack/custom-stack
```

---

## O que já existia (material original do zip)

| Item | Situação original |
|---|---|
| `src/custom_stack_class.py` | Classe `CustomStack` com o bug `self.size == self.limit` |
| `test/custom_stack_test.py` | Apenas **1 teste** (push de um elemento) |
| `requirements.txt` | pytest, pytest-cov, pytest-mock e dependências |
| `README.md` | Instruções de instalação e execução |
| `.vscode/settings.json` | Configuração do pytest no VS Code |
| `.coverage`, `.pytest_cache/` | Artefatos de execuções anteriores |

Com apenas esse teste, a cobertura era de **79%** e o bug passava despercebido:
como `self.size` (o método) era comparado com `self.limit`, a condição nunca era
verdadeira e `StackFullException` nunca era lançada.

---

## O que foi implementado

### Parte 1 — Testes da `CustomStack`

- Corrigido o bug em `push`: `self.size` → `self.size()`.
  Nenhum método novo foi criado na classe.
- `test/custom_stack_test.py` reescrito com **9 testes**, cobrindo:
  - construtor (`limit`, `elements`, tamanho inicial);
  - `size()`;
  - `is_empty()` com pilha vazia e com elemento;
  - `push()` dentro do limite, no limite e acima do limite;
  - `push()` em pilha com limite zero;
  - `pop()` (comportamento LIFO) e `pop()` em pilha vazia;
  - `top()` sem remover o elemento e `top()` em pilha vazia;
  - lançamento de `StackFullException` e `StackEmptyException`.

### Parte 2 — `NumberAscOrder`

Criada a classe em `src/number_asc_order.py`:

```python
class NumberAscOrder:
    def sort(self, stack):
        ...
```

O método `sort(stack)`:

- recebe uma `CustomStack`;
- valida `None` (`ValueError`) e objetos que não são pilhas (`TypeError`);
- coleta os números com `pop()` enquanto a pilha não estiver vazia;
- retorna um `list` ordenado de forma ascendente;
- para pilha vazia, retorna `[]`.

Nenhum método adicional foi adicionado às classes já existentes.

### Testes da Parte 2

`test/number_asc_order_test.py` contém **6 testes**:

1. Pilha de 6 posições com 6 números sorteados — os sorteios são controlados
   com `mocker.patch("random.randint", side_effect=[...])`.
2. Pilha de 6 posições vazia → retorna `[]`.
3. Teste com `mocker.MagicMock(spec=CustomStack)` verificando as interações
   (`is_empty` e `pop`) — exemplo de **mock** observando comportamento.
4. Ordenação mantendo números duplicados.
5. `sort(None)` → `ValueError`.
6. `sort()` com objeto inválido → `TypeError`.

---

## Resultado dos testes

```
15 passed

Name                        Stmts   Miss  Cover
-------------------------------------------------
src/__init__.py                 0      0   100%
src/custom_stack_class.py      24      0   100%
src/number_asc_order.py        11      0   100%
-------------------------------------------------
TOTAL                          35      0   100%
```

- **15 testes**
- **100% de cobertura** em `src/`

---

## Como executar

### 1. Criar e ativar a venv

Na pasta do projeto:

```bash
cd custom-stack/custom-stack
python3 -m venv venv
source venv/bin/activate
```

### 2. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 3. Rodar os testes com cobertura

```bash
python -m pytest --cov=src --cov-report=term-missing
```

Saída esperada: **15 passed** e **100%** de cobertura em `src/`.

---

## Sobre o uso de mocks

Os links de referência do exercício foram usados como base:

- **pytest-mock** (`mocker`): criação de mocks, `side_effect` e verificação de
  chamadas;
- **múltiplos retornos com `side_effect`**: usado para simular os 6 sorteios da
  Mega Sena de forma determinística;
- **mock de `random.randint`**: evita depender do sorteio real e torna o teste
  reproduzível;
- **taxonomia de dublês** (Dummy, Stub, Mock, Fake, Spy): o teste com
  `MagicMock(spec=CustomStack)` observa interações, caracterizando um **Mock**;
  o `side_effect` com valores fixos caracteriza um **Stub**.

---

## Git

O `.gitignore` foi configurado para versionar somente o exercício. Ficam fora
do repositório:

- `venv/`
- `__pycache__/`
- `.pytest_cache/`
- `.coverage` e `htmlcov/`
- `.vscode/`
- `__MACOSX/` e arquivos `.zip`
- `foto.png` (material auxiliar)
- `exercicio.txt` (enunciado, mantido apenas localmente)
- `link.txt` (links de referência, mantidos apenas localmente)

Arquivos versionados:

```
.gitignore
README.md
custom-stack/custom-stack/README.md
custom-stack/custom-stack/requirements.txt
custom-stack/custom-stack/src/__init__.py
custom-stack/custom-stack/src/custom_stack_class.py
custom-stack/custom-stack/src/number_asc_order.py
custom-stack/custom-stack/test/__init__.py
custom-stack/custom-stack/test/custom_stack_test.py
custom-stack/custom-stack/test/number_asc_order_test.py
```

---

## Entrega

Exercício individual — repositório Git com a implementação.
