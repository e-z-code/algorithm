# GAME THEORY

## Sprague-Grundy Theorem

You can apply the Sprague-Grundy theorem to the problem if a given game satisfies the following conditions.

```
(1) There are two players.
(2) The players take alternative turns.
(3) The players know the optimal move.
(4) A player loses if there is no possible move. 
(5) The game terminates in finite time.
```

In the Sprague-Grundy theorem, each game state X can be represented by a Grundy number G(X) by the following rules.

```
(1) If there is no possible move for X, G(X) = 0.
(2) Let X` be the set of Grundy numbers of the next possible game states from X. Then, G(X) = MEX(X').
(3) Let's assume a game X consists of multiple games X1, X2, ..., Xn. Then, G(X) = G(X1) ⊕ G(X2) ⊕ ... ⊕ G(Xn).
```

Let S denote the start state. Then, the following holds.

```
If G(S) = 0, the first player loses.
Otherwise, the first player wins.
```

*Reference : https://velog.io/@cldhfleks2/Sprague-Grundy-Theorem*