class Perceptron(object):
    def __init__(self, input_num, activator_fun):
        self.activator = activator_fun
        self.weights = [0,0] * input_num
        self.bias = 0.0
        print("initial weight:{0}， bias:{1}".format(self.weights, self.bias))

    def __str__(self):
        return 'weights: {0} ' \
            'bias: {1}n'.format(self.weights, self.bias)

    def predict(self, input_vec):
        zipped = list(zip(input_vec, self.weights))
        sum_total = sum(list(map(lambda x_y: x_y[0] * x_y[1], zipped)))
        return self.activator(sum_total + self.bias)

    def train(self, input_vecs, labels, iteration, rate):
        for i in range(iteration):
            self._one_interation(input_vecs, labels, rate)

    def _one_interation(self, input_vecs, labels, rate):
        samples = list(zip(input_vecs, labels))
        for (input_vec, label) in samples:
            output = self.predict(input_vec)
            self._update_weights(input_vec, output, label, rate)

    def _update_weights(self, input_vec, output, label, rate):
        print(input_vec, output, label, "rate", rate)
        delta = label - output
        self.weights = list(map(lambda x_w : rate * delta * x_w[0] + x_w[1], zip(input_vec, self.weights)))
        self.bias += rate * delta

def f_active_function(x):
        return 1 if x > 0 else 0


def get_training_dataset():
        input_vecs = [[1, 1], [0, 0], [1, 0], [0, 1]]
        labels = [1, 0, 0, 0]
        return input_vecs, labels

def train_and_perceptron():
        p = Perceptron(2, f_active_function)
        input_vecs, labels = get_training_dataset()
        p.train(input_vecs, labels, 10, 0.1)
        return p

if __name__ == '__main__':
    and_perceptron = train_and_perceptron()
    print(and_perceptron)
    print("input value{0}, predict:{1}".format([0, 0], and_perceptron.predict([0, 0])))
    print(and_perceptron.predict([1, 0]))
    print(and_perceptron.predict([0, 1]))
    print(and_perceptron.predict([1, 1]))