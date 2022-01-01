# -*- coding: utf-8 -*-
import os
import json
import sys
BASE_PATH = os.path.abspath(os.path.dirname(__file__))
print(BASE_PATH)
sys.path.insert(0,BASE_PATH.split('\\test')[0])
from pathfinding.finder.a_star import AStarFinder
from pathfinding.finder.dijkstra import DijkstraFinder
from pathfinding.core.grid import Grid
from pathfinding.core.diagonal_movement import DiagonalMovement
import time

# test scenarios from Pathfinding.JS
scenarios = os.path.join(BASE_PATH, 'Scenarios\\path_scenario_1.json')
data = json.load(open(scenarios, 'r'))
finders = [AStarFinder, DijkstraFinder]


def test_path():
    """
    test scenarios defined in json file
    """
    for scenario in data:
        for find in finders:
            grid = Grid(matrix=scenario['matrix'])
            start = grid.node(scenario['startX'], scenario['startY'])
            end = grid.node(scenario['endX'], scenario['endY'])
            finder = find()
            path, runs = finder.find_path(start, end, grid)
            print(find.__name__,runs, len(path))
            print(grid.grid_str(path=path, start=start, end=end))
            #assert len(path) == scenario['expectedLength']
    

def test_path_diagonal():
    # test diagonal movement
    for scenario in data:
        for find in finders:
            grid = Grid(matrix=scenario['matrix'])
            start = grid.node(scenario['startX'], scenario['startY'])
            end = grid.node(scenario['endX'], scenario['endY'])
            finder = find(diagonal_movement=DiagonalMovement.always)
            path, runs = finder.find_path(start, end, grid)
            print(find.__name__, runs, len(path))
            print(grid.grid_str(path=path, start=start, end=end))
            #assert len(path) == scenario['expectedDiagonalLength']


if __name__ == '__main__':

    T1 = 0
    T3 = 0

    for i in range(1):
        # if you allow diagonal path
        tt2=time.time()
        test_path_diagonal()
        tt3=time.time()-tt2
        T3+=tt3  # "With Diagonal Path"

        # test path
        tt=time.time()
        test_path()
        tt1=time.time()-tt
        T1+=tt1  # "Without Diagonal Path"

    
    print("Without Diagonal:  " + str(T1))
    print("With Diagonal:  " + str(T3))