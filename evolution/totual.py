#!usr/bin/env/python 
# -*- coding: utf-8 -*-

from pyevolve import G1DList
from pyevolve import GSimpleGA
from pyevolve import Selectors
from pyevolve import Statistics
from pyevolve import DBAdapters
from pyevolve import Util
from pyevolve import Interaction

# This function is the evaluation function, we want
# to give high score to more zero'ed chromosomes
def eval_func(genome):
    # print ("----eval_func-----",type(genome),dir(genome))
    score = 0.0

    # iterate over the chromosome
    # The same as "score = len(filter(lambda x: x==0, genome))"
    for value in genome:
        if value==0:
            score += 1
    # print ('-'*80,)
    return score

def run_main():
    # Genome instance, 1D List of 50 elements
    # l = range(0,10)
    # print ("l = ",l)
    # Util.listSwapElement(l, 1, 2)
    # print ("l = ",l)    
    genome = G1DList.G1DList(50)
    print ("genome",type(genome),dir(genome))
    # Sets the range max and min of the 1D List
    genome.setParams(rangemin=0, rangemax=10)

    # The evaluator function (evaluation function)
    genome.evaluator.set(eval_func)
    # genome.evaluator.set(eval_func1)
    # genome.evaluator.add(eval_func2)

    # Genetic Algorithm Instance
    ga = GSimpleGA.GSimpleGA(genome)

    # Set the Roulette Wheel selector method, the number of generations and
    # the termination criteria
    ga.selector.set(Selectors.GRouletteWheel)
    ga.setGenerations(5)
    ga.terminationCriteria.set(GSimpleGA.ConvergenceCriteria)

    # Sets the DB Adapter, the resetDB flag will make the Adapter recreate
    # the database and erase all data every run, you should use this flag
    # just in the first time, after the pyevolve.db was created, you can
    # omit it.
    
    # dbadapter = DBSQLite(identify="test", resetDB=True)
    sqlite_adapter = DBAdapters.DBSQLite(identify="ex1", resetDB=True)
    ga.setDBAdapter(sqlite_adapter)

    csv_adapter = DBAdapters.DBFileCSV(identify="run1", filename="secondStats.csv")
    # adapter = DBFileCSV(filename="file.csv", identify="run_01",frequency = 1, reset = True
    ga.setDBAdapter(csv_adapter)

    urlpost_adapter = DBAdapters.DBURLPost("http://120.26.105.20:3821/login/", identify="run1", frequency=10)
    ga.setDBAdapter(urlpost_adapter)
    # Do the evolution, with stats dump
    # frequency of 20 generations
    ga.evolve(freq_stats=2)
    print dir(ga)

    
    # population = ga.getPopulation()
    # lst = Interaction.getPopScores(population)
    # Interaction.plotHistPopScore(population)
    # Interaction.plotPopScore(population)

    # adapter = ga.getAdapter()


    # Best individual
    print ga.bestIndividual()

if __name__ == "__main__":
    run_main()