import numpy as np, sys, os

def np_validate_structure(rows:list):
    def columns(row:str):
        column_length = 0
        ret=[]
        for j in range(len(row)):
            if row[j]=='+' or row[j]=='|':
                if 0==column_length:
                    column_start=j+1
                else:
                    found_cols = (column_start, column_start+column_length-1)
                    ret.append(found_cols)
                    column_start=j+1
                    column_length=0
            elif row[j] in cell_syntax:
                column_length += 1 
            else:
                print('np compiler syntax error:\n-- unknown character {}\n-- at column = {} row={} out of {} rows'.format(row[j], j, i, n_rows-1))
                return False
            
        #
        return ret
        
    cell_syntax = ['.','0','1','2','3','4','5','6','7','8','9','-',' ']
    n_rows = len(rows)
    n_3d_rows = 0
    n_data_rows = 0
    rows_types = []
    cols = []
    for i in range(n_rows):
        row = rows[i]
        if row.find('/') >= 0:
            n_3d_rows += 1
            rows_types.append('depth')
        elif row[0]=='+' or row[0]=='|':
            rows_types.append('vertical-spacer')
            cols_per_row = columns(row)
            if 0==len(cols): cols.append(cols_per_row)
            else:
                if cols_per_row != cols[0]:
                    print('np compiler syntax error:\n-- columns do not match {}\n-- vs. {}.\n-- at row={} out of {} rows'.format(cols_per_row, cols[0], i, n_rows-1))
                    return False
                    
        if row[0]=='|':
            n_data_rows += 1
            rows_types.append('data')
            
    return True


def npp(rows:int, columns:int, depth:int=1):
    '''
    return a string print of the 3D matrix
    '''
    sRows = '%5d' % (rows-1)
    sColumns = '%5d' % (columns-1)
    sDepth = '%5d' % (depth-1)
    if depth>1:
        x =\
        '''             
           +-----+---+-----+
          /     /   /DDDDD /
         /     /   /      /|
        +-----+---+-----+/ .
        |0    |...|CCCCC| /|
        +-----+---+-----+/ .
        |...  |   |     | /|
        +-----+---+-----+/ +
        |RRRRR|   |     | /
        +-----+---+-----+/
        '''
        x = x.replace('DDDDD',sDepth)
        x = x.replace('CCCCC', sColumns)
        x = x.replace('RRRRR', sRows)
    else:
        x =\
        '''             
        +-----+---+-----+
        |0    |...|CCCCC|
        +-----+---+-----+
        |...  |   |     |
        +-----+---+-----+
        |RRRRR|   |     |
        +-----+---+-----+
        '''
        x = x.replace('CCCCC', sColumns)
        x = x.replace('RRRRR', sRows)
    
    return x
    
    
def npn(rows:list):
    '''
    @return list of list-3 [integer, row, column]
    '''
    numbers=[]
    n_rows = len(rows)
    for i in range(0,n_rows,1):
        row=rows[i]
        n_chars = len(row)
        ci = 0
        aNumber = ''
        sign = 1
        while ci<n_chars:
            c = row[ci]
            if '|' == c or ' ' == c or '/' == c or '.' == c:
                if len(aNumber)>0:
                    numbers.append([sign*int(aNumber),i,ci])  # list
                #
                aNumber = ''
                sign = 1
            elif c>='0' and c<='9':
                # if aNumber is still empty, check if we have a negative sign before it
                if 0 == len(aNumber):
                    sign = 1
                    if ci>=1 and row[ci-1]=='-':
                        sign = -1
                aNumber += c
            ci+=1
    return (numbers, rows)

def npnu(data:tuple):
    numbers, rows = data
    depth = 1
    if 3==len(numbers):
        # case1: 3D matrix with columns=1 or 
        # case2: 2D matrix
        n0,n1,n2=numbers
        # if rows of n0,n1 are the same, its 2D
        if n0[1] == n1[1]:
            return 1+n2[0]-n0[0], 1+n1[0]-n0[0], depth
        else:  # case 1
            return 1+n2[0]-n1[0], 1, 1+n0[0]-n1[0]
            
    elif 4==len(numbers):  # 3D?
        n0,n1,n2,n3=numbers
        return 1+n3[0]-n1[0], 1+n2[0]-n1[0], 1+n0[0]-n1[0]
        
    else:  # explicit structure
        n_rows = len(rows)
        count_rows = 0
        count_depth = 0
        for i in range(n_rows):
            row = rows[i]
            if len(row)>0:
                if '|' == row[0]: 
                    count_rows+=1
                elif row.find('/') >= 0 and row[0]!='+':  # 3d case
                    count_depth += 1
        #
        if 0==count_depth: 
            count_depth=1
        #
        count_columns = 0        
        for i in range(n_rows-1):
            row = rows[i]
            next_row = rows[i+1]
            if '|'==row[0]:  # 2d case
                count_bars=0
                for ci in range(len(row)):
                    if '|'==row[ci] and next_row[ci] == '+': 
                        count_bars+=1
                count_columns = count_bars-1
                break
        return count_rows, count_columns, count_depth

