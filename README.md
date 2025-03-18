# Implementação de TAD Fila (FIFO)

Este projeto implementa uma TAD (Tipo Abstrato de Dados) Fila (FIFO) com dois casos de uso práticos:
1. Reembolso de Compras
2. Atendimento em Clínica Médica

## Estrutura do Projeto

```
fila_fifo/
├── fila_fifo.py          # Implementação principal da TAD Fila
├── reembolso/            # Módulo de reembolsos
│   ├── __init__.py
│   └── processador.py
├── atendimento/          # Módulo de atendimento médico
│   ├── __init__.py
│   └── processador.py
├── main.py               # Ponto de entrada do programa
├── tests/                # Testes unitários
│   └── test_fila.py
└── README.md             # Este arquivo
```

## Requisitos

- Python 3.6 ou superior
- Módulos padrão do Python (não requer dependências externas)

## Como Executar

1. Clone o repositório
2. Navegue até o diretório do projeto
3. Execute o programa principal:
   ```bash
   python main.py
   ```

## Como Executar os Testes

Para executar os testes unitários:
```bash
python -m unittest tests/test_fila.py
```

## Funcionalidades

### 1. Reembolso de Compras
- Enfileiramento de pedidos
- Processamento na ordem FIFO
- Análise e aprovação/reprovação
- Registro de status e justificativas

### 2. Atendimento em Clínica Médica
- Enfileiramento de pacientes
- Atendimento na ordem FIFO
- Registro de ordem de atendimento
- Suporte a níveis de prioridade

## Documentação

A documentação completa do projeto está disponível nos seguintes arquivos:
- `analise_requisitos.md`: Análise de requisitos
- `arquitetura_software.md`: Arquitetura e diagramas
- `desenvolvimento_algoritmos.md`: Algoritmos e pseudocódigo
- `implementacao_programador.md`: Detalhes da implementação
- `relatorio_testes.md`: Relatório de testes

## Autores

José Fernando Cunha da Silva | 
Gustavo Moreira Schneider | 
Data: 18/03/2025 
