# Documento de Implementação - TAD Fila (FIFO)

## 1. Estrutura do Projeto

```
fila_fifo/
├── fila_fifo.py      # Implementação principal
├── tests/            # Testes unitários
└── README.md         # Documentação do projeto
```

## 2. Implementação da TAD Fila

### 2.1 Classe Fila
```python
class Fila:
    """
    Implementação de uma Fila (FIFO) usando lista
    """
    def __init__(self):
        self._items = []
    
    def enqueue(self, item: Any) -> None:
        """
        Adiciona um elemento ao final da fila
        """
        self._items.append(item)
    
    def dequeue(self) -> Optional[Any]:
        """
        Remove e retorna o primeiro elemento da fila
        Retorna None se a fila estiver vazia
        """
        if self.is_empty():
            return None
        return self._items.pop(0)
    
    def is_empty(self) -> bool:
        """
        Verifica se a fila está vazia
        """
        return len(self._items) == 0
    
    def peek(self) -> Optional[Any]:
        """
        Retorna o primeiro elemento da fila sem removê-lo
        Retorna None se a fila estiver vazia
        """
        if self.is_empty():
            return None
        return self._items[0]
```

### 2.2 Classes de Dados

#### PedidoReembolso
```python
@dataclass
class PedidoReembolso:
    numero_pedido: int
    numero_compra: int
    descricao: str
    status: Optional[str] = None
    justificativa: Optional[str] = None
```

#### Paciente
```python
@dataclass
class Paciente:
    nome: str
    numero_carteirinha: int
    prioridade: Prioridade
    ordem_atendimento: Optional[int] = None
```

#### Prioridade
```python
class Prioridade(Enum):
    URGENTE = 1
    AGENDADO = 2
    NORMAL = 3
```

## 3. Casos de Uso

### 3.1 Processamento de Reembolsos
```python
def processar_reembolsos():
    """
    Processa pedidos de reembolso usando a estrutura FIFO
    """
    fila_reembolsos = Fila()
    
    # Simulando entrada de pedidos
    pedidos = [
        PedidoReembolso(1, 1001, "Reembolso de material de escritório"),
        PedidoReembolso(2, 1002, "Reembolso de passagem"),
        PedidoReembolso(3, 1003, "Reembolso de alimentação")
    ]
    
    # Enfileirando pedidos
    for pedido in pedidos:
        fila_reembolsos.enqueue(pedido)
        print(f"Pedido {pedido.numero_pedido} enfileirado")
    
    # Processando pedidos
    print("\nProcessando pedidos de reembolso:")
    while not fila_reembolsos.is_empty():
        pedido = fila_reembolsos.dequeue()
        # Simulando análise do pedido
        if pedido.numero_pedido % 2 == 0:
            pedido.status = "APROVADO"
            pedido.justificativa = "Pedido dentro das políticas"
        else:
            pedido.status = "REPROVADO"
            pedido.justificativa = "Documentação incompleta"
        
        print(f"\nPedido {pedido.numero_pedido}:")
        print(f"Status: {pedido.status}")
        print(f"Justificativa: {pedido.justificativa}")
```

### 3.2 Atendimento em Clínica Médica
```python
def processar_atendimento():
    """
    Processa atendimento em clínica médica usando a estrutura FIFO
    """
    fila_atendimento = Fila()
    
    # Simulando entrada de pacientes
    pacientes = [
        Paciente("João Silva", 1001, Prioridade.URGENTE),
        Paciente("Maria Santos", 1002, Prioridade.AGENDADO),
        Paciente("Pedro Oliveira", 1003, Prioridade.NORMAL)
    ]
    
    # Enfileirando pacientes
    for paciente in pacientes:
        fila_atendimento.enqueue(paciente)
        print(f"Paciente {paciente.nome} enfileirado")
    
    # Processando atendimento
    print("\nProcessando atendimento médico:")
    ordem = 1
    while not fila_atendimento.is_empty():
        paciente = fila_atendimento.dequeue()
        paciente.ordem_atendimento = ordem
        print(f"\nAtendendo paciente {ordem}:")
        print(f"Nome: {paciente.nome}")
        print(f"Carteirinha: {paciente.numero_carteirinha}")
        print(f"Prioridade: {paciente.prioridade.name}")
        ordem += 1
```

## 4. Função Principal
```python
def main():
    """
    Função principal que executa os casos de uso
    """
    print("=== Sistema de Gerenciamento FIFO ===\n")
    
    print("Caso 1: Processamento de Reembolsos")
    print("=" * 40)
    processar_reembolsos()
    
    print("\nCaso 2: Atendimento em Clínica Médica")
    print("=" * 40)
    processar_atendimento()
```

## 5. Considerações de Implementação

### 5.1 Escolhas de Design
- Uso de `dataclass` para simplificar a criação de classes de dados
- Tipagem estática com `typing` para maior segurança
- Enumeração para níveis de prioridade
- Lista dinâmica para implementação da fila

### 5.2 Tratamento de Erros
- Verificação de fila vazia antes de operações
- Validação de tipos com anotações
- Retorno de None para operações inválidas

### 5.3 Otimizações
- Uso de listas nativas do Python
- Implementação eficiente de operações FIFO
- Código limpo e bem documentado 