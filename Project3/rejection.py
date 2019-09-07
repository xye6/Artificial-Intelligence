
# coding: utf-8

# In[100]:

import xml.dom.minidom
from xml.dom.minidom import parse
import random
import re
import time


def parse_xml(filename):

    DOMTree = xml.dom.minidom.parse(filename)
    collection = DOMTree.documentElement
    nodes = collection.getElementsByTagName("VARIABLE")
    
    bayes_net = []
    
    variables = {}
    
    # read variables
    for node in nodes:
        
        var = node.getElementsByTagName('NAME')[0].childNodes[0].data
        values = node.getElementsByTagName("OUTCOME")
        values_list = [i.childNodes[0].data for i in values]
        variables[var] = values_list
    
    nodes = collection.getElementsByTagName("DEFINITION")
    
    
    # read possibility distribution table
    for node in nodes:
        
        name = node.getElementsByTagName('FOR')[0].childNodes[0].data
        
        parents = node.getElementsByTagName("GIVEN")
        par_list = [i.childNodes[0].data for i in parents]
            
        table = node.getElementsByTagName("TABLE")
        
        p_table = {}
        
        for value in variables[name]:
            p_table[tuple([value])] = {}

        if len(par_list) == 0:
            p_numbers = table[0].childNodes[0].data.split()
            p_table[tuple(["true"])] = {():float(p_numbers[0])}
            p_table[tuple(["false"])] = {():float(p_numbers[1])}
        
        else: 
            for i in range(3,table[0].childNodes.length):
                exp = table[0].childNodes[i].data.split()
                if ((par_list[0]) in exp) or (("!"+par_list[0]) in exp):
                    par_comb = []
                    for string in exp:
                        if string.startswith("!"):
                            par_comb.append("false")
                        else:
                            par_comb.append("true")
                    par_comb = tuple(par_comb)
                else:
                    p_table[tuple(["true"])][par_comb] = float(exp[0])
                    p_table[tuple(["false"])][par_comb] = float(exp[1])

        bayes_net.append([name,variables[name],par_list,p_table])
    
    return bayes_net


def event_values(event, par_list):
    return tuple([event[i] for i in par_list])


# In[102]:

class Bayes_node:
    
    def __init__(self, var, values, parents, table):
        self.var = var
        self.values = values
        self.parents = parents
        self.cpt = table
        self.children = []
        
    def get_possibility(self, value, event):
        get_value = event_values(event, self.parents)
        return self.cpt[tuple([value])][get_value]


# In[103]:

class Bayes_DAG:
    
    def __init__(self, expressions):
        self.nodes = []
        self.variables = []
        total = len(expressions)
        give_node = {}
        for expression in expressions:
            give_node[tuple([expression[0]])] = False
            
        # construct DAG (make sure the variables order is right)
        while total > 0:
            for expression in expressions:
                if give_node[tuple([expression[0]])] == False:
                    result = self.add(expression)
                    if result == True:
                        give_node[tuple([expression[0]])] = True
                        total -= 1
        
            
    def add(self, expression):
        node = Bayes_node(*expression)
        if all((parent in self.variables) for parent in node.parents) == False:
            return False
        self.variables.append(node.var)
        self.nodes.append(node)
        for parent in node.parents:
            self.find_node(parent).children.append(node)
        return True
    
    def find_node(self, var):
        for node in self.nodes:
            if node.var == var:
                return node
            
    def find_values(self, var):
        return self.find_node(var).values



def normalize(result):
    result_sum = 0
    
    for i in result:
        result_sum += result[i]
    
    if result_sum == 0:
        print(result)
        return True
    
    for i in result:
        result[i] = result[i]/result_sum
        
    print(result)


# In[107]:

def generate_sampling(bn):
    
    sample = {}
    
    for var in bn.variables:
        var_node = bn.find_node(var)
        
        start = 0
        number = random.random()
        
        for value in bn.find_values(var):
            p = var_node.get_possibility(value,sample)
            start += p
            if number <= start:
                sample[var] = value
                break
            
    return sample


# In[108]:

def consistent(e, sample):
    return all(sample[k] == v for k,v in e.items())


# In[109]:

def rejection_sampling(var,e,bn,times):
    
    result = {}
    for value in bn.find_values(var):
        result[value] = 0
    
    for i in range(times):
        sample = generate_sampling(bn)
        if consistent(e, sample):
            result[sample[var]] += 1
            
    return normalize(result)


# In[110]:

while True:
    print("Please type the filename, the sampling times, the query variable and evidence variables in one line(if no more question, please type END)")
    line = input()
    if line == "END":
        break
    else:
        line = line.split(" ")
        filename = line[0]
        if filename.endswith("bif"):
            net_construct = parse_bif(filename)
        elif filename.endswith(".xml"):
            net_construct = parse_xml(filename)
        else:
            Raise
        
        bn = Bayes_DAG(net_construct)
        
        times = int(line[1])
        
        q_var = line[2]
        evidence = {}
        
        for i in range(3,len(line)):
            if line[i] in bn.variables:
                evidence[line[i]] = line[i+1]
            else:
                continue
    
    starttime = time.time()
    
    rejection_sampling(q_var,evidence,bn,times)
    
    endtime = time.time()
    
    print("time cost:%.2f"%(endtime-starttime))

