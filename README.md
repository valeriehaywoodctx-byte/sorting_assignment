# Advanced Algorithmic Suite: Network Flow & Optimization

This repository contains a comprehensive collection of advanced algorithms implemented as part of my Data Structures and Algorithms coursework. The primary focus is on **Network Flow Theory** and its real-world applications.

## 🚀 Week 10: Network Flow Solvers
I implemented three core solvers from scratch to manage flow through capacity-constrained directed graphs:
* **Edmonds-Karp:** A BFS-based implementation of the Ford-Fulkerson method.
* **Push-Relabel:** A local-search optimization using height-based preflow.
* **Min-Cost Max-Flow:** Optimization for both volume and cost (latency/weight).

### 🛠️ Real-World Applications
The solvers were used to demonstrate algorithmic reductions for:
1.  **Bipartite Matching:** Optimal assignment of entities under constraints.
2.  **Image Segmentation:** Using the **Max-Flow Min-Cut Theorem** to separate foreground and background data.
3.  **Resource Scheduling:** Feasibility analysis for multi-agent workload distribution.

## 📊 Performance Analysis
The project includes a benchmarking suite (`week10_flow_benchmark.py`) that compares the scaling properties of Edmonds-Karp vs. Push-Relabel on networks up to 300 nodes.

## 📁 Repository Structure
* `src/flow/core/`: The mathematical engines (Solvers).
* `src/flow/applications/`: Reductions to practical problems.
* `src/flow/visualization/`: Graph plotting using Matplotlib and NetworkX.
* `results/`: Performance graphs and visual outputs.