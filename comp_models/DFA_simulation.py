# we consider a deterministic finite automaton 
# for the input alphabet we use letters (lowercase)
# for states we use nonnegative integers (decimal strings)  
# the initial state is '0'
# accepting states are stored in the set accepting_state

def DFA_move(trans_func,input_str): 
    curr_state = '0'
    for curr_symbol in input_str: 
        curr_state = trans_func[(curr_state,curr_symbol)]    
    return curr_state

# main program 

# here we define the transition function and accepting states
trans_func = {('0','a'):'1',('0','b'):'3',
              ('1','a'):'0',('1','b'):'2',
              ('2','a'):'3',('2','b'):'0',
              ('3','a'):'1',('3','b'):'0'}
accepting_state = {'2','3'}

# here we define the input string
input_str =  ['b','a','b','a','a']

# here we return the final state after the input is read 
final_state = DFA_move(trans_func,input_str)

if final_state in accepting_state: 
    print('The input is accepted.') 
else: 
    print('The input is rejected.')