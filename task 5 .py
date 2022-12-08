# -*- coding: utf-8 -*-

import numpy as np
import statistics as stt

mxCustomer  = 100

clerks = list()
space  = list()
IAT = np.random.normal( 1.5 , 0.15 , mxCustomer+1 )
serviceTime = np.random.normal( 6 , 1 , mxCustomer+1 )
profit = [0,0]

for i in range ( 2 ):
    
    sales       = list()
    waitCost    = list()
    
    if   ( i == 0 ):
        clerks = [0,0]
        space  = [0,0,0]
    elif ( i == 1 ):
        clerks = [0,0,0,0,0,0]
        space  = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    AT = list()
    AT.append(0)

    for c in range ( 1 , mxCustomer+1 ):
        AT.append( IAT[c] + AT[c - 1] )
        
        if ( AT[-1] > 10*60 ):
            break
        
        startTime = max( AT[i] , min(clerks) )
        waitingTime = startTime - AT[-1]
        
        indexSpace = np.argmin( space  )
        indexClerk = np.argmin( clerks )
        if ( AT[-1] < min( space ) ):
            continue
        
        waitCost.append( waitingTime * 10/60 )
        sales.append( 22 ) 
        
        space [ indexSpace ] = startTime + serviceTime[c]
        clerks[ indexClerk ] = startTime + serviceTime[c]
        
        '''
        if ( c <= 10 ):
            print( clerks )
            print( space  )
            print( '------' )
        '''
    
    profitCount = sum(sales) - sum(waitCost) 
    if ( i == 0 ):
        profit[0] = profitCount - 200  - ( 20*3*10 )
    else:
        profit[1] = profitCount - 2000 - ( 20*6*10 )


#print( profit )
if ( profit[0] >= profit[1] ):
    print( 'use the first  configrations' )
else:
    print( 'use the second configrations' )






