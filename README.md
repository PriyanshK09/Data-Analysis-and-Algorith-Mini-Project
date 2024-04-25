# Data-Analysis-and-Algorith-Mini-Project
----------------------------------------------
# Network Flow Optimization for Task Allocation

This mini project implements a network flow optimization algorithm for task allocation in a graph. It uses Dijkstra's algorithm to find the shortest path in the graph and allocates tasks based on flow requirements, deadlines, and uncertainty.

## How It Works

1. **Graph Representation**: The project uses a graph data structure to represent nodes, edges, distances between nodes, and intervals for each edge.

2. **Dijkstra's Algorithm**: It utilizes Dijkstra's algorithm to find the shortest path from the source node 's' to the destination node 'd' in the graph.

3. **Task Allocation**: 
   - Tasks are represented with flow requirements and deadlines.
   - Shortest paths are found for each task using Dijkstra's algorithm.
   - Tasks are allocated to paths based on their flow requirements and deadlines.
   - If a task cannot be allocated in the remaining paths, it is marked as unallocated.

4. **Uncertainty Calculation**:
   - For unallocated tasks, uncertainty is calculated based on the flow, interval, and allocation in each path.
   - Tasks are allocated to paths with lower uncertainty first, if possible.

5. **Graph Update**: The graph is updated after each task allocation by reducing the edge distances based on the remaining flow for each task.

## Components

- **Graph Class**: Represents the graph with nodes, edges, distances, and intervals.
- **Dijkstra's Algorithm Functions**: Find the shortest path in the graph.
- **Task Allocation Functions**: Allocate tasks to paths based on flow requirements and deadlines.
- **Uncertainty Calculation Functions**: Calculate uncertainty for unallocated tasks and allocate tasks based on lower uncertainty values.

## Usage

1. Initialize a graph with nodes, edges, distances, and intervals.
2. Use Dijkstra's algorithm to find the shortest path for each task.
3. Allocate tasks to paths based on flow requirements and deadlines.
4. Update the graph and allocate remaining tasks based on uncertainty.

## Dependencies

- Python 3.x

## Future Improvements

- Add more robust error handling and input validation.
- Optimize the algorithm for larger graphs and tasks.
- Improve the user interface for better interaction.

## Contribution

Contributions are welcome! Feel free to fork the project and submit pull requests for improvements.
