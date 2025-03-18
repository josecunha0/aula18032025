"""
Processador de atendimento em clínica médica usando TAD Fila
"""

from fila_fifo import Fila, Paciente, Prioridade

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