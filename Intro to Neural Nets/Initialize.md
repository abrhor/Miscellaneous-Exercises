Code Explanation

Biases: Get a (n,1) vector of biases for nodes in 2nd and another one for output layer.

Weights:  Get an ndarray (vector) of weights for input and 2nd layer. Example: The input layer has 3 nodes, and the second layer has 2 nodes, so our first matrix will be of dimensions 2 x 3. This creates a column of weights for each of the inputs, and a row for each node in the next layer, with M[1,1] being the weight for the synapse between the first input and the first node of the second layer, M[1,2] Being the weight for the synapse between the second input and the first node of the second layer, and M[2,1] being the weight for the synapse between the first input and the second node of the second layer.
