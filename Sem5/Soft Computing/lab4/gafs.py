import numpy as np
import nb
import matplotlib.pyplot as plt
import pandas as pd
import time

x = nb.df_spect.drop(['Class'], axis=1)
y = nb.df_spect['Class']

class GAFS():

    def __init__(self,cross_rate=0.25,mutation_rate = 0.1, iterations=80, pool_size = 30):
        self.mutation_rate = mutation_rate
        self.iterations = iterations
        self.pool_size = pool_size
        self.pool = np.array([])
        self.iterations_results = {}
        self.cross_rate=cross_rate

    def results(self):
        return (self.pool[0], [idx for idx, gene in enumerate(self.pool[0]) if gene==1])


    def plot_progress(self):
        avs = [np.mean(self.iterations_results[str(x)]['scores']) for x in range(1,self.iterations+1)]
        avs0 = [np.mean(self.iterations_results[str(x)]['scores'][0]) for x in range(1,self.iterations+1)]
        plt.plot(avs, label='Pool Average Score')
        plt.plot(avs0, label='Best Solution Score')
        plt.legend()
        plt.show()
    

    def fit(self, evaluate, X, y, verbose=True):

        self.__init__(self.mutation_rate, self.iterations, self.pool_size)
        
        self.pool = np.random.randint(0,2,(self.pool_size, X.shape[1]))

        for iteration in range(1,self.iterations+1):
            s_t = time.time()
            scores = list(); fitness = list(); 
            for chromosome in self.pool:
                chosen_idx = [idx for gene, idx in zip(chromosome, range(X.shape[1])) if gene==1]

                adj_X = X.iloc[:,chosen_idx]
                nb.features = adj_X.columns
                adj_X = adj_X.join(y)
                score = evaluate(adj_X, 10)
                scores.append(score)
            fitness = [x/sum(scores) for x in scores]

            fitness, self.pool, scores = (list(t) for t in zip(*sorted(zip(fitness, [list(l) for l in list(self.pool)], scores),reverse=True)))
            self.iterations_results['{}'.format(iteration)] = dict()
            self.iterations_results['{}'.format(iteration)]['fitness'] = fitness
            self.iterations_results['{}'.format(iteration)]['pool'] = self.pool
            self.iterations_results['{}'.format(iteration)]['scores'] = scores

            self.pool = np.array(self.pool)

            if iteration != self.iterations+1:
                new_pool = []
                for chromosome in self.pool[1:int((len(self.pool)/2)+1)]:
                    random_split_point = np.random.randint(1,len(chromosome))
                    next_gen1 = np.concatenate((self.pool[0][:random_split_point], chromosome[random_split_point:]), axis = 0)
                    next_gen2 = np.concatenate((chromosome[:random_split_point], self.pool[0][random_split_point:]), axis = 0)
                    for idx, gene in enumerate(next_gen1):
                        if np.random.random() < self.mutation_rate:
                            next_gen1[idx] = 1 if gene==0 else 0
                    for idx, gene in enumerate(next_gen2):
                        if np.random.random() < self.mutation_rate:
                            next_gen2[idx] = 1 if gene==0 else 0
                    new_pool.append(next_gen1)
                    new_pool.append(next_gen2)
                self.pool = new_pool
            else:
                continue
            if verbose:
                if iteration % 10 == 0:
                    e_t = time.time()
                    print('Iteration {} Complete [Time Taken For Last Iteration: {} Seconds]'.format(iteration,round(e_t-s_t,2)))

ga = GAFS()

ga.fit(nb.evaluate_algorithm, x, y)

ga.results()

ga.plot_progress()

