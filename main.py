from csv import reader
from os import listdir

def choose_input():
    files = listdir('inputs/')
    cont = 0
    for i in files:
        print('Num {}: {}'.format(str(cont),i),end=' | ')
        cont += 1
    
    num = int(input('\nEscolha o input: '))
    return files[num]

def get():
    n = 0
    m = 0
    allocation = []
    max = []
    available = []

    with open('inputs/' + choose_input(), newline='') as csv_file:
        csv_reader = reader(csv_file, delimiter=',')
        
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

def show(max, allocation, available,n,m):
    print('\nN = {}'.format(n))
    print('M = {}'.format(m))
    
    print('\nAllocation')
    for i in range(n):
        print('P' + str(i), end=' ')
        print(allocation[i])
        
    print('\nMax')
    for i in range(n):
        print('P' + str(i), end=' ')
        print(max[i])
    print('')
    
    print('Available')
    print(available, end='\n\n')

def main():
    
    #etapa 1--------------------------------
    n, m, allocation, max, available = get()
    
    show(max, allocation, available, n, m)
    
    finish = [False]*n
    
    limit = 0
    safe = False
    finish_order = []
    
    #etapa 2--------------------------------
    while not safe and limit < n+1:
        for i in range(n):
            line = []
            for j in range(m):
                line.append(max[i][j] - allocation[i][j])
                
            need = line        
    
            if finish[i] == False and workcheck(need,available, m):
                #etapa 3--------------------------------
                finish[i] = True
                finish_order.append('P'+ str(i))
                
                for j in range(m):
                    available[j] = available[j] + allocation[i][j]
        #etapa 4--------------------------------
        if len(set(finish)) == 1 and finish[0]:
            safe = True
        else:
            print("O sistema ainda não esta seguro {}\n:".format(finish))
            limit += 1
            safe = False
            
    if safe:
        print(":\nO sistema esta seguro para a ordem {}".format(finish_order))
    else:
        print("O sistema não esta seguro {}".format(finish))

if __name__ == "__main__":
    main()