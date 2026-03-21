from src.flow.core.network import FlowNetwork
from src.flow.core.edmonds_karp import edmonds_karp
from src.flow.visualization.plot_network import draw_flow_network

def test_visual():
    fn = FlowNetwork()
    fn.add_edge('s', 'A', 10)
    fn.add_edge('s', 'B', 5)
    fn.add_edge('A', 't', 8)
    fn.add_edge('B', 't', 10)
    fn.add_edge('A', 'B', 2)

    max_f, flow_map = edmonds_karp(fn, 's', 't')
    
    print("Generating visualization...")
    draw_flow_network(fn, flow_map, title=f"Max Flow Result: {max_f}")

if __name__ == "__main__":
    test_visual()