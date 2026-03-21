from src.flow.core.network import FlowNetwork
from src.flow.core.edmonds_karp import edmonds_karp

def segment_simple_image(pixel_intensities):
    """
    pixel_intensities: list of numbers (0-255) representing a row of pixels.
    We want to separate dark pixels (background) from light pixels (foreground).
    """
    fn = FlowNetwork()
    source = 'FOREGROUND'
    sink = 'BACKGROUND'
    
    # Thresholds for likelihood
    for i, val in enumerate(pixel_intensities):
        node = f"pix_{i}"
        
        # Connection to Source (Likelihood of being Foreground/Light)
        fn.add_edge(source, node, val)
        
        # Connection to Sink (Likelihood of being Background/Dark)
        fn.add_edge(node, sink, 255 - val)
        
        # Neighbors (Penalize cutting between similar adjacent pixels)
        if i < len(pixel_intensities) - 1:
            next_node = f"pix_{i+1}"
            # Penalty for separating these pixels is higher if they are similar
            penalty = 50 
            fn.add_edge(node, next_node, penalty)
            fn.add_edge(next_node, node, penalty)

    max_flow, flow_dict = edmonds_karp(fn, source, sink)
    
    # To find the 'Cut', we see which pixels are still reachable from Source
    # in the residual graph.
    segmented = []
    # Simplified reachability check for this example:
    for i in range(len(pixel_intensities)):
        node = f"pix_{i}"
        if fn.capacity[(source, node)] - flow_dict.get((source, node), 0) > 0:
            segmented.append("FG")
        else:
            segmented.append("BG")
            
    return segmented