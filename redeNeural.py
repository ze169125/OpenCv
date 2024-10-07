import numpy as np

class RedeNeural(objeto):
  def __init__(self, camadas):
    self.num_camadas = len(camadas)
    self.camadas = camadas
    self.vies = [np.random.randn(y, 1) for y in camadas[1:]]
    self.pesos = [np.random.randn(y, x) 
                    for x, y in zip(camadas[:-1], camadas[1:])]
  def sigmoid(z):#z pode ser valor ou vetor
    return 1.0/(1.0+np.exp(-z))

  def feedforward(self, a):
      """Retorna o resultado calculado de uma rede neural "self" com o input "a"."""
      for b, w in zip(self.vies, self.pesos):
          a = sigmoid(np.dot(w, a)+b)
      return a

  def SGD(self, dados_treinamento, rounds, mini_batch_size, eta,
          dados_teste=None):
      """Train the neural network using mini-batch stochastic
      gradient descent.  The "training_data" is a list of tuples
      "(x, y)" representing the training inputs and the desired
      outputs.  The other non-optional parameters are
      self-explanatory.  If "test_data" is provided then the
      network will be evaluated against the test data after each
      epoch, and partial progress printed out.  This is useful for
      tracking progress, but slows things down substantially."""
      if test_data: n_test = len(test_data)
      n = len(training_data)
      for j in xrange(epochs):
          random.shuffle(training_data)
          mini_batches = [
              training_data[k:k+mini_batch_size]
              for k in xrange(0, n, mini_batch_size)]
          for mini_batch in mini_batches:
              self.update_mini_batch(mini_batch, eta)
          if test_data:
              print "Epoch {0}: {1} / {2}".format(
                  j, self.evaluate(test_data), n_test)
          else:
              print "Epoch {0} complete".format(j)
