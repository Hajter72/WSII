## Zad.1
#A
```
man(Marcus)
```
```
Pompeian(Marcus)
```
```
∀x : Pompeian(x) → Roman(x)
```
```
ruler(Caesar)
```
```
∀x : Roman(x) → loyalto(x,Caesar) ∨ hate(x,Caesar)
```
```
∀x :∃y :loyalto(x, y)
```
```
∀x :∀y : man(x) ∧ ruler(y) ∧ tryassass(x, y) → ¬loyalto(x, y)
```
```
tryassass(Marcus,Caesar)
```
#B
```
¬loyalto(Marcus, Caesar) podstawiamy równość
```
```
man(Marcus) ∧ ruler(Caesar) ∧ tryassass(Marcus, Caesar)
```
```
ruler(Caesar) i  tryassass(Marcus, Caesar) wyrzucamy bo wynika to z wcześniej podanych faktów
```
```
man(Marcus)
```
```
fakt zwraca logiczną jedynkę, udowodniliśmy wnioskowaniem wstecz metodą modus ponens.
```
# C
#Zmienimy następujące funkcje do CNF 
```∀x : Pompeian(x) → Roman(x) ```
```∀x : Roman(x) → loyalto(x,Caesar) ∨ hate(x,Caesar)```
```∀x :∃y :loyalto(x, y)```
```∀x :∀y : man(x) ∧ ruler(y) ∧ tryassass(x, y) → ¬loyalto(x, y)```
#
Pozostałe funckje albo nie wymagają zmian albo wystarczy usunąć kwantyfikatory, które nie zmienią znaczenia faktu.
#
```∀x : Pompeian(x) → Roman(x) ```
```
a → b ≡ ¬a ∨ b
∀x :¬Pompeian(x) ∨ Roman(x)
Opuszcza się w wyrażeniu kwantyfikatory wielkie i nie zmienia to znaczenia całego wyrażenia.
¬Pompeian(x1) ∨ Roman(x1)
```
#
```∀x : Roman(x) → loyalto(x,Caesar) ∨ hate(x,Caesar)```
```
∀x : ¬Roman(x)  ∨ loyalto(x,Caesar) ∨ hate(x,Caesar)
¬Roman(x2)  ∨ loyalto(x2,Caesar) ∨ hate(x2,Caesar)
```
#
```∀x :∃y :loyalto(x, y)```
```
loyalto(x3, f1(x3))
```
#
```∀x :∀y : man(x) ∧ ruler(y) ∧ tryassass(x, y) → ¬loyalto(x, y)```
```
∀x :∀y : ¬(man(x) ∧ ruler(y) ∧ tryassass(x, y)) ∨ ¬loyalto(x, y)
Prawo de Morgana dla negacji koniunkcji
(¬man(x4)∨¬ruler(y1)∨¬tryassass(x4,y1))∨¬loyalto(x4,y1)
i uproszczenie
¬man(x4)∨¬ruler(y1)∨¬tryassass(x4,y1)∨¬loyalto(x4,y1)
```
# D
```
Negujemy predykat do udowodnienia "Markus był nie lojalny wobec Cezara".
loyalto(Macrus, Caesar) z zestawiamy to z  ¬man(x4)∨¬ruler(y1)∨¬tryassass(x4,y1)∨¬loyalto(x4,y1) i podstawiamy pod x4 Markusa, a pod y1 Cezara.
¬man(Marcus)∨¬ruler(Caesar)∨¬tryassass(Marcus,Caesar) zestawiamy to z man(Marcus)
¬ruler(Caesar)∨¬tryassass(Marcus,Caesar) zestawiamy to z  ruler(Caesar)
¬tryassass(Marcus,Caesar) zestawiamy to z tryassass(Marcus,Caesar)
Otrzymujemy klauzulę pustą, dowód zakończono.
```
## Zadanie 3
# Baza predykatów
```
1.man(Marcus)
```
```
2.Pompeian(Marcus)
```
```
3.born(Marcus,40)
```
```
4.∀x : Pompeian(x) → died(x,79)
```
```
5.erupted(Volcano,79)
```
```
6. ∀x: ∀t1: ∀t2: man(x) ∧ born(x,t1) ∧ gt(t2-t1,150) → dead(x,t2)
```
```
7. now=2021
```
```
8. ∀x: ∀t1: ∀t2: died(x,t1) ∧ gt(t2,t1) → dead(x,t2)
```
# Dowodzenie tego, ze Markus nie żyje
```
dead(Marcus, now) reguła 8.
died(Marcus, t1) ∧ gt(now,t1) reguła 4
Pompeian(Marcus) ∧ gt(now,79) reguła 2
gt(now,79) równość z regułą 7
gt(2021,79) obliczenie gt i tyle
```
# Dowod 2
```
dead(Marcus, now) reguła 6.
man(Marcus) ∧ born(Marcus,t1) ∧ gt(now-t1,150) reguła 1
born(Marcus,t1) ∧ gt(now-t1,150) reguła 3
gt(now-40,150) równość 7
gt(2021-40,150)
gt(1981,150)
```
# Zamiana na CNF funckji
```
1.man(Marcus)
```
```
2.Pompeian(Marcus)
```
```
3.born(Marcus,40)
```
```
4. ¬Pompeian(x1) ∨ died(x1,79)
```
```
5.erupted(Volcano,79)
```
```
6. ¬man(x2) ∨ ¬born(x2,t1) ∨ ¬gt(t2-t1,150) ∨ dead(x,t2)
```
```
7. now=2021
```
```
8. ¬died(x3,t3) ∨ ¬gt(t4,t3) ∨ dead(x3,t4)
```
# Dowod 3
```
Przyjmujemy, że Markus żyje
¬dead(Marcus, now), podstawiamy z ¬died(x3,t3) ∨ ¬gt(t4,t3) ∨ dead(x3,t4), gdzie 'Macrus' to x3, a 'now' to t4
¬died(Marcus,t3) ∨ ¬gt(now,t3) podstawiamy z 4, gdzie x1 to Marcus, a t3 to 79
¬Pompeian(Marcus)  ∨ ¬gt(now,79) pod 'now' podstawiamy wartość z 7
¬Pompeian(Marcus)  ∨ ¬gt(2021,79) redukcja
¬Pompeian(Marcus) zestawiamy z 2. i otrzymujemy klauzulę pustą, zakończyliśmy dowód.
```
