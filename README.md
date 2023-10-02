# Projeto P1

> Um jogo 2D em que o jogador precisa coletar operações matemáticas com o intuito de alcanças uma determinada meta gerada aleatoriamente, tudo isso em 90 segundos.
## Sumário
1. [Intruções](#intruções)
2. [Membros da equipe e suas atribuições](#membros-da-equipe-e-suas-atribuições)
3. [Estrutura do projeto](#estrutura-do-projeto)
4. [Bibliotecas](#bibliotecas)
5. [Conceitos utilizados](#conceitos-utilizados)
6. [Desafios, erros e aprendizados](#desafios-erros-e-aprendizados)
7. [Galeria do projeto](#galeria-do-projeto)

## Intruções
1. Instalação do python e dos pacotes listados em __*requirements.txt*__
2. Download da branch *Main* deste repositório
3. Extraia o arquivo _*.zip*_
4. Execute o arquivo _*main.py*_
> A movimentação do personagem é feita pelas setas do teclado
## Membros da equipe e suas atribuições
[Vitor Negromonte](https://github.com/vitornegromonte): mecânica dos coletáveis (operações) e interface de jogo

[Adna Farias](): implementação do sistema de timer

[Danielly Santos](https://github.com/daniellysantoslds): movimentação do jogador e scoreboard

[Natália Albuquerque](https://github.com/natalialbuquerque): mecânica de criação dos objetos coletáveis


## Estrutura do projeto

- Main.py: Controle do loop principal do jogo, responsável pelas telas de começo e fim da partida e configuração da interface.
- Coletaveis.py: Responsável pela geração dos objetos coletáveis, fluxo de operações e mecânica de queda dos objetos.
- Player.py: Responsável pelas mecânicas de movimentação e colisão do jogador com as operações.
- Timer.py: Definição do sistema de temporizador da partida (90 segundos).

- Assets: diretório que contém os recursos visual do projeto (imagens, sprites, fontes e etc).
  
![Digrama contendo a estrutura dos diretórios do projeto](assets/imgs/diagram.jpg)

## Bibliotecas:
Foi utilizado o [Pygame](pygame.org) para o desenvolvimento, sobretudo, devido a sua extensa documentação e implementação em projetos na comunidade open source.

## Conceitos utilizados

## Desafios, erros e aprendizados

## Galeria do projeto