def np2(x:str):
    '''
    Syntax:           Example (102,29)
    +---+---+---+     +---+---+---+  
    | 0 |...|int|     | 0 |...| 28|
    +---+---+---+     +---+---+---+  
    |...|   |   |     |...|   |   |
    +---+---+---+     +---+---+---+  
    |int|   |   |     |101|   |   |
    +---+---+---+     +---+---+---+  

    Or just the REAL n_rows and n_columns (4,7):
    +--+--+--+--+--+--+--+
    |  |  |  |  |  |  |  |
    +--+--+--+--+--+--+--+
    |  |  |  |  |  |  |  |
    +--+--+--+--+--+--+--+
    |  |  |  |  |  |  |  |
    +--+--+--+--+--+--+--+
    |  |  |  |  |  |  |  |
    +--+--+--+--+--+--+--+

    Cell width can be any length, like: +---+, +-----+, etc
    Cell height should be exactly 3 rows:  +----+
                                           |int |
                                           +----+
    
    raise exception on error
    '''
    _rows = x.split('\n')
    if np_validate_structure(_rows) is False:
        err = 'np2 failed to validate structure of\n{}'.format('\n'.join(_rows))
        raise Exception(err)
    n_rows = len(_rows)
    for i in range(2,n_rows,2):
        if _rows[0] != _rows[i]:
            err = 'np2 failed to match "x" as 2D matrix. row {} does not match row 0'.format(_rows[i])
            raise Exception(err)
    rows, columns, depth = npnu(npn(_rows))
    return np.zeros((rows, columns, depth))

    
def np3(x:str):
    '''
    Support 2D, 3D and 3D with columns=1 textual matrices. return numpy matrix.
    
    Example:             Format: must use only <int> + - / . | characters
    
       +---+--------+
      /002/        /| 
     /   /        / .
    +---+---+---+/ /|
    | 0 |...| 8 | / .
    +---+---+---+/ /|
    |...|   |   | / +
    +---+---+---+/ /
    |10 |   |   | /
    +---+---+---+/

    '''
    _rows = x.split('\n')
    rows = []
    x = ''
    found_fwd_slash=False
    for r in _rows:
        if 0 == len(r.strip()):
            r = r.strip()
        if r.find('/')>0:
            found_fwd_slash=True
        if len(r)>0:
            rows.append(r)
            x += r + '\n'
    #
    if x[-1]=='\n':
        x=x[0:-1]
    #    
    if found_fwd_slash is False:  # a 2D matrix
        y = np2(x)
    else: # a 3D matrix
        rows, columns, depth = npnu(npn(_rows))
        y = np.zeros((rows, columns, depth))
    #
    return y
    
