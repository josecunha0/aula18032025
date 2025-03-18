"""
Implementação de TAD Fila (FIFO) com casos de uso:
1. Reembolso de Compras
2. Atendimento em Clínica Médica
"""

from dataclasses import dataclass
from typing import Any, Optional
from enum import Enum

class Prioridade(Enum):
    URGENTE = 1
    AGENDADO = 2
    NORMAL = 3

@dataclass
class PedidoReembolso:
    numero_pedido: int
    numero_compra: int
    descricao: str
    status: Optional[str] = None
    justificativa: Optional[str] = None

@dataclass
class Paciente:
    nome: str
    numero_carteirinha: int
    prioridade: Prioridade
    ordem_atendimento: Optional[int] = None

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