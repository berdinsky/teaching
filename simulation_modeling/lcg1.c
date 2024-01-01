// linear congruential generator  - simple illustration  

#include <stdio.h>
   

void prntseq(int a, int c, int m, int seed);
int fullperiod (int a, int c, int m);

void main() {
    
    int a,c,m,seed;   
    a = 13; 
    c = 13; 
    m = 256; 
    seed = 0;  
    prntseq (a,c,m,seed);  
    if (fullperiod(a,c,m)==1) 
        printf("This LCG has a full period.\n");	
    else 
        printf("This LCG does not have a full period.\n");	    
}

void prntseq(int a, int c, int m, int seed) 
{
    int z,i;
    z=seed;   
    i=0;
		
    while (i<m){ 
        printf("%d \n", z);
        i++; 
        z= (a*z + c) % m;  
    }
}
/* BRUTE FORCE*/
int fullperiod (int a, int c, int m)
{
    int z,y;
    int i,j;  
    z=0; 
    i=0;
    while (i<m-1)
    { 
        z= (a*z + c) % m; 
        y=0;
        for (j=0;j<=i;j++)
        {    
            if (z==y) return 0;
	        y = (a*y + c) % m; 
        }	 
        i++;     
    }	   
    return 1; 
}	
