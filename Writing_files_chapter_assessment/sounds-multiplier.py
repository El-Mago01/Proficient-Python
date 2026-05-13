
def execute_order(order) -> bool:
    filename = order['filename']
    multiplicationNumber = order['multiplicationNumber']
    outputFilename = order['outputFilename']
    try:
        with open(filename, 'rb') as binfile:
            content=binfile.read()
    except FileNotFoundError:
        return False
    try:
        with open(outputFilename, 'wb') as outfile:
            outfile.write(content*multiplicationNumber)
    except FileNotFoundError:
        return False
    return True


def multiplier_demand() -> list:
    with open('sounds-multiply.csv', 'r') as csvfile:
        content = csvfile.read()
    lines = content.split('\n')
    order=[]
    count=0
    for line in lines:
        if count == 0: # skip header line
            count+=1
        else:
            if line[0] != '#' or len(line)>0:
                new_order={}
                filename, multiplicationNumber, outputFilename = line.split(',')
                new_order['filename'] = filename
                new_order['multiplicationNumber'] = int(multiplicationNumber)
                new_order['outputFilename'] = outputFilename
                order.append(new_order)
    return order

def main():
    orders = multiplier_demand()
    for order in orders:
        if execute_order(order):
            print('Success')
        else:
            print('Failed')

if __name__ == '__main__':
    main()
