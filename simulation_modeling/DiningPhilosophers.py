# Dining philosophers 

import random
import simpy 
import matplotlib
import matplotlib.pyplot as plt

matplotlib.style.use("ggplot")

class Philosopher():
    T0=10   # Thinking time
    T1=10   # Eating time
    DT=1    # Time to pick the other chopstick
    def __init__(self,env,chopsticks, my_id): 
        
        self.env = env
        self.chopsticks = chopsticks 
        self.identity = my_id
        self.waiting = 0 
        # Register the environment 
        env.process(self.run_the_party())
        
    def get_hungry(self): 
        
        start_waiting = self.env.now 
        self.diag ("requested chopstick")
        rq1 = self.chopsticks[0].request() 
        yield rq1 
        self.diag("obtained chopstick")
        yield self.env.timeout(self.DT) 
        self.diag("requested another chopstick")
        rq2 = self.chopsticks[1].request() 
        yield rq2 
        self.diag("obtained another chopstick")
        self.waiting += self.env.now - start_waiting 
        return rq1, rq2 
    
    def run_the_party(self): 
        while True: 
            # Thinking 
            thinking_delay = random.expovariate(1 / self.T0)
            yield self.env.timeout(thinking_delay)
            # Getting hungry 
            get_hungry_p = self.env.process(self.get_hungry())
            rq1, rq2 = yield get_hungry_p
            # Eating 
            eating_delay = random.expovariate (1 / self.T1) 
            yield self.env.timeout(eating_delay)
            # Done eating, put down the chopsticks 
            self.chopsticks[0].release(rq1) 
            self.chopsticks[1].release(rq2) 
            self.diag("release the chopsticks")
    
    def diag(self,message):   
        print("P{} {} @{}".format(self.identity,message,self.env.now))

def simulate(n,t): 
   
    env = simpy.Environment()
    
    chopsticks=[simpy.Resource(env,capacity=1) for i in range(n)]
    
    philosophers = [Philosopher(env,(chopsticks[i],chopsticks[(i+1) % n]),i) for i in range(n)]
    
    env.run(until=t)
    
    return sum(ph.waiting for ph in philosophers) / n


N=20
X = range(2,N) 
Y = [simulate(n,500) for n in X] 
# Plot 
plt.plot(X,Y,"-o")
plt.ylabel("Waiting time")
plt.xlabel("Number of philosophers")
plt.show()