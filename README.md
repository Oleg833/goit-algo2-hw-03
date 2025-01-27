# goit-algo2-hw-03

## Висновок
### Завдання1:

- **"Термінал 1" забезпечує більший потік до магазинів**, оскільки його максимальні значення потоку, наприклад, до "Магазин 3" (20 одиниць) і "Магазин 7" (15 одиниць), свідчать про його велику пропускну здатність.
- **"Термінал 2"** також значно постачає товари, але його потоки рівномірно розподілені між багатьма магазинами.

- **Маршрути з найменшою пропускною здатністю:**
  - "Склад 4" → "Магазин 13" (5 одиниць)
  - "Склад 4" → "Магазин 14" (10 одиниць)
- **Вплив:** Ці маршрути обмежують загальний потік товарів до кінцевих магазинів, що призводить до недопостачання товарів.

- **Магазини з найменшим постачанням:**
  - "Магазин 13" отримав лише 5 одиниць.
  - "Магазин 14" отримав 10 одиниць.
- **Покращення:** Постачання до цих магазинів можна збільшити шляхом розширення пропускної здатності таких маршрутів:
  - "Склад 4" → "Магазин 13"
  - "Склад 4" → "Магазин 14"

- **Вузькі місця:**
  - "Склад 4" → магазини (пропускна здатність обмежена).
  - "Склад 2" → "Магазин 4" і "Магазин 5" (обмежені 15 і 10 одиниць відповідно).


### Завдання2:

### Результати виконання
- **OOBTree** виконав 100 діапазонних запитів за **0.006627 секунд**.
- **Dict** виконав 100 діапазонних запитів за **0.672286 секунд**.

### Аналіз
1. **OOBTree**:
   - Використовує метод `items(min, max)` для швидкого доступу до значень у заданому діапазоні.
   - Ефективність: O(log n) завдяки структурі B-дерева.

2. **Dict**:
   - Реалізує діапазонний запит через лінійний перебір усіх значень.
   - Ефективність: O(n), що значно повільніше при великих обсягах даних.

### Підсумок
- **OOBTree** значно переважає `Dict` для виконання діапазонних запитів завдяки оптимізованій структурі.
- **Dict** може бути корисним для інших операцій, але для діапазонних запитів його продуктивність поступається.




