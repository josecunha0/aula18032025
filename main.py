"""
Programa principal que executa os casos de uso da TAD Fila
"""

from reembolso.processador import processar_reembolsos
from atendimento.processador import processar_atendimento

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

if __name__ == "__main__":
    main() 