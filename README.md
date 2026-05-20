# GerenciaFunc

Sistema desktop de gerenciamento empresarial desenvolvido em Python com interface gráfica utilizando Tkinter.

O projeto tem como objetivo auxiliar no gerenciamento de funcionários, controle de presença e organização de tarefas dentro de uma empresa, centralizando informações importantes em uma única aplicação.

---

# Interface

O sistema possui interface gráfica moderna em tons de preto e laranja, incluindo:

* Login e cadastro
* Menu principal
* Gerenciamento de funcionários
* Controle de presença em calendário
* Sistema de tarefas
* Importação e exportação de dados

---

# Funcionalidades

## Autenticação

* Cadastro de usuários
* Login de usuários
* Validação de senha

---

## Funcionários

* Listar funcionários
* Adicionar funcionários
* Editar funcionários
* Remover funcionários
* Status ativo/inativo
* Exportar funcionários em JSON compactado (.zip)
* Importar funcionários via endereço web JSON

---

## Controle de Presença

* Calendário interativo
* Navegação entre meses
* Registro de presença por dia
* Horário de entrada e saída
* Descrição das atividades realizadas
* Visualização de múltiplos funcionários por dia

---

## Tarefas

* Criar tarefas
* Editar tarefas
* Remover tarefas
* Concluir tarefas
* Atribuir funcionário responsável
* Definir prazo
* Definir prioridade
* Filtrar tarefas

---

## Importação de Dados

* Importação de funcionários via JSON online a partir do repositório: https://github.com/b4rradas/empresa-JSON
* Uso da biblioteca `requests`
* Armazenamento automático no banco SQLite
* Atualização automática da interface

---

## Exportação de Dados

* Exportação em JSON
* Compactação automática em `.zip`
* Escolha do local de salvamento

---

# Tecnologias Utilizadas

* Python
* Tkinter
* SQLite
* Requests
* JSON
* ZipFile
* PyInstaller

---

# Estrutura do Projeto

```text
GerenciaFunc/
│
├── assets/
│   └── logo.ico
│
├── backend/
│   ├── auth.py
│   ├── funcionarios.py
│   ├── tarefas.py
│   ├── presenca.py
│   ├── importar_funcionarios.py
│   └── exportar_funcionarios.py
│
├── ui/
│   ├── login.py
│   ├── cadastro.py
│   ├── menu.py
│   ├── funcionarios_ui.py
│   ├── funcionario_form.py
│   ├── tarefas_ui.py
│   ├── tarefa_form.py
│   ├── presenca_ui.py
│   ├── presenca_form.py
│   ├── importar_funcionarios_ui.py
│   ├── sobre.py
│   └── theme.py
│
├── database.py
├── main.py
├── requirements.txt
└── README.md
```

---

# Como Executar

## 1. Instalar dependências

```bash
pip install -r requirements.txt
```

---

## 2. Executar aplicação

```bash
python main.py
```

---

# Gerar Executável

```bash
pyinstaller --onefile --windowed --icon=assets/logo.ico --name GerenciaFunc main.py
```

O executável será criado em:

```text
dist/
```
