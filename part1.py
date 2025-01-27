import networkx as nx
import matplotlib.pyplot as plt

# Дані про пропускну здатність
edges = [
    ("Термінал 1", "Склад 1", 25),
    ("Термінал 1", "Склад 2", 20),
    ("Термінал 1", "Склад 3", 15),
    ("Термінал 2", "Склад 3", 15),
    ("Термінал 2", "Склад 4", 30),
    ("Термінал 2", "Склад 2", 10),
    ("Склад 1", "Магазин 1", 15),
    ("Склад 1", "Магазин 2", 10),
    ("Склад 1", "Магазин 3", 20),
    ("Склад 1", "Магазин 4", 15),
    ("Склад 2", "Магазин 5", 10),
    ("Склад 2", "Магазин 6", 25),
    ("Склад 3", "Магазин 7", 20),
    ("Склад 3", "Магазин 8", 15),
    ("Склад 3", "Магазин 9", 10),
    ("Склад 4", "Магазин 10", 20),
    ("Склад 4", "Магазин 11", 10),
    ("Склад 4", "Магазин 12", 15),
    ("Склад 4", "Магазин 13", 5),
    ("Склад 4", "Магазин 14", 10)
]

# Створення графа
graph = nx.DiGraph()

# Додавання ребер з пропускною здатністю
graph.add_weighted_edges_from(edges)

# Візуалізація графа
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(graph, seed=42)

# Відображення вузлів і ребер
nx.draw(graph, pos, with_labels=True, node_color="lightblue", node_size=3000, font_size=10, font_weight="bold", arrowsize=15)

# Додавання ваги до ребер
edge_labels = nx.get_edge_attributes(graph, 'weight')
nx.draw_networkx_edge_labels(graph, pos, edge_labels={(u, v): f"{d}" for u, v, d in graph.edges(data="weight")}, font_size=9)

plt.title("Логістична мережа")
plt.show()
