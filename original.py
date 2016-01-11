import sys, time

start = time.time()

def timer(end):
    global start
    hours, rem = divmod(end-start, 3600)
    minutes, seconds = divmod(rem, 60)
    return ("{:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds))

def getTime():
    return timer(time.time())

sudoku = [
 			0, 0, 0, 0, 0, 0, 0, 0, 0,
			0, 0, 0, 0, 0, 0, 0, 0, 0,
			0, 0, 0, 0, 0, 0, 0, 0, 0,
			0, 0, 0, 0, 0, 0, 0, 0, 0,
			0, 0, 0, 0, 0, 0, 0, 0, 0,
			0, 0, 0, 0, 0, 0, 0, 0, 0,
			0, 0, 0, 0, 0, 0, 0, 0, 0,
			0, 0, 0, 0, 0, 0, 0, 0, 0,
			0, 0, 0, 0, 0, 0, 0, 0, 0
		]

def write(x, y, text):
    sys.stdout.write("\337\33[%d;%dH%s\338"%(x,y,text))

def imprime00():
    strRes = ""
    for i in range(len(sudoku)):
    	if i%(9*3) == 0:
    		strRes += '\n\n'
    	elif i%9 == 0:
    		strRes += '\n'
    	elif i%3 == 0:
    		strRes += '  '
    	strRes += "%d  "%sudoku[i]
    write(0, 0, strRes)
    write(2, 0, getTime())

def comprobar():
    if compruebaTodo() == 1:
        imprime()
        write(0, 50, "OK!")
        exit(0)
def bt(i):
    imprime00()
    comprobar()
    for n in range(len(sudoku))[i:]:
        if sudoku[n] != 0:
            continue
        else:
            for m in range(10)[1:]:
                sudoku[n] = m
                if comprueba(n) == -1:
                    sudoku[n] = 0
                    continue
                valor = bt(n+1)
                if valor == -1:
                    sudoku[n] = 0
            return -1
    return -1

def imprime():
	strRes = ""
	for i in range(len(sudoku)):
		if i%(9*3) == 0:
			strRes += '\n\n'
		elif i%9 == 0:
			strRes += '\n'
		elif i%3 == 0:
			strRes += '  '
		strRes += "%d  "%sudoku[i]
	print strRes

def compruebaTodo():
    coincidencias = 0
    for i in range(len(sudoku)):
    	valor = comprueba(i)
    	if valor == -1:
    		return -1
    	elif valor == 1:
    		coincidencias += 1

    return 1 if coincidencias == len(sudoku) else 0

def comprueba(i):
    aux = i
    while aux%9 > 0:
        aux -= 1


    coincidenciasH = 0
    for x in range(aux+9)[-9:]:
        if sudoku[x] == 0:
            continue
        if sudoku[x] == sudoku[i] and i != x:
            return -1
        if sudoku[x] != 0:
            coincidenciasH += 1

    valoresV = []
    for x in range(9):
        valoresV += [9*x + i%9]

    coincidenciasV = 0
    for x in valoresV:
        if sudoku[x] == sudoku[i] and i != x:
            return -1
        if sudoku[x] != 0:
        	coincidenciasV += 1

    posicion0C = i
    while posicion0C % 3 !=0:
        posicion0C -= 1
    mod = posicion0C%27

    while mod != 0 and mod != 3 and mod != 6:
        posicion0C -= 9
        mod = posicion0C%27

    valoresC = []
    for x in range(3):
        for y in range(3):
            valoresC += [ 9 * x + posicion0C + y ]

    coincidenciasC = 0
    for x in valoresC:
        if sudoku[x] == sudoku[i] and i!=x:
            return -1
        if sudoku[x] != 0:
            coincidenciasC += 1

    if coincidenciasV == 9 and coincidenciasH == 9 and coincidenciasC == 9:
    	return 1
    else:
    	return 0
bt(0)
