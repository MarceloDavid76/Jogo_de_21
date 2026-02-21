🃏 Blackjack Game – Python

Projeto de jogo Blackjack (21) desenvolvido em Python, executado via terminal.
O jogador compete contra o computador seguindo as regras básicas do jogo.

📌 Sobre o Projeto

Este projeto simula uma partida de Blackjack onde:

O jogador recebe cartas aleatórias
Pode escolher pedir mais cartas ou parar
O computador joga automaticamente seguindo regra de pontuação
O vencedor é definido conforme as regras do jogo

O projeto possui diferentes versões do jogo, mostrando a evolução da implementação (mais simples até versão com funções organizadas).

🧠 Conceitos Aplicados

Funções
Listas
Laços (while)
Condicionais (if/elif/else)
Modularização
Organização de código
Lógica de jogo
Uso de biblioteca padrão (random, os)

📂 Estrutura do Projeto

blackjack-game/
│
├── theatcher_game.py   # Versão mais organizada e modularizada
├── my_game.py          # Versão intermediária
├── teste.py            # Primeira versão mais simples
├── art.py              # Logo ASCII do jogo
└── README.md

🎮 Regras do Jogo

Objetivo: chegar o mais próximo possível de 21
Ás vale 11 ou 1 (ajustado automaticamente)
Se passar de 21 → perde
Blackjack (Ás + 10) vence automaticamente
O computador compra cartas até atingir pelo menos 17


🛠 Tecnologias Utilizadas

Python 3
Biblioteca random
Biblioteca os
