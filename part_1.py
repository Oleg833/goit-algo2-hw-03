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
    ("Склад 2", "Магазин 4", 15),
    ("Склад 2", "Магазин 5", 10),
    ("Склад 2", "Магазин 6", 25),
    ("Склад 3", "Магазин 7", 20),
    ("Склад 3", "Магазин 8", 15),
    ("Склад 3", "Магазин 9", 10),
    ("Склад 4", "Магазин 10", 20),
    ("Склад 4", "Магазин 11", 10),
    ("Склад 4", "Магазин 12", 15),
    ("Склад 4", "Магазин 13", 5),
    ("Склад 4", "Магазин 14", 10),
]

# Створення графа
graph = nx.DiGraph()

# Додавання ребер з пропускною здатністю
graph.add_weighted_edges_from(edges)


# Функція для збирання потоків до всіх магазинів від терміналу
def collect_all_flows(graph, terminal):
    flows = []
    for node in graph.nodes:
        if "Магазин" in node:
            flow_value, flow_dict = nx.maximum_flow(
                graph, terminal, node, capacity="weight"
            )
            if flow_value > 0:
                flows.append((terminal, node, flow_value))
    return flows


# Збирання потоків для Терміналу 1 і Терміналу 2
flows_terminal_1 = collect_all_flows(graph, "Термінал 1")
flows_terminal_2 = collect_all_flows(graph, "Термінал 2")

# Виведення потоків для Терміналу 1
print("\nТаблиця потоків для Терміналу 1:")
print(f"{'Термінал':<15}{'Магазин':<15}{'Фактичний Потік':<20}")
for terminal, shop, flow in flows_terminal_1:
    print(f"{terminal:<15}{shop:<15}{flow:<20}")

# Виведення потоків для Терміналу 2
print("\nТаблиця потоків для Терміналу 2:")
print(f"{'Термінал':<15}{'Магазин':<15}{'Фактичний Потік':<20}")
for terminal, shop, flow in flows_terminal_2:
    print(f"{terminal:<15}{shop:<15}{flow:<20}")

# Візуалізація графа
plt.figure(figsize=(12, 8))
pos = {
    "Термінал 1": (-2, 2),
    "Термінал 2": (2, 2),
    "Склад 1": (-3, 1),
    "Склад 2": (-1, 1),
    "Склад 3": (1, 1),
    "Склад 4": (3, 1),
    "Магазин 1": (-6.0, 0),
    "Магазин 2": (-5.0, 0),
    "Магазин 3": (-4.0, 0),
    "Магазин 4": (-2.8, 0),
    "Магазин 5": (-2, 0),
    "Магазин 6": (-1.2, 0),
    "Магазин 7": (-0.2, 0),
    "Магазин 8": (0.7, 0),
    "Магазин 9": (1.5, 0),
    "Магазин 10": (2.5, 0),
    "Магазин 11": (3.5, 0),
    "Магазин 12": (4.5, 0),
    "Магазин 13": (5.5, 0),
    "Магазин 14": (6.5, 0),
}

# Відображення вузлів і ребер
nx.draw(
    graph,
    pos,
    with_labels=True,
    node_color="lightblue",
    node_size=3000,
    font_size=10,
    font_weight="bold",
    arrowsize=15,
)

# Додавання ваги до ребер
edge_labels = nx.get_edge_attributes(graph, "weight")
nx.draw_networkx_edge_labels(
    graph,
    pos,
    edge_labels={(u, v): f"{d}" for u, v, d in graph.edges(data="weight")},
    font_size=9,
)

plt.title("Логістична мережа")
plt.show()
