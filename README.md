# **README**

## **Descrição do Projeto**
Este projeto consiste em um sistema de gerenciamento de restaurantes, onde é possível cadastrar restaurantes, listar suas informações e receber avaliações de clientes. O sistema permite alternar o estado de um restaurante entre ativo e inativo, além de calcular a média das avaliações recebidas.

## **Estrutura do Projeto**
O projeto é composto por dois arquivos principais:

- **avaliacao.py**: Define a classe `Avalicao`, que representa uma avaliação feita por um cliente.
- **restaurante.py**: Define a classe `Restaurante`, que gerencia os restaurantes e suas avaliações.
- **app.py**: Arquivo principal que utiliza as classes para criar um restaurante e receber avaliações.

## **Classes**

### **1. Avalicao**
- **Atributos**:
  - `_cliente`: Nome do cliente que fez a avaliação.
  - `_nota`: Nota dada pelo cliente (de 1 a 5).

- **Método Construtor**:
  ```python
  def __init__(self, cliente='', nota=int):
  ```

### **2. Restaurante**
- **Atributos**:
  - `_nome`: Nome do restaurante.
  - `_categoria`: Categoria do restaurante.
  - `_ativo`: Estado do restaurante (ativo ou inativo).
  - `_avaliacao`: Lista de avaliações recebidas.

- **Métodos**:
  - `__init__(self, nome, categoria)`: Inicializa um novo restaurante.
  - `__str__(self)`: Retorna uma representação em string do restaurante.
  - `listar_restaurante(cls)`: Lista todos os restaurantes cadastrados com suas informações.
  - `ativo(self)`: Retorna o estado do restaurante (ativo ou inativo).
  - `alternar_estado(self)`: Alterna o estado do restaurante.
  - `receber_avaliacao(self, cliente, nota)`: Recebe uma avaliação de um cliente.
  - `media_avaliacoes(self)`: Calcula e retorna a média das avaliações recebidas.

## **Código do Arquivo `app.py`**
O arquivo `app.py` é o ponto de entrada do sistema e contém o seguinte código:

```python
from modelos.restaurante import Restaurante # De: pasta modelos, arquivo restaurante -> importe a classe Restaurante

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Gui', 10)
restaurante_praca.receber_avaliacao('Lais', 8)
restaurante_praca.receber_avaliacao('Amy', 2)

def main():
    Restaurante.listar_restaurante()

if __name__ == '__main__':
    main()
```

### **Descrição do Código**
- **Importação**: O código importa a classe `Restaurante` do módulo `modelos.restaurante`.
- **Instanciação**: Um novo restaurante chamado "Praça" da categoria "Gourmet" é criado.
- **Avaliações**: O restaurante recebe três avaliações de diferentes clientes com notas variadas.
- **Função Principal**: A função `main()` chama o método `listar_restaurante()` para exibir todos os restaurantes cadastrados.
- **Execução**: O bloco `if __name__ == '__main__':` garante que a função `main()` seja executada quando o arquivo for executado diretamente.

## **Uso**
Para utilizar o sistema, siga os passos abaixo:

1. **Importar as classes**:
   ```python
   from modelos.restaurante import Restaurante
   from modelos.avaliacao import Avalicao
   ```

2. **Criar um novo restaurante**:
   ```python
   restaurante1 = Restaurante("Nome do Restaurante", "Categoria")
   ```

3. **Listar restaurantes**:
   ```python
   Restaurante.listar_restaurante()
   ```

4. **Receber uma avaliação**:
   ```python
   restaurante1.receber_avaliacao("Cliente 1", 4)
   ```

5. **Alternar o estado do restaurante**:
   ```python
   restaurante1.alternar_estado()
   ```

## **Contribuição**
Contribuições são bem-vindas! Sinta-se à vontade para abrir um pull request ou relatar problemas.
