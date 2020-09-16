stockpricce={}
with open("knime.csv","r") as f:
    for line in f:
        token=line.split(',')
        code=token[0]
        pridicted=token[2]
        stockpricce[code]=pridicted
print(stockpricce)