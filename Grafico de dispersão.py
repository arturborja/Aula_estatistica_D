mi=20
ni=10
print(mi+ni)

import numpy as np
import matplotlib.pyplot as plt

def grafic20():
  

    x = np.array([3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 8])
    mu = np.sum(x/21)  # média
    sigma = np.std(x) #dp
    y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma)**2)

    plt.plot(x, y)
    plt.xlabel('Valores')
    plt.ylabel('Densidade')
    plt.title('Distribuição Normal')
    plt.grid(True)
    plt.show()
    print(mu)
    print(sigma)

# Chamar a função para exibir o gráfico
grafic20()

