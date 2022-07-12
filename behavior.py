import heapq
from model import Unit, UnitOrder


class Behavior:
    unit: Unit
    state_heap: list

    def __init__(self, unit):
        self.unit = unit

    def add(self, state):
        self.state_heap.append(state)

    def run(self) -> dict:
        order = {}
        heapq.heapify(self.state_heap)
        order[self.unit.id] = self.state_heap[0].run(self.unit)
        return order
