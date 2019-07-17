class Perceptron(object):
    def __init__(self, input_num, activator_fun):
        self.activator = activator_fun
        self.weights = [0.0 for _ in range(input_num)]
        self.bias = 0.0
        print("initial weight:{0}， bias:{1}".format(self.weights, self.bias))

    def __str__(self):
        return 'weights: {0} ' \
            'bias: {1}'.format(self.weights, self.bias)

    def predict(self, input_vec):
        zipped = list(zip(input_vec, self.weights))
        sum_total = sum(list(map(lambda x_y: x_y[0] * x_y[1], zipped)))
        return self.activator(sum_total + self.bias)
    #训练到想要的次数
    def train(self, input_vecs, labels, iteration, rate):
        for _ in range(iteration):
            self._one_interation(input_vecs, labels, rate)
    #每一次的训练
    def _one_interation(self, input_vecs, labels, rate):
        samples = list(zip(input_vecs, labels)) #将输入矩阵和标签一一对应起来
        for (input_vec, label) in samples:
            output = self.predict(input_vec) #得到现阶段预测的值
            self._update_weights(input_vec, output, label, rate) #更新权重

    def _update_weights(self, input_vec, output, label, rate):
        print(input_vec, output, label, "rate", rate)
        delta = label - output #实际标签值 - 预测得到的值
        #更新权重，将输入矩阵和目前的权重对应打包，根据公式更新
        self.weights = list(map(lambda x_w : rate * delta * x_w[0] + x_w[1], zip(input_vec, self.weights)))
        self.bias += rate * delta
        print(self.weights)
        print (self.bias)

def f_active_function(x):
        return 1 if x > 0 else 0


def get_training_dataset():
        input_vecs = [[1, 1], [0, 0], [1, 0], [0, 1]]
        labels = [1, 0, 0, 0]
        return input_vecs, labels

def train_and_perceptron():
        p = Perceptron(2, f_active_function) # 输入参数个数为2，自己设置的激活函数
        input_vecs, labels = get_training_dataset() #训练数据，向量和label
        p.train(input_vecs, labels, 10, 0.1) # 开始训练，一共迭代十次，学习速率为0.1
        return p

if __name__ == '__main__':
    and_perceptron = train_and_perceptron()
    print("Training finished, we are good to go!")
    print(and_perceptron)
    print("input value{0}, predict:{1}".format([0, 0], and_perceptron.predict([0, 0])))
    print(and_perceptron.predict([1, 0]))
    print(and_perceptron.predict([0, 1]))
    print(and_perceptron.predict([1, 1]))