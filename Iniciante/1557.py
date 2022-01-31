from math import log, ceil
while True:
	vetor = int(input())
	if vetor == 0:
		break
	maior = 2**(2*(vetor - 1))
	casas = int(ceil(log(maior, 10)))
	for i in range(vetor):
		margem = ''
		for j in range(vetor):
			valor = 2**(i+j)
			print(f'{margem}{valor:{casas}}', end='')
			margem = ' '
		print()
	print()