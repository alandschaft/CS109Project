# Visualizing MetaMap and MedEx tag connections

We use NetworkX library in Python to draw the connections between the tags in two datasets. Each tag is treated as a node, and each time a MedEx tag and a MetaMap tag appears on the same row, it counts as one connection (edge) between the two tags (nodes). We are not discussing the connections within the MetaMap tag group or the MedEx tag group here.

We also set a threshold parameter. Only when the percentage of total connections between a MetaMap tag and MedEx tag among all connections of this MedEx tag exceeds a certain number (default is 10% here), it is shown in the visualization. Nodes that are not connected to any other nodes are not shown in the graph.

There are many identical tags (same drugs) in both MetaMap and MedEx datasets. Since the connections between the identical tags do not provide much new information, they are excluded in calculation.

By examining the interactive diagram connection shown, we can see that the connected MedEx and MetaMao tags are highly relevant.

(Nodes that are not connected to any other nodes are not shown)