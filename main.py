import time
import random
import matplotlib.pyplot as plt

from algoritmos.bubble_sort import bubble_sort
from algoritmos.counting_sort import counting_sort
from algoritmos.merge_sort import merge_sort
from algoritmos.quick_sort import quick_sort

def generate_random_array(size):
    return [random.randint(0, 1000) for _ in range(size)]

input = [10**3, 10**4, 10**5, 10**6]
algoritmos = { 'Merge Sort': merge_sort, 'Quick Sort': quick_sort, 'Counting Sort': counting_sort}
timings = {alg: [] for alg in algoritmos}

print('Aguarde...\n'+
      'Executando comparação...')

for i in input:
    arr = generate_random_array(i)
    for alg_name, alg_func in algoritmos.items():
        start_time = time.time()
        alg_func(arr.copy())
        end_time = time.time()
        timings[alg_name].append(end_time - start_time)

print('-----> Comparação executada com sucesso <-----')

for alg_name, timing in timings.items():
    plt.plot(input, timing, label = alg_name)

plt.xlabel('Tamanho da Entrada')
plt.ylabel('Tempo (s)')
plt.title('Comparação de Tempo dos Algoritmos de Ordenação')
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.show()
