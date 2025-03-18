"""
Processador de reembolsos usando TAD Fila
"""

from fila_fifo import Fila, PedidoReembolso

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