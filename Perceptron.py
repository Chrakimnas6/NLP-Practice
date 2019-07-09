class Perceptron(Object):
    def __init__(self, input_num, activator_fun):
        self.activator = activator_fun
        self.weights = [0,0] * input_num
        self.bias = 0.0
        print("initial weight:{0}， bias:{1}".format(self.weights, self.bias))

    def __str__(self):
        return 'weights: {0} ' \
            'bias: {1}n'.format(self.weights, self.bias)

    def predict(self, input_vec):
        
