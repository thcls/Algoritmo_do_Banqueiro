import csv
from os import listdir

def choose_input():
    files = listdir('inputs/')
    cont = 0
    for i in files:
        print('Num {}: {}'.format(str(cont),i),end='|\n')
        cont += 1
    
        num = int(input('Escolha o input:'))
        return files[num]
    
def get():
    n = 0
    m = 0
    allocation = []
    max = []
    available = []

    with open('inputs/' + choose_input(), newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        
        line_count = 0
        
        for row in csv_reader:
            
            if len(row) <= 1:
                continue
            elif line_count == 0:
                row = list(map(int, row))
                n, m = row
            elif line_count < n+1:
                row = list(map(int, row)) 
                allocation.append(row)
            elif line_count < n*2+1:
                row = list(map(int, row)) 
                max.append(row)
            
            else:
                row = list(map(int, row)) 
                available = row
                
            line_count += 1
    csv_file.close()
            
    return [n, m, allocation, max, available]

def workcheck(solicitation, available, n):
    for i in range(n):
        if solicitation[i] > available[i]:
            work = False
            break
        else:
            work = True
        return work  
    
def show(max, allocation,n,m):
    print('N = {}'.format(n))
    print('M = {}'.format(m))
    print('\nAllocation')
    for i in range(n):
        print('P' + str(i), end=' ')
        print(allocation[i])
    print('\nMax')
    for i in range(n):
        print('P' + str(i), end=' ')
        print(max[i])
    print('\n',end='')
    
def main():
    #etapa 1--------------------------------
    n, m, allocation, max, available = get()
    
    show(max, allocation,n,m)
    
    finish = [False]*n
    
    limit = 0
    safe = False
    line = []
    finish_order = []
    
    while not safe:
        
    #etapa 2--------------------------------
    
        for i in range(n):
            line = []
            
            for j in range(m):
                line.append(max[i][j] - allocation[i][j])
                
            need = line
            
    #etapa 3--------------------------------
    
            if finish[i] == False and workcheck(need,available, m):
                finish[i] = True
                finish_order.append('P'+ str(i))
                
                for j in range(m):
                    available[j] = available[j] + allocation[i][j]
                    
    #etapa 4--------------------------------
    
        for i in finish:
            if not i:
                print("O sistema ainda não esta seguro{}".format(finish))
                limit += 1
                break
            elif i:
                safe = True
                
        if limit == n:
            break
                
    if safe:
        print("\n--------------------------------------------------------------------------\nO sistema esta seguro para a ordem {}".format(finish_order))
    else:
        print("O sistema esta em deadlock {}".format(finish))
    
if __name__ == "__main__":
    main()