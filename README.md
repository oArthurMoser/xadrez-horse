# Knight’s Tour

O problema pode ser resolvido com busca exaustiva (backtracking), ou seja, com um algoritmo guloso.

Para o trabalho utilizamos a heurística de Warnsdorff.

É uma estratégia gulosa Warnsdorff. O qual possui a seguinte regra:

Sempre mova o cavalo para a casa que possui o menor número de movimentos futuros possíveis. Ou seja, se o cavalo pode ir para várias casas, ele escolhe a que é mais restrita, no caso, a com menos saídas possíveis depois. Por causa disso é reduzida as chances do cavalo ficar preso antes de visitar todas as casas.

Trabalho realizado por [Daniel Sansão Araldi](https://github.com/DanielAraldi), [Arthur Moser](https://github.com/oArthurMoser) e [Breno Capraro de Souza](https://github.com/BrenoCapraroDeSouza) para a matéria de Inteligência Artificial I.
