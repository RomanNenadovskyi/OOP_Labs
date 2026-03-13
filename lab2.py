import asyncio
import random
import time
import networkx as nx
import matplotlib.pyplot as plt


#Завдання 1.(КЛАС ВУЗЛА МЕРЕЖІ)
class Node:

    def __init__(self, name):
        self.name = name
        self.connections = []

    def connect(self, node):
        self.connections.append(node)
        node.connections.append(self)
# -----------------------------


#Завдання 2.(КЛАС МАРШРУТИЗАТОРА)
class Router(Node):
    pass
# -----------------------------


#Завдання 3.(КЛАС ПАКЕТА)
class Packet:

    def __init__(self, src, dest, size, protocol):
        self.src = src
        self.dest = dest
        self.size = size
        self.protocol = protocol


# -----------------------------


#Завдання 4.(TCP ПРОТОКОЛ)
class TCPProtocol:

    name = "TCP"

    @staticmethod
    async def transmit(src, dest, network):

        packet = Packet(src, dest, random.randint(200, 500), "TCP")

        await asyncio.sleep(random.uniform(0.05, 0.2))

        if random.random() < network.loss_rate:
            network.packets_lost += 1
            print("TCP packet lost")
        else:
            print(f"TCP packet delivered {src.name} -> {dest.name}")
# -----------------------------


#Завдання 5.UDP ПРОТОКОЛ
class UDPProtocol:

    name = "UDP"

    @staticmethod
    async def transmit(src, dest, network):

        packet = Packet(src, dest, random.randint(50, 200), "UDP")

        await asyncio.sleep(random.uniform(0.05, 0.2))

        if random.random() < network.loss_rate:
            network.packets_lost += 1
            print("UDP packet lost")
        else:
            print(f"UDP packet delivered {src.name} -> {dest.name}")
# -----------------------------


#Завдання 6.(КЛАС МЕРЕЖІ)
# -----------------------------
class Network:

    def __init__(self):

        self.nodes = []

        self.loss_rate = random.uniform(0.10, 0.15)

        self.packets_sent = 0
        self.packets_lost = 0

        self.total_time = 0

    async def simulate(self, protocol, count=10):

        for i in range(count):

            src, dest = random.sample(self.nodes, 2)

            start = time.time()

            self.packets_sent += 1

            await protocol.transmit(src, dest, self)

            end = time.time()

            self.total_time += (end - start)

    def analyze(self):

        avg_time = self.total_time / self.packets_sent

        loss_percent = (self.packets_lost / self.packets_sent) * 100

        bandwidth = (self.packets_sent - self.packets_lost) / self.total_time

        print("\n--- Network statistics ---")

        print("Average time:", round(avg_time, 4), "sec")

        print("Packet loss:", round(loss_percent, 2), "%")

        print("Bandwidth:", round(bandwidth, 2), "packets/sec")

    def visualize(self, title):

        G = nx.Graph()

        for node in self.nodes:
            for conn in node.connections:
                G.add_edge(node.name, conn.name)

        nx.draw(G,
                with_labels=True,
                node_color="lightblue",
                node_size=2500)

        plt.title(title)

        plt.show()
# -----------------------------


#Завдання 7.(ЗІРКОВА ТОПОЛОГІЯ)
async def star_topology():

    network = Network()

    router = Router("Router")

    pcs = [Node("PC1"), Node("PC2"), Node("PC3"), Node("PC4")]

    network.nodes = [router] + pcs

    for pc in pcs:
        router.connect(pc)

    await network.simulate(TCPProtocol)

    network.analyze()

    network.visualize("Star topology")
# -----------------------------


#Завдання 8.(СІТКОВА ТОПОЛОГІЯ)
async def mesh_topology():

    network = Network()

    nodes = [Node("PC1"), Node("PC2"), Node("PC3"), Node("PC4")]

    network.nodes = nodes

    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            nodes[i].connect(nodes[j])

    await network.simulate(UDPProtocol)

    network.analyze()

    network.visualize("Mesh topology")
# -----------------------------


#Завдання 9.(ГОЛОВНА ФУНКЦІЯ)

async def main():

    print("STAR NETWORK")

    await star_topology()

    print("\nMESH NETWORK")

    await mesh_topology()


asyncio.run(main())