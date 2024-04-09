## zad. 1.1
# A
x jest rodzenstwem y i odwrotnie
# B
x jest kuzynem y i odwrotnie
# C 
X i Y jest dziadkami tego samego wnuka
# D
Y jest przybranym rodzicem X
# E
x jest kuzynem y
# F
y jest bratem/siostra partnera x.
# G
X jest bratem/siostra Y.
## Zadanie1.2
```prolog
rodzeństwo(X, Y) :- 
    rodzic(Z, X), 
    rodzic(Z, Y), 
    X \= Y.
```
```prolog
kuzyn(X, Y) :- 
    rodzic(A, X), 
    rodzic(B, Y), 
    A \= B, 
    rodzeństwo(A, B),
    mężczyzna(X),
    X \= Y.
```
```prolog
przodek_do2pokolenia_wstecz(X, Y) :- 
    rodzic(X, Z), 
    rodzic(Z, Y).
```
```prolog
przybrany_rodzic(X, Y) :- 
    rodzic(X, Y), 
    rodzic_typ(X, przybrany).
biologiczny_rodzic(X, Y) :- 
    rodzic(X, Y), 
    rodzic_typ(X, biologiczny).
```
```prolog
kuzyn(X, Y) :- 
    rodzic(A, X), 
    rodzic(B, Y), 
    A \= B, 
    rodzeństwo(A, B),
    mężczyzna(X),
    X \= Y.
```
```prolog
szwagier(X, Y) :- 
    mężczyzna(X),
    rodzeństwo(X, Z),
    (partner(Y, Z);
    partner(Z, Y)),
    X \= Y.
szwagierka(X, Y) :- 
    kobieta(X),
    rodzeństwo(X, Z),
    (partner(Y, Z);
    partner(Z, Y)),
    X \= Y.
partner(X, Y) :- 
    małżeństwo(X, Y).
partner(X, Y) :- 
    małżeństwo(Y, X).
```
```prolog
rodzeństwo(X, Y) :- 
    rodzic(Z, X), 
    rodzic(Z, Y), 
    X \= Y.
```
## Zadanie 2
#
```prolog
kobieta(X) :- \+ mężczyzna(X).
```
```prolog
ojciec(X, Y) :- rodzic(X, Y), mężczyzna(X).
```
```prolog
matka(X, Y) :- rodzic(X, Y), kobieta(X).
```
```prolog
córka(X, Y) :- rodzic(Y, X), kobieta(X).
```
```prolog
brat_rodzony(X, Y) :- 
    rodzic(Z, X), 
    rodzic(Z, Y), 
    mężczyzna(X),
    \+kobieta(X),
    X \= Y.
```
```prolog
brat_przyrodni(X, Y) :- 
    rodzic(Z, X), 
    rodzic(Z, Y), 
    rodzic(A, X), 
    rodzic(B, Y), 
    mężczyzna(X),
    \+kobieta(X),
    X \= Y, 
    A \= B.
```
```prolog
rodzeństwo(X, Y) :- 
    rodzic(Z, X), 
    rodzic(Z, Y), 
    X \= Y.
kuzyn(X, Y) :- 
    rodzic(A, X), 
    rodzic(B, Y), 
    A \= B, 
    rodzeństwo(A, B),
    mężczyzna(X),
    X \= Y.
```
```prolog
dziadek_od_strony_ojca(X, Y) :- 
    rodzic(X, Z), 
    rodzic(Z, Y), 
    mężczyzna(X).
```
```prolog
dziadek_od_strony_matki(X, Y) :- 
    rodzic(Z, Y),
    rodzic(X, Z),
    mężczyzna(X).
```
```prolog
dziadek(X, Y) :- 
    rodzic(X, Z), 
    rodzic(Z, Y), 
    mężczyzna(X).
```
```prolog
babcia(X, Y) :- 
    rodzic(X, Z), 
    rodzic(Z, Y), 
    kobieta(X).
```
```prolog
wnuczka(X, Y) :- 
    rodzic(X, Z), 
    rodzic(Z, Y), 
    kobieta(Y).
```
```prolog
przodek_do2pokolenia_wstecz(X, Y) :- 
    rodzic(X, Z), 
    rodzic(Z, Y).
```
```prolog
przodek_do3pokolenia_wstecz(X, Y) :- 
    rodzic(X, Z), 
    rodzic(Z, A), 
    rodzic(A, Y).
```
