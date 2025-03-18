# Documento de Análise de Requisitos - TAD Fila (FIFO)

## 1. Introdução
Este documento apresenta a análise de requisitos para a implementação de uma TAD (Tipo Abstrato de Dados) Fila (FIFO) com dois casos de uso práticos: Reembolso de Compras e Atendimento em Clínica Médica.

## 2. Casos de Uso

### 2.1 Reembolso de Compras

#### Descrição
Sistema para gerenciar pedidos de reembolso de compras, processando-os em ordem FIFO (First In, First Out).

#### Requisitos Funcionais
1. **Entrada de Dados**
   - Número do pedido
   - Número da compra
   - Descrição da solicitação

2. **Processamento**
   - Enfileiramento dos pedidos na ordem de chegada
   - Análise dos pedidos com decisão (aprovado/reprovado)
   - Geração de justificativa em caso de reprovação
   - Remoção do pedido após análise

3. **Saída**
   - Registro da análise de cada pedido
   - Status do processamento
   - Justificativa da decisão

### 2.2 Atendimento em Clínica Médica

#### Descrição
Sistema para gerenciar a fila de atendimento em uma clínica médica, seguindo a ordem FIFO.

#### Requisitos Funcionais
1. **Entrada de Dados**
   - Nome do paciente
   - Número da carteirinha
   - Nível de prioridade (urgência, agendado, normal)

2. **Processamento**
   - Enfileiramento dos pacientes na ordem de chegada
   - Atendimento na ordem FIFO
   - Registro da ordem de atendimento
   - Remoção do paciente após atendimento

3. **Saída**
   - Registro da ordem de atendimento
   - Informações do paciente em atendimento
   - Status do atendimento

## 3. Requisitos Não-Funcionais

### 3.1 Performance
- O sistema deve processar operações de enfileiramento e desenfileiramento em tempo O(1)
- A estrutura deve ser eficiente em termos de memória

### 3.2 Confiabilidade
- O sistema deve manter a integridade dos dados
- Não deve haver perda de informações durante o processamento

### 3.3 Usabilidade
- Interface clara e intuitiva
- Mensagens de erro informativas
- Feedback visual do estado da fila

## 4. Regras de Negócio

### 4.1 Reembolso de Compras
- Pedidos devem ser processados na ordem de chegada
- Cada pedido deve ter um número único
- A análise deve ser documentada com justificativa

### 4.2 Atendimento Médico
- Pacientes devem ser atendidos na ordem de chegada
- O sistema deve registrar a ordem de atendimento
- Informações do paciente devem ser mantidas durante todo o processo

## 5. Restrições
- Implementação em Python
- Uso de tipos estáticos
- Documentação completa do código
- Testes unitários para todas as funcionalidades 