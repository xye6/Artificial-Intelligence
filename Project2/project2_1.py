
# coding: utf-8

# ## Part I: Basic Model Checking

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
        
    def insert_left(self, new_val):
        if self.left_child == None:
            self.left_child = BinaryTree(new_val)
        else:
            t = BinaryTree(new_val)
            t.left_child = self.left_child
            self.left_child = t
            
    def insert_right(self, new_val):
        if self.right_child == None:
            self.right_child = BinaryTree(new_val)
        else:
            t = BinaryTree(new_val)
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
        self.symbols = []
        self.words = data
    
    # represent sentence in parse tree
    def build_parse_tree(self):
        sentence_list = self.words.split()
        tree_stack = Stack()
        b_tree = BinaryTree("")
        tree_stack.push(b_tree)
        curr_tree = b_tree

        for i in sentence_list:
            if i == "(":
                curr_tree.insert_left("")
                tree_stack.push(curr_tree)
                curr_tree = curr_tree.get_left_child()
            elif i == " ":
                pass
            elif (i == "&" or i == "|" or i == "=>" or i == "<=>" ):
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
                if i not in self.symbols:
                    self.symbols.append(i)

        self.tree = b_tree

        
def pl_true(sentence,model):   
    # to check whether the model makes the sentence true
    for i in sentence:
        if judge_T_F(i.tree,model)==False:
            return False
    return True

def tt_entails(KB,alpha):
    symbols_list = []
    for i in KB:
        for j in i.symbols:
            if j not in symbols_list:
                symbols_list.append(j)
                
    return tt_check_all(KB,alpha,symbols_list,{})

def tt_check_all(KB,alpha,symbols_list,model):
    if not symbols_list:
        if pl_true(KB,model):
            #print(model)
            return pl_true(alpha,model)
        else:
            return True
    
    else:
        p,rest = symbols_list[0],symbols_list[1:]
        # assign True/False to every symbol in order to generate all possible models
        return tt_check_all(KB,alpha,rest,dict(model,**{p:True})) and tt_check_all(KB,alpha,rest,dict(model,**{p:False}))
              

def judge_T_F(parse_tree,model):
    
    tmp_left = parse_tree.get_left_child()
    tmp_right = parse_tree.get_right_child()

    if parse_tree.get_root_val() == "!":
        return not judge_T_F(tmp_right,model)
    elif tmp_left and tmp_right:
        fn = parse_tree.get_root_val()
        if fn == "&":
            return judge_T_F(tmp_left,model) and judge_T_F(tmp_right,model)
        
        elif fn == "|":
            return judge_T_F(tmp_left,model) or judge_T_F(tmp_right,model)    
        
        #change "=>" and "<=>" to and/or which program can operate
        elif fn == "=>":
            return (not judge_T_F(tmp_left,model)) or judge_T_F(tmp_right,model)          
        
        elif fn == "<=>":
            return (((not judge_T_F(tmp_left,model)) or judge_T_F(tmp_right,model)) and 
                    ((not judge_T_F(tmp_right,model)) or judge_T_F(tmp_left,model)))
    
    else:
        return model[parse_tree.get_root_val()]

    
    
def model_check(s_KB,s_check):
    KB=[]
    for i in range(len(s_KB)):
        s = sentence(s_KB[i])
        s.build_parse_tree()
        KB.append(s)

    s=sentence(s_check[0])
    s.build_parse_tree()
    alpha = [s]
    result1 = tt_entails(KB,alpha)
    s_negative = "( ! " + s_check[0] + " )"
    s = sentence(s_negative)
    s.build_parse_tree()
    alpha = [s]
    result2 = tt_entails(KB,alpha)
    # check both alpha and !alpha
    #print(s_check[0])
    if result1 != result2:
        #print(result1)
        print("{0} : {1}".format(s_check[0],result1))
    else:
        
        print("{0} : not sure".format(s_check[0])) 


# ## Sample problem:

# ### Q1

# In[2]:

s_KB=['P',
      '( P => Q )']
s_check=['Q']
print('Question1:')
model_check(s_KB,s_check)
print('\n')


# ### Q2

# In[3]:

s_KB=['( ! P11 )',
      '( B11 <=> ( P12 | P21 ) )',
      '( B21 <=> ( P11 | P22 | P31 ) )',
      '( ! B11 )',
      'B21',]
s_check=['P12']

print('Question2:')
model_check(s_KB,s_check)
print('\n')


# ### Q3

# In[4]:

s_KB=[
    '( MY => IM )',
    '( ( ! MY ) => ( ( ! IM ) & MA ) )',
    '( ( IM | MA ) => HO )',
    '( HO => MA )']

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

# In[5]:

s_KB=['( A <=> ( C & A ) )',
     '( B <=> ( ! C ) )',
     '( C <=> ( B | ( ! A ) ) )']

s_check1=['A']
s_check2=['B']
s_check3=['C']

print('Question4(a):')
model_check(s_KB,s_check1)
model_check(s_KB,s_check2)
model_check(s_KB,s_check3)
print('\n')


# #### (b)

# In[6]:

s_KB=['( A <=> ( ! C ) )',
     '( B <=> ( A & C ) )',
     '( C <=> B )']

s_check1=['A']
s_check2=['B']
s_check3=['C']

print('Question4(b):')
model_check(s_KB,s_check1)
model_check(s_KB,s_check2)
model_check(s_KB,s_check3)
print('\n')


# ### Q5

# In[7]:

s_KB=['( A <=> ( H & I ) )',
      '( B <=> ( A & L ) )',
      '( C <=> ( B & G ) )',
      '( D <=> ( E & L ) )',
      '( E <=> ( C & H ) )',
      '( F <=> ( D & I ) )',
      '( G <=> ( ( ! E ) & ( ! J ) ) )',
      '( H <=> ( ( ! F ) & ( ! K ) ) )',
      '( I <=> ( ( ! G ) & ( ! K ) ) )',
      '( J <=> ( ( ! A ) & ( ! C ) ) )',
      '( K <=> ( ( ! D ) & ( ! F ) ) )',
      '( L <=> ( ( ! B ) & ( ! J ) ) )']

s_check=['A','B','C','D','E','F','G','H','I','J','K','L']

print('Question5:')
for i in range(len(s_check)):
    a=[s_check[i]]
    model_check(s_KB , a)
print('\n')


# In[ ]:



