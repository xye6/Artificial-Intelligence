
# coding: utf-8

# ## Part II: Advanced Propositional Inference

# In[1]:

class Stack:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []

    def push(self, item):
         self.items.append(item)

    def pop(self):
         return self.items.pop()

    def peek(self):
         return self.items[len(self.items)-1]

    def size(self):
         return len(self.items)
        
class BinaryTree:
    
    def __init__(self, root_val):
        self.key = root_val
        self.left_child = None
        self.right_child = None
        
    def insert_left(self, new_valiable):
        if self.left_child == None:
            self.left_child = BinaryTree(new_valiable)
        else:
            t = BinaryTree(new_valiable)
            t.left_child = self.left_child
            self.left_child = t
            
    def insert_right(self, new_valiable):
        if self.right_child == None:
            self.right_child = BinaryTree(new_valiable)
        else:
            t = BinaryTree(new_valiable)
            t.right_child = self.right_child
            self.right_child = t
            
    def get_right_child(self):
        return self.right_child
    
    def get_left_child(self):
        return self.left_child
    
    def set_root_val(self, obj):
        self.key = obj
        
    def get_root_val(self):
        return self.key
        
class sentence:

    def __init__(self,data):
        self.tree = None
        self.symbols = {}
        self.value = data
      
    def build_parse_tree(self):
        sentence_list = self.value.split()
        for i in range(len(sentence_list)):
            symb = sentence_list[i]
            if symb not in ['('," ",')','|','!']:
                if symb not in self.symbols:
                    if sentence_list[i-1] != '!':
                        self.symbols[symb] = 1     
                    elif sentence_list[i-1] == '!':
                        self.symbols[symb] = 2     
                    
        tree_stack = Stack()
        bina_tree = BinaryTree("")
        tree_stack.push(bina_tree)
        curr_tree = bina_tree

        for i in sentence_list:
            if i == "(":
                curr_tree.insert_left("")
                tree_stack.push(curr_tree)
                curr_tree = curr_tree.get_left_child()
            elif i == " ":
                pass
            elif (i == "|"):
                curr_tree.set_root_val(i)
                curr_tree.insert_right("")
                tree_stack.push(curr_tree)
                curr_tree = curr_tree.get_right_child()
            elif i == "!":
                curr_tree = tree_stack.pop()
                curr_tree.set_root_val(i)
                curr_tree.insert_right("")
                tree_stack.push(curr_tree)
                curr_tree=curr_tree.get_right_child()
            elif i == ")":
                curr_tree = tree_stack.pop()
            else:
                curr_tree.set_root_val(i)
                parent = tree_stack.pop()
                curr_tree = parent

        self.tree = bina_tree


# In[2]:


def judge_T_F(parse_tree,model):

    tmp_left = parse_tree.get_left_child()
    tmp_right = parse_tree.get_right_child()

    if parse_tree.get_root_val() == "!":
        if judge_T_F(tmp_right,model) == None:
            return None
        else:
            return not judge_T_F(tmp_right,model)
    elif tmp_left and tmp_right:
        op = parse_tree.get_root_val()
        if op == "&":
            return judge_T_F(tmp_left,model) and judge_T_F(tmp_right,model)
        else:
            left_result = judge_T_F(tmp_left,model)
            right_result = judge_T_F(tmp_right,model)
            if ((left_result == None and right_result == False) or 
                (left_result == False and right_result == None)):
                    return None
            else:
                return left_result or right_result
    else:
        if parse_tree.get_root_val() not in model:
            return None
        else:
            return model[parse_tree.get_root_val()]


def satisfactory(KB):

    total_symbols = []
    for clause in KB:
        for key in clause.symbols:
            if key not in total_symbols:
                total_symbols.append(key)
    
    return dpll(KB,total_symbols,{})
        
def pl_true(clause,model):
    return judge_T_F(clause.tree,model)


def dpll(KB,total_symbols,model):
    
    unknown_clause = []
    
    for c in KB:
        result = pl_true(c,model)
        if result == False:
            return False
        if result != True:
            unknown_clause.append(c)
    if len(unknown_clause) == 0:
        return True
    
    # to find pure symbol
    p,value = find_pure_symbol(total_symbols,unknown_clause)
    if p:

        new_total_symbols = []
        new_total_symbols.extend(total_symbols)
        new_total_symbols.remove(p)
        return dpll(KB,new_total_symbols,dict(model,**{p:value}))
    
    # to find a unit clause
    p,value = find_unit_clause(total_symbols,unknown_clause)
    if p:
        new_total_symbols = []
        new_total_symbols.extend(total_symbols)
        new_total_symbols.remove(p)
        return dpll(KB,new_total_symbols,dict(model,**{p:value}))
    
    # try normal search
    p = total_symbols.pop()
    return (dpll(KB,total_symbols,dict(model,**{p:True})) or 
                dpll(KB,total_symbols,dic(model,**{p:False})))
    

