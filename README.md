# Arquitetura Multiagentes para Operação de Cloud OpenStack

Este projeto implementa uma **arquitetura multiagentes** para a operação de **cloud OpenStack**, sendo desenvolvido como entrega da disciplina **Sistemas Multiagentes** do curso de **Engenharia da Computação**.

A solução está dividida em **duas partes principais**, que devem ser sempre referenciadas nesta ordem:
1. **MCP Server**
2. **Agentes Inteligentes**

---

# Equipe:

Aluno 1: [Eduardo Nogueira](https://github.com/eduardongal)
Aluno 2: [Gislany Dias](https://github.com/gislanydias)
Aluno 3: [Igor Kádson](https://github.com/igorkso)

---

---

## 🎯 Objetivo do Projeto
Criar uma arquitetura de **sistemas multiagentes** para gerenciar e operar recursos em um ambiente **OpenStack**, utilizando integração entre um **servidor MCP** e **agentes inteligentes**.

---

## 🛠️ Tecnologias Utilizadas

### MCP Server
- **Python 3**
- [FastMCP](https://pypi.org/project/fastmcp/)
- [OpenstackSDK](https://docs.openstack.org/openstacksdk/latest/)

### Agentes Inteligentes
- **Python 3**
- [CrewAI](https://docs.crewai.com/)

---

## 📂 Estrutura do Projeto

### 📁 MCP Server
```bash
mcp/
└── src
    ├── connection.py
    ├── connection.py.backup
    ├── constant.py
    ├── DEBUG
    ├── main.py
    ├── mcp-server.log
    ├── openstack_builder.py
    ├── openstack_builder.py.backup
    ├── __pycache__/
    ├── server.py
    ├── server.py.backup
    └── WARNING
```

### 📁 Agentes Inteligentes
```bash
controlstack/
├── config/
│   ├── agents.yaml
│   ├── crew.yaml
│   └── tasks.yaml
├── crew.py
├── main.py
├── __init__.py
├── __pycache__/
└── tools/
    ├── custom_tool.py
    └── __init__.py
```

---

## 🚀 Como Instalar e Executar

### 1️⃣ Clonar o Repositório
```bash
git clone <url-do-repositorio>
cd <pasta-do-projeto>
```

### 2️⃣ Criar Ambiente Virtual e Instalar Dependências
Para o **MCP Server**:
```bash
cd mcp/requirements_mcp.txt
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Para os **Agentes Inteligentes**:
```bash
cd controlstack
python3 -m venv venv
source venv/bin/activate
pip install -r requirements_crew.txt
```

> **Obs:** Caso não exista um `requirements.txt`, instale manualmente as bibliotecas listadas na seção de **Tecnologias Utilizadas**.

### 3️⃣ Executar

#### MCP Server
```bash
python3 main.py
```

#### Agentes Inteligentes
```bash
crewai run
```

---

## 📌 Observações
- Cada parte (MCP e Agentes) pode ser desenvolvida e testada separadamente, mas a integração é o ponto central da arquitetura.
- O MCP Server atua como interface de controle e orquestração, enquanto os agentes executam tarefas de forma autônoma conforme definido nos arquivos `agents.yaml` e `tasks.yaml`.

---
