from modelos.restaurante import Restaurante #De: pasta modelos, arquivo restaurante -> importe a classe Restaurante

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Gui', 10)
restaurante_praca.receber_avaliacao('Lais', 8)
restaurante_praca.receber_avaliacao('Amy', 2)

def main():
    Restaurante.listar_restaurante()

if __name__ == '__main__':
    main()