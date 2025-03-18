"""
Testes unitários para a implementação da TAD Fila
"""

import unittest
from fila_fifo import Fila, PedidoReembolso, Paciente, Prioridade

class TestFila(unittest.TestCase):
    def setUp(self):
        """Inicializa uma nova fila antes de cada teste"""
        self.fila = Fila()

    def test_inicializacao(self):
        """Testa a inicialização da fila"""
        self.assertTrue(self.fila.is_empty())
        self.assertIsNone(self.fila.peek())

    def test_enqueue(self):
        """Testa o enfileiramento de elementos"""
        self.fila.enqueue(1)
        self.assertFalse(self.fila.is_empty())
        self.assertEqual(self.fila.peek(), 1)

    def test_dequeue(self):
        """Testa o desenfileiramento de elementos"""
        self.fila.enqueue(1)
        self.fila.enqueue(2)
        self.assertEqual(self.fila.dequeue(), 1)
        self.assertEqual(self.fila.dequeue(), 2)
        self.assertTrue(self.fila.is_empty())

    def test_fila_vazia(self):
        """Testa operações em fila vazia"""
        self.assertIsNone(self.fila.dequeue())
        self.assertIsNone(self.fila.peek())

class TestReembolso(unittest.TestCase):
    def setUp(self):
        """Inicializa uma nova fila de reembolsos antes de cada teste"""
        self.fila = Fila()
        self.pedido = PedidoReembolso(1, 1001, "Teste")

    def test_processamento_reembolsos(self):
        """Testa o processamento de pedidos de reembolso"""
        self.fila.enqueue(self.pedido)
        pedido_processado = self.fila.dequeue()
        self.assertEqual(pedido_processado.numero_pedido, 1)
        self.assertEqual(pedido_processado.numero_compra, 1001)
        self.assertEqual(pedido_processado.descricao, "Teste")

class TestAtendimento(unittest.TestCase):
    def setUp(self):
        """Inicializa uma nova fila de atendimento antes de cada teste"""
        self.fila = Fila()
        self.paciente = Paciente("Teste", 1001, Prioridade.NORMAL)

    def test_atendimento_medico(self):
        """Testa o processamento de atendimento médico"""
        self.fila.enqueue(self.paciente)
        paciente_atendido = self.fila.dequeue()
        self.assertEqual(paciente_atendido.nome, "Teste")
        self.assertEqual(paciente_atendido.numero_carteirinha, 1001)
        self.assertEqual(paciente_atendido.prioridade, Prioridade.NORMAL)

if __name__ == '__main__':
    unittest.main() 