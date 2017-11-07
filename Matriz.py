mat=[[0,0],[0,0]]
def det(matrix):
	return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
	for i in range(2):
		for j in range(2):
			print("Ingrese el valor de la posicion[",i,"][",j,"]")
			mat[i][j]= int( input())
print("\n\ndet(", mat ,")=", det(mat))