def find_pure_symbol(total_symbols,clause):
    
    for p in total_symbols:
        find_true, find_false = False, False
        for c in clause:
            if p in c.symbols:
                if not find_true and c.symbols[p] == 1:
                    find_true = True
                if not find_false and c.symbols[p] == 2:
                    find_false = True
        if find_true != find_false:
            return p, find_true
        
    return None,None


def find_unit_clause(total_symbols,clause):
    
    for c in clause:
        find_symbols = 0
        for symbol in c.symbols:
            if symbol in total_symbols:
                find_symbols += 1
                if c.symbols[symbol] == 1:
                    p = symbol
                    val = True
                else:
                    p = symbol
                    val = False
        if find_symbols == 1:
            return p,val
    return None,None

def model_check(s_KB,s_check):
    KB=[]
    for i in range(len(s_KB)):

        s = sentence(s_KB[i])
        s.build_parse_tree()
        KB.append(s)

    s_negative = "( ! " + s_check[0] + " )"
    s = sentence(s_negative)
    s.build_parse_tree()
    KB.append(s)
    result1 = satisfactory(KB)
    KB.pop()

    s = sentence(s_check[0])
    s.build_parse_tree()
    KB.append(s)
    result2 = satisfactory(KB)
    KB.pop()

#     print(s_check[0])
    if result1 != result2:
        print("{0} : {1}".format(s_check[0],result2))
        
    else:
        print("{0} : not sure".format(s_check[0])) 
        
    #print('\n')


# ## Sample problem

# ### Q1

# In[3]:

s_KB=['P',
      '( ( ! P ) | Q )']

s_check=['Q']

print('Question1:')
model_check(s_KB,s_check)
print('\n')


# ### Q2

# In[4]:

s_KB=['( ! P11 )',
    '( ( ! B11 ) | P12 | P21 )',
    '( ( ! P12 ) | B11 )',
    '( ( ! P21 ) | B11 )',
    '( ( ! B21 ) | P11 | P22 | P31 )',
    '( ( ! P11 ) | B21 )',
    '( ( ! P22 ) | B21 )',
    '( ( ! P31 ) | B21 )',
    '( ! B11 )',
    'B21']

s_check=['P12']

print('Question2:')
model_check(s_KB,s_check)
print('\n')


# ### Q3

# In[5]:

s_KB=['( ( ! MY ) | IM )',
    '( ( ! HO ) | MA )',
    '( MY | ( ! IM ) )',
    '( MY | MA )',
    '( ( ! IM ) | HO )',
    '( ( ! MA ) | HO )']

s_check1=['MY']
s_check2=['MA']
s_check3=['HO']

print('Question3:')
model_check(s_KB,s_check1)
model_check(s_KB,s_check2)
model_check(s_KB,s_check3)
print('\n')


# ### Q4

# #### (a)

# In[6]:

s_KB=['( ( ! A ) | C )',
    '( ( ! B ) | ( ! C ) )',
    '( C | B )',
    '( ( ( ! C ) | ( ! A ) ) | B )',
    '( ( ! B ) | C )',
    '( A | C )']

s_check1=['A']
s_check2=['B']
s_check3=['C']

print('Question4(a):')
model_check(s_KB,s_check1)
model_check(s_KB,s_check2)
model_check(s_KB,s_check3)
print('\n')


# #### (b)

# In[7]:

s_KB=['( ( ! A ) | ( ! C ) )',
    '( C | A )',
    '( ( ! B ) | A )',
    '( ( ! B ) | C )',
    '( ( ( ! A ) | ( ! C ) ) | B )',
    '( ( ! C ) | B )',
    '( ( ! B ) | C )']

s_check1=['A']
s_check2=['B']
s_check3=['C']

print('Question4(b):')
model_check(s_KB,s_check1)
model_check(s_KB,s_check2)
model_check(s_KB,s_check3)
print('\n')


# In[ ]:




# In[ ]:



