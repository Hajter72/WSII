import numpy as np
import matplotlib.pyplot as plt

class Neuron:
    def __init__(self, n_inputs, bias=0., weights=None):
        self.b = bias
        if weights:
            self.ws = np.array(weights)
        else:
            self.ws = np.random.rand(n_inputs)

    def _f(self, x):  
        return max(x * .1, x)

    def _f_prime(self, x):  
        return 1. if x > 0 else .1

    def __call__(self, xs):  
        self.last_input = xs
        return self._f(xs @ self.ws + self.b)

    def backward(self, delta, learning_rate):
        self.ws -= learning_rate * delta * self.last_input
        self.b -= learning_rate * delta
        return delta * self.ws * self._f_prime(self.last_input)


class Layer:
    def __init__(self, n_inputs, n_neurons):
        self.neurons = [Neuron(n_inputs) for _ in range(n_neurons)]

    def __call__(self, xs):
        return np.array([neuron(xs) for neuron in self.neurons])

    def backward(self, delta, learning_rate):
        return sum(neuron.backward(d, learning_rate) for neuron, d in zip(self.neurons, delta))


class NeuralNetwork:
    def __init__(self):
        self.layers = [
            Layer(3, 4), 
            Layer(4, 4),  
            Layer(4, 4),  
            Layer(4, 1)  
        ]

    def __call__(self, xs):
        for layer in self.layers:
            xs = layer(xs)
        return xs

    def mse(self, y_true, y_pred):  # mean squared error
        return np.mean((y_true - y_pred) ** 2)

    def mse_prime(self, y_true, y_pred):  # derivative of mean squared error
        return 2 * (y_pred - y_true) / y_true.size

    def train(self, X_train, y_train, epochs, learning_rate):
        for i in range(epochs):
            err = 0
            for x, y_true in zip(X_train, y_train):
                # forward pass
                output = self(x)
                err += self.mse(y_true, output)

                # backward pass
                delta = self.mse_prime(y_true, output)
                for layer in reversed(self.layers):
                    delta = layer.backward(delta, learning_rate)

            # print out the mean squared error over the epoch
            print('epoch %d/%d, mse=%.6f' % (i+1, epochs, err / len(X_train)))


nn = NeuralNetwork()

xs = np.array([0.1, 0.2, 0.3])

output = nn(xs)

classification = 1 if output > 0.5 else 0
print(classification)




def draw_neural_net(ax, left, right, bottom, top, layer_sizes, layer_colors):
    n_layers = len(layer_sizes)
    v_spacing = (top - bottom) / float(max(layer_sizes))
    h_spacing = (right - left) / float(len(layer_sizes) - 1)
    # Nodes
    for n, layer_size in enumerate(layer_sizes):
        layer_top = v_spacing * (layer_size - 1) / 2. + (top + bottom) / 2.
        for m in range(layer_size):
            circle = plt.Circle((n * h_spacing + left, layer_top - m * v_spacing), v_spacing / 4.,
                                color=layer_colors[n], ec='k', zorder=4)
            ax.add_artist(circle)
    for n, (layer_size_a, layer_size_b) in enumerate(zip(layer_sizes[:-1], layer_sizes[1:])):
        layer_top_a = v_spacing * (layer_size_a - 1) / 2. + (top + bottom) / 2.
        layer_top_b = v_spacing * (layer_size_b - 1) / 2. + (top + bottom) / 2.
        for m in range(layer_size_a):
            for o in range(layer_size_b):
                line = plt.Line2D([n * h_spacing + left, (n + 1) * h_spacing + left],
                                  [layer_top_a - m * v_spacing, layer_top_b - o * v_spacing], c='k')
                ax.add_artist(line)

layer_colors = ['red', 'blue', 'blue', 'green']
fig = plt.figure(figsize=(20, 20))
ax = fig.gca()
ax.axis('off')
draw_neural_net(ax, .2, .8, .2, .8, [3, 4, 4, 1], layer_colors)
plt.show()
