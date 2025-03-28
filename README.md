# Алгоритмы и структуры данных - AI Masters (Осень 2024 - Весна 2025)

Данный репозиторий содержит материалы курса, посвящённого алгоритмам и структурам данных, который читался в осеннем семестре 2024 года и весеннем семестре 2025 года. 

Лектор - Илья Осокин

## Содержание

1. [Материалы](#материалы)
2. [Рекомендованная Литература](#рекомендованная-литература)
3. [Программа курса](#программа-курса)
    - [Лекции](#лекции)
    - [Семинары](#семинары)

## Материалы 

Репозиторий постепенно обновляется по мере продвижения курса. Здесь Вы можете найти:

- [Домашние задания](/home_assignments/)
- [Материалы лекций](/lectures/)
- [Инструкции](/docs/)

Кроме того, у данного курса есть:

- [Страница в Google Classroom](https://classroom.google.com/c/NzExODI1MDEzNTcy) - тут сдаются теоретические домашние задания
- [Страница с записями занятий](https://aimasters.ru/algo_2024) - тут есть записи занятий
- [Группа на codeforces](https://codeforces.com/group/IlvHL3HmNU) - здесь проходят контесты

## Рекомендованная Литература

Вы также можете ознакомиться со списком рекомендованной литературы:

- [Алгоритмы. Построение и анализ. Кормен.](https://disk.yandex.ru/i/CLzI0vEW4W3gXQ) - тут есть все. Можно использовать как справочник или как инструмент самообороны
- [Алгоритмы. Дасгупта.](https://disk.yandex.ru/i/ur9vX1VuXMKeWg) - покороче, с пассажами пояснительного характера

Вы можете ознакомиться полным списком литературы на [нашем Яндекс.Диске](https://disk.yandex.ru/d/li8Xj1NekV4gPA). Все книги доступны по ссылкам в формате PDF.


## Программа курса

Курс разделен на две части: первая читалась осенью 2024-го года и включала в себя теоретическую часть по алгоритмам. Вторая часть читалась весной 2025-го года и включала в себя практические занятия по пройденным темам.

### Лекции

|                      Тема занятия                      |  Дата занятия | Конспект | Домашнее задание |  Дедлайн  |
|--------------------------------------------------------|:-------------:|:--------:|:----------------:|:---------:|
| Введение. Понятие асимптотической сложности алгоритма. введение в нотацию для оценки асимптотической сложности. |    13.09.2024    | [lecture](/lectures/01_intro_complexities/lec_intro_complexities.pdf) | [assignment](/home_assignments/ha01/algaim_ha01_2024.pdf) | 19.09.2024 |
| Введение в рекурсию. Рекурсивные алгоритмы вычисления чисел Фибоначчи. Алгоритм быстрого возведения в степень. Вычисление чисел Фибоначчи при помощи быстрого возведения в степень. | 20.09.2024 | [lecture](/lectures/02_recursion_fibonacci/lec_recursion_fibonacci.pdf) | [assignment](/home_assignments/ha02/algaim_ha02_2024.pdf) | 26.09.2024 |
| Основная теорема о рекуррентных соотношениях. Применение мастер-теоремы для оценки сложности рекуррентных алгоритмов. Сортировка слиянием. Бинарный поиск в отсортированном массиве. Метод Акра-Баззи. | 27.09.2024 | [lecture](/lectures/03_master_theorem/lec_master_theorem.pdf) | [assignment](/home_assignments/ha03/algaim_ha03_2024.pdf) | 03.10.2024 |
| Алгоритм быстрой сортировки (quicksort). Выбор опорного элемента. Поиск k-ой порядковой статистики за линейное время (quickselect). | 04.10.2024 | [lecture](/lectures/04_quicksort/lec_quicksort.pdf) | [assignment](/home_assignments/ha04/algaim_ha04_2024.pdf) | 10.10.2024 |
| Алгоритм Евклида. Битовое представление чисел. Атомарные битовые операции. Поиск в массиве. Линейный поиск элемента, удовлетворяющего условию. Бинарный поиск. | 11.10.2024 | [lecture](/lectures/05_bin_operations/lec_bin_operations.pdf) | [assignment](/home_assignments/ha05/algaim_ha05_2024.pdf) | 17.10.2025 |
| Повторение пройденного материала. k-ая порядковая статистика. Majority Element. Расширенный алгоритм Евклида. | 18.10.2025 | [lectures](/lectures/06_recap_and_euclid/lec_recap_and_euclid.pdf) | [assignment](/home_assignments/ha06/algaim_ha06_2024.pdf) | 24.10.2024 |
| Решение диофантовых уравнений | 01.11.2024 | [lecture](/lectures/07_diophantine_equations/lec_diophantine_equations.pdf) | - | - |
| Стек. Очередь. Бинарное дерево. Куча. Построение кучи из линейной последовательности. Сортировка кучей. Задачи планирования и похода к точке в пространстве. Графы. Основные понятия. Методы хранения графов в памяти. Поиск в глубину (DFS). Поиск в ширину (BFS). | 08.11.2024 | [lecture](/lectures/08_graphs/lec_graphs.pdf) | [assignment](/home_assignments/ha07/algaim_ha07_2024.pdf) | 17.11.2024 |
| Алгоритмы на графах. Выделение компонент сильной связности. Топологическая сортировка. Проверка графа на двудольность. Простейшие алгоритмы поиска кратчайшего пути. Алгоритм Дейкстры. | 15.11.2024 | [lectures](/lectures/09_graph_paths/lec_graphs_paths.pdf) | [assignments](/home_assignments/ha08/algaim_ha08_2024.pdf) | 24.11.2024 |
| Поиск кратчайшего пути из одной вершины (single source). Случай отрицательных весов. Алгоритм Беллмана-Форда. Решения задач на поиск пути наименьшей стоимости в графе. | 22.11.2024 | [lectures](/lectures/10_bellman_ford/lec_bellman_ford.pdf) | [assignment](/home_assignments/ha09/algaim_ha09_2024.pdf) | 30.11.2024 |
| Сильная связность в ориентированном графе. Дополнение ориентированного графа до сильно связного. Алгоритм Эсварана-Тарьяна. | 29.11.2024 | [lectures](/lectures/11_scc_tarjan/lec_scc_tarjan.pdf) | [assignments](/home_assignments/ha10/algaim_ha10_2024.pdf) | 05.12.2024 |
| Повторение. Графы. Алгоритмы обхода графа. Использование различных методов обхода в практических задачах. Алгоритмы поиска кратчайших путей. | 06.12.2024 | [lectures](/lectures/12_graph_recap/lec_graph_recap.pdf) | [assignment](/home_assignments/ha11/algaim_ha11_2024.pdf) | 12.12.2024 |
| Минимальные остовные деревья. Алгоритм Краскала поиска минимального остовного дерева. Система непересекающихся множеств (Disjoint-set). Методы оптимизации поиска минимального остовного дерева. | 13.12.2024 | [lectures](/lectures/13_minimal_spanning_trees/lec_minimal_spanning_trees.pdf) | - | - |
| Повторение. Минимальные остовные деревья. Алгоритм Краскала. Disjoint-set и его оптимизации. Введение в динамическое программирование. Поиск наименьшего редакционного расстояния (Расстояние Левенштейна). | 20.02.2025 | [lecture](/lectures/14_mst_dynprog/lec_mst_dynprog.pdf) | [assignment](/home_assignments/ha12/algaim_ha12_2025.pdf) | 26.02.2025 |
| Продолжение динамического программирования. Алгоритм Флойда-Уоршелла. Задача о рюкзаке. Метод Ветвей и Границ. Применение динамического программирования для упрощения вычислений. Разложение числа на сумму других чисел. Задача о банкоматах. | 28.02.2025 | [lecture](/lectures/15_dynprog/lec_dynprog.pdf) | [assignment](/home_assignments/ha13/algaim_ha13_2025.pdf) | 06.03.2025 |
| Представление графа в виде матрицы. Матрицы смежности. Операции над матрице смежности. Проверка наличия пути длины k. Проверка графа на связность методом возведения матрицы смежности в степень. | 06.03.2025 | [lecture](/lectures/16_graph_matrices/lec_graph_matrices.pdf) | [assignment](/home_assignments/ha14/algaim_ha14_2025.pdf) | 12.03.2025 |

### Семинары

|                      Тема занятия                      |  Дата занятия | Код | Домашнее задание |  Дедлайн  |
|--------------------------------------------------------|:-------------:|:---:|:----------------:|:---------:|
| Поиск k-го числа Фибоначчи. Использование быстрого возведения в степень. Измерение времени выполнения программы. Алгоритмы поиска максимума. Сравнение поиска полным перебором и линейного алгоритма поиска. | 06.03.2025 | [code](/seminars/01_fibonacchi_max/sem_fibonacci_max.ipynb) | - | - |