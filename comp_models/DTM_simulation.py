# we consider a deterministic bi-infinite one-tape Turing machine
# for the input alphabet we use letters (lowercase)
# for tape symbols we use letters (uppercase) 
# for blank we use the symbol 'B'
# for non-halting states we use nonnegative integers (decimal strings)  
# the initial state is '0'
# for the halting state we use the symbol '*' 

from collections import deque

def TM_move(conf_left,conf_right,curr_state,trans_func):
    
    current_symbol = conf_right[0] # the symbol the head is pointing at
    u = (curr_state[0],current_symbol) # the input of transition function
    
    v = trans_func[u] # the output of transition function 
    curr_state[0] = v[0] # update state 
    conf_right[0] = v[1] # rewrite cell 
    move = v[2] # direction : left or right

    if move == 'L': # the head moves to the left  
        if conf_left: # check if conf_left is nonempty     
            s = conf_left[-1] # the last element of conf_left      
            conf_left.pop() # removing the last element of conf_left
            # check if conf_right has only one blank symbol
            bool_right = ((len(conf_right)==1) and (conf_right[0]=='B'))
            if bool_right:
                conf_right[0]=s # change conf_right to [s]
            else:    
                conf_right.appendleft(s) # updating conf_right         
        else: 
            # check if conf_right has only one blank symbol
            bool_right = ((len(conf_right)==1) and (conf_right[0]=='B'))
            if not bool_right:
                conf_right.appendleft('B') # appending the blank symbol  
    
    else: # the head moves to the right 
        s=conf_right[0] # the first element of conf_right 
        bool_left=((not conf_left) and (s=='B')) 
        if not bool_left:
            conf_left.append(s) # updating conf_left        
        
        conf_right.popleft() # removing the first element of conf_right
        if not conf_right: conf_right.append('B') # conf_right cannot be empty

    return conf_left,conf_right,curr_state     

def print_TM_conf(conf_left,conf_right,curr_state): 
    print(''.join(conf_left)+curr_state[0]+''.join(conf_right))

# main program 

# here we define the transition function
trans_func = {('0','a'):('1','B','L'),('0','b'):('1','a','L'),
              ('0','B'):('0','b','R'),('1','a'):('1','b','R'),
              ('1','b'):('0','B','L'),('1','B'):('0','B','R')}
# here we define the input string
input_str =  deque(['b','a','b','a'])
# here we set the number of moves TM makes
N = 50  

conf_left  = deque([]) # the left part of the configuration of TM    
conf_right = input_str # the right part of the configuration of TM
curr_state = ['0'] # the current state of TM 

# printing the initial configuration
print_TM_conf(conf_left,conf_right,curr_state)

# the loop does not stop even if TM halts
for i in range(N):
    if not curr_state[0]=='*': # check that the state is non-halting
        TM_move(conf_left,conf_right,curr_state,trans_func)
    print_TM_conf(conf_left,conf_right,curr_state)

