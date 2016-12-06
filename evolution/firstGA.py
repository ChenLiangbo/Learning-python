#!usr/bin/env/python 
# -*- coding: utf-8 -*-

from pyevolve import G1DList
from pyevolve import GSimpleGA
def eval_func(chromosome):
    score = 0.0
    # iterate over the chromosome
    for value in chromosome:
        if value==0:
            score += 1
    return score


genome = G1DList.G1DList(10)
genome.evaluator.set(eval_func)
ga = GSimpleGA.GSimpleGA(genome)
ga.evolve(freq_stats=20)
print ga.bestIndividual()