def selftest():
    rows = 11
    cols = 9
    depth = 3
    p = np.zeros((rows, cols, depth))

    c2d = np.zeros((rows, depth))
    r2d = np.zeros((cols, depth))
    d2d = np.zeros((rows, cols))
                           
    x = np3(
    '''
    +---+---+---+
    | 0 |...| 28|
    +---+---+---+
    |...|   |   |
    +---+---+---+
    |101|   |   |
    +---+---+---+
    ''')
    print(x)
    print('computed shape=',x.shape, 'SUCCESS=', x.shape==(1+101-0,1+28-0))

    # syntax errors: not all rows and columns match
    try:
        x = np3(
    '''
    +---+---+----+
    | 0 |...| 28 |
    +---+---+----+
    |...|   |    |
    +---+---+-------+
    |101|   |       |
    +---+---+-------+
    ''')
    except Exception as e:
        print('expecting exception={}'.format(e))

    try:
        x = np3(
    '''
    +-----+---+----+
    | 0   |...| 28 |
    +-----+---+----+
    |...|   |    |
    +---+---+----+
    |101|   |    |
    +---+---+----+
    ''')
    except Exception as e:
        print('expecting exception={}'.format(e))


    try:
        x = np3(
    '''
    +---+---+----+
    | 0 |...| 28 <
    +---+---+----+
    |...|   |    |
    +---+---+----+
    |101|   |    |
    +---+---+----+
    ''')
    except Exception as e:
        print('expecting exception={}'.format(e))


    for i in range(1, 4):
        for j in range(1, 4):
            for k in range(1, 4):
                x = np3(npp(i,j,k))
                print('computed shape=',x.shape, 'SUCCESS=', x.shape==(i,j,k))

    x = np3(
    '''             
    +---+---+---+
    | 1 |...| 29|
    +---+---+---+
    |...|   |   |
    +---+---+---+
    |102|   |   |
    +---+---+---+
    ''')
    print('computed shape=',x.shape, 'SUCCESS=', x.shape==(1+102-1,1+29-1,1))


    x = np3(
    '''             
       +---+---+----+
      /   /   /   2/| 
     /   /   /    / .
    +---+---+---+/ /|
    | 0 |...| 8 | / .
    +---+---+---+/ /|
    |...|   |   | / .
    +---+---+---+/ /
    |10 |   |   | /
    +---+---+---+/
    ''')
    print('computed shape=',x.shape, 'SUCCESS=', x.shape==(1+10-0,1+8-0,1+2-0))


    x = np3(
    '''             
    +--+--+--+--+--+--+--+
    |  |  |  |  |  |  |  |
    +--+--+--+--+--+--+--+
    |  |  |  |  |  |  |  |
    +--+--+--+--+--+--+--+
    |  |  |  |  |  |  |  |
    +--+--+--+--+--+--+--+
    |  |  |  |  |  |  |  |
    +--+--+--+--+--+--+--+
    ''')
    print('computed shape=',x.shape, 'SUCCESS=', x.shape==(4,7,1))


    x = np3(
    ''' 
        +--------------------+            
       /I use explicit depth/|
      +--------------------+ .
     /  here depth=two    /  |
    +--+--+--+--+--+--+--+   |
    |  |  |  |  |  |  |  |   |
    +--+--+--+--+--+--+--+   |
    |  |  |  |  |  |  |  |   |
    +--+--+--+--+--+--+--+   |
    |  |  |  |  |  |  |  |   .
    +--+--+--+--+--+--+--+  /
    |  |  |  |  |  |  |  | /
    +--+--+--+--+--+--+--+
    ''')
    print('computed shape=',x.shape, 'SUCCESS=', x.shape==(4,7,2))

    # Test errors
    x = np3(
    '''
    +---+---+---+
    | 0 |...| 28|
    +---+---+---+
    |...|   |   |
    +---+---+---+
    |101|   |   |
    +---+---+---+
    ''')
    print('computed shape=',x.shape, 'SUCCESS=', x.shape==(1+101-0,1+28-0,1))

    try:
        x = np3(
        '''
        +---+---+---+
        | 0 |...|-28|
        +---+---+---+
        |...|   |   |
        +---+---+---+
        |101|   |   |
        +---+---+---+
        ''')
    except Exception as e:
        print('expecting exception={}'.format(e))

    x = np3(
    '''
    +---+---+---+
    | 0 |...| 28|
    +---+---+---+
     ...|   |   |
    +---+---+---+
    |101|   |   |
    +---+---+---+
    ''')
    print('computed shape=',x.shape, 'SUCCESS=', x.shape==(1+101-0,1+28-0,1))

    # we also support different column width - it makes no change
    x = np3(
    '''
    +---+----+---+
    | 0 |... | 28|
    +---+----+---+
     ...|    |   |
    +---+----+---+
    |101|    |   |
    +---+----+---+
    ''')
    print('computed shape=',x.shape, 'SUCCESS=', x.shape==(1+101-0,1+28-0,1))

    x = np3(
    '''             
      +---+
     / 23/
    +---+
    | 0 |
    +---+
    |...|
    +---+
    |10 |
    +---+
    ''')
    print('computed shape=',x.shape, 'SUCCESS=', x.shape==(1+10-0,1,1+23-0))

    x = np3(
    '''             
      +----+
     / 123/
    +----+
    | 0  |
    +----+
    |... |
    +----+
    |10  |
    +----+
    ''')
    print('computed shape=',x.shape, 'SUCCESS=', x.shape==(1+10-0,1,1+123-0))


    x = np3(
    '''             
      +---+---+----+
     /   /   /    /.
    +---+---+---+/ |
    | 0 |...| 8 | /.
    +---+---+---+/ |
    |...|   |   | /.
    +---+---+---+/ /
    |10 |   |   | /
    +---+---+---+/
    ''')
    print('computed shape=',x.shape, 'SUCCESS=', x.shape==(1+10-0,1+8-0,1))


    x = np3(
    '''             
      we can even use negative indices!
      +------+
     / 1231 /
    +------+
    | -19  |
    +------+
    |...   |
    +------+
    |19    |
    +------+
    ''')
    print('computed shape=',x.shape, 'SUCCESS=', x.shape==(1+19--19,1,1+1231--19))


    x47 = np3(
    ''' 
    +--+--+--+--+--+--+--+
    |  |  |  |  |  |  |  |
    +--+--+--+--+--+--+--+
    |  |  |  |  |  |  |  |
    +--+--+--+--+--+--+--+
    |  |  |  |  |  |  |  |
    +--+--+--+--+--+--+--+
    |  |  |  |  |  |  |  |
    +--+--+--+--+--+--+--+
    ''').squeeze()

    x74 = np3(
    ''' 
    +--+--+--+--+
    |  |  |  |  |
    +--+--+--+--+
    |  |  |  |  |
    +--+--+--+--+
    |  |  |  |  |
    +--+--+--+--+
    |  |  |  |  |
    +--+--+--+--+
    |  |  |  |  |
    +--+--+--+--+
    |  |  |  |  |
    +--+--+--+--+
    |  |  |  |  |
    +--+--+--+--+
    ''').squeeze()

    print('x74 dot x47 = (7,7) = {}'.format(np.dot(x74, x47)))
    print('x47 dot x74 = (4,4) = {}'.format(np.dot(x47, x74)))
    print(npp(7,3,9))
    print(npp(7,3))
    print(np3(npp(7,3,9)).shape)
    print(np3(npp(7,3)).shape)

if __name__ == '__main__':
    selftest()