from simevopy import Environment, Organism, Genes, Food
import random
import matplotlib.pyplot as plt
import numpy as np

width = 100
height = 100

def setup_base_organism(env, count=20):
    for _ in range(count):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        # x = random.randint(0, env.width - 1)
        # y = random.randint(0, env.height - 1)

        dna = chr(20) * 4
        env.add_organism(Organism(Genes(dna)), x, y)

def distribute_food_randomly(env, food_count=50):
    for _ in range(food_count):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)

        env.add_food(x, y)

def visualize_objects(env):
    objects = env.get_all_objects()
    organisms_positions = []
    food_positions = []
    awareness_radii = []

    for obj in objects:
        if isinstance(obj, Organism):
            organisms_positions.append(obj.get_position())
            awareness_radii.append(obj.get_reaction_radius())
        elif isinstance(obj, Food):
            food_positions.append(obj.get_position())

    organisms_positions = np.array(organisms_positions)
    food_positions = np.array(food_positions)
    awareness_radii = np.array(awareness_radii)

    # print(organisms_positions)
    # print(food_positions)
    # print(awareness_radii)

    plt.clf()
    # 檢查 organisms_positions 是否為空，不為空時繪圖
    if organisms_positions.size > 0:
        plt.scatter(organisms_positions[:, 0], organisms_positions[:, 1], s=1, color='blue', label='Organisms')
        for i in range(len(organisms_positions)):
            circle = plt.Circle((organisms_positions[i, 0], organisms_positions[i, 1]), awareness_radii[i], color='red', fill=False, alpha=0.5)
            plt.gca().add_artist(circle)

    # 檢查 food_positions 是否為空，不為空時繪圖
    if food_positions.size > 0:
        plt.scatter(food_positions[:, 0], food_positions[:, 1], s=1, color='green', label='Food')

    plt.xlim(0, width)
    plt.ylim(0, height)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.title('Organisms and Food Distribution')
    plt.draw()
    plt.pause(0.1)

env = Environment(width, height)

setup_base_organism(env, 5)

for i in range(1):
    print("=========================================")
    print(f"Gen {i} th")
    distribute_food_randomly(env, 30)
    visualize_objects(env)
    env.simulate_iteration(50, on_each_iteration=visualize_objects)

plt.ioff()
plt.show()
