from __future__ import print_function
from game import sd_peers, sd_spots, sd_domain_num, init_domains, \
    restrict_domain, SD_DIM, SD_SIZE
import random, copy
class AI:
    def __init__(self):
        self.stack = []

    def solve(self, problem):
        domains = init_domains()
        restrict_domain(domains, problem)

        # TODO: implement backtracking search. 
        while True:

            if self.propagate(domains): #report no conflict
                flag = True
                for spot in sd_spots:
                    if len(domains[spot]) != 1:
                        flag = False
                        break
                if flag == True: #if len(domains[spot]) = 1 for all spots, this is a consistent assignment
                    return domains

                orig_domains = copy.deepcopy(domains)
                spot, num = self.search(domains)
                self.stack.append((spot, num, orig_domains))
            else:
                #if stack is empty, there is no consistent assignment
                if len(self.stack) == 0:
                    return domains
                domains = self.backtrack(self.stack, domains)
            


        # TODO: delete this block ->
        # Note that the display and test functions in the main file take domains as inputs. 
        #   So when returning the final solution, make sure to take your assignment function 
        #   and turn the value into a single element list and return them as a domain map. 
        # for spot in sd_spots:
        #     domains[spot] = [1]
        # return domains
        # <- TODO: delete this block

    # TODO: add any supporting function you need

    def propagate(self, domains):
        flag = True
        while flag:
            flag = False
            for spot in sd_spots:
                if len(domains[spot]) == 1:
                    for peer in sd_peers.get(spot):
                        if domains[spot][0] in domains[peer]:
                            domains[peer].remove(domains[spot][0])
                            flag = True
                if len(domains[spot]) == 0:
                    return False
        return True

    def search(self, domains):
        dictionary = {}
        smallest_value = 100
        smallest_spot = None
        for spot in sd_spots:
            dictionary[spot] = len(domains[spot])
        for spot in sd_spots:
            if dictionary[spot] == 1:
                continue
            if dictionary[spot] < smallest_value:
                smallest_value = dictionary[spot]
                smallest_spot = spot

        min_domains = domains[smallest_spot]
        num = min_domains[len(min_domains)-1] #a possible num for spot
        for i in range(len(domains[smallest_spot])):
            if i == 0:
                continue
            domains[smallest_spot].pop(0)
        return smallest_spot, num
        
        

    def backtrack(self, stack, domains):
        spot, num, orign_domains = self.stack.pop(0)
        domains = orign_domains
        domains[spot].remove(num)
        return domains


















    #### The following templates are only useful for the EC part #####

    # EC: parses "problem" into a SAT problem
    # of input form to the program 'picoSAT';
    # returns a string usable as input to picoSAT
    # (do not write to file)
    def sat_encode(self, problem):
        text = ""

        # TODO: write CNF specifications to 'text'

        return text

    # EC: takes as input the dictionary mapping 
    # from variables to T/F assignments solved for by picoSAT;
    # returns a domain dictionary of the same form 
    # as returned by solve()
    def sat_decode(self, assignments):
        # TODO: decode 'assignments' into domains
        
        # TODO: delete this ->
        domains = {}
        for spot in sd_spots:
            domains[spot] = [1]
        return domains
        # <- TODO: delete this
