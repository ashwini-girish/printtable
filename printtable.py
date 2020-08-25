def multtable(start, stop, number):
    """
    Print multiplication table for <number>
    from <start> to including <stop>
    """
    print ('Mult table')
    for i in range(start, stop+1):
        print(f"{i} x {number} = {i*number}")
    print ('')
        #output: 1 x 7 = 7

if __name__ == '__main__':
    multtable(1, 4, 7)
