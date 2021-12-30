import math


cosh=math.cosh
holder=[]
table_val=[]
def table(target,step, limit_up, limit_down):
  
    # generating the list (cant use float for decomlas so the number is devided by 10 in the for loop)
    for i in range(limit_down, limit_up, step):
        x = i/10
    # apending the values (-1,-0.5,0..... to the index list)
        
        holder.append(x)
        eq=cosh(x)
    # Entering the e equation i wish to build the table on
        
        table_val.append(eq)  # appending values 
    for idx, value in enumerate(table_val):
        answer=table_val[idx] + ((table_val[idx+1]-table_val[idx])/(table_val[value] - table_val[value]))*(target-table_val[value]) 
        print(str(answer))
    return answer
        
       


table(1.2,10,31,3)