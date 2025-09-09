import random
import numpy as np

class A1:
    def __init__(self):
        self.potential_state = None
        self.trans_matrix = None
        
    def generate_markov_chain(self, potential_state, seq_state):
        self.potential_state = potential_state
        state_count = len(self.potential_state)
               
        seq_state_idx = []
        for seq in seq_state:
            state = self.potential_state.index(seq)
            seq_state_idx.append(state)
            
        # Generate transition matrix
        # Case 1: Invalid Input
        if len(seq_state) < 2 or len(potential_state) < 2: 
            return np.zeros((0,0))
        
        # Case 2: regular input
        trans_count = np.zeros((state_count, state_count), dtype=float)
        cur = seq_state_idx[:-1]
        nxt = seq_state_idx[1:]
        
        np.add.at(trans_count, (cur, nxt), 1.0)
        row_sums = trans_count.sum(axis=1, keepdims=True)
        
        with np.errstate(divide='ignore', invalid='ignore'):
            trans_matrix = np.divide(trans_count, row_sums, out=np.zeros_like(trans_count), where=row_sums>0)

        self.trans_matrix = trans_matrix
        return trans_matrix
    
    
    def generate_samples(self, first_state, seed, length):
        # 1st state generated in idx 
        first_state_idx = self.potential_state.index(first_state)
        state_count = len(self.potential_state)
        
        # Trans_Matrix into Trans_Range
        trans_range = np.zeros((state_count, state_count), dtype=float)
        for i, prob_rows in enumerate(self.trans_matrix):
            added = 0
            for j, prob in enumerate(prob_rows):
                added_prob = prob + added
                trans_range[i][j] = added_prob
                added += prob
        print("trans_range\n", trans_range)  
              
        # random number generation using seed 
        generated_num = []
        
        random.seed(seed)
        for i in range(length):
            state = random.random()
            generated_num.append(state)
        print("generated_num\n", generated_num)
        
        # Check inclusion of the generated numbers in sequence
        generated_seq = [first_state_idx]
        for i, num in enumerate(generated_num):
            nxt_state = int(np.searchsorted(trans_range[generated_seq[-1]], num, side='right'))
            generated_seq.append(nxt_state)
        print("generated_seq\n",generated_seq)
        
        generated_states = []        
        for i in generated_seq:
            generated_states.append(self.potential_state[i])
    
        return generated_states


    def stationary_distribution(self):
        # transpose of transition matrix
        transition_matrix = self.trans_matrix
        vals, vecs = np.linalg.eig(transition_matrix.T)
        
        # closest finding eigenval close to 1 
        i = np.argmin(np.abs(vals - 1))
        stationary = np.real(vecs[:, i])
        stationary = stationary / stationary.sum()
        
        return stationary


potential_state = ['A','B','C']
seq_state = ['A','B','A','C','B','B','C','B']
# # potential_state = ["left", "right"]
# # seq_state = ["left", "right", "left", "left", "left", "right", "right", "left", "right", "right"]
a = A1()
a.generate_markov_chain(potential_state, seq_state)
print(a.generate_samples(potential_state[2], 13, 8))
print(a.stationary_distribution())