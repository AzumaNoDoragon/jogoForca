# Jogo da Forca em Python

Este é um jogo da forca implementado em Python, onde o jogador tenta adivinhar palavras relacionadas a temas específicos. O desenho da forca é atualizado a cada erro do jogador.

## Como funciona

1. **Seleção da Palavra**:
   - Uma palavra e seu tema são selecionados aleatoriamente de um arquivo de texto (`palavras.txt`).

2. **Jogabilidade**:
   - O jogador tenta adivinhar a palavra digitando letras.
   - A cada letra correta, a letra é revelada na palavra.
   - A cada letra incorreta, uma parte do desenho da forca é adicionada.
   - O jogo continua até que o jogador adivinhe a palavra ou o desenho da forca esteja completo.

## Requisitos

- Python 3.x

## Como executar

1. Certifique-se de ter o Python instalado.
2. Clone este repositório ou faça o download dos arquivos.
3. Certifique-se de ter um arquivo `palavras.txt` no mesmo diretório do script, contendo palavras e temas no formato `palavra - tema`.
4. Execute o script:

```sh
python forca.py
