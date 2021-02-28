# receber um numero int
#converter para binario
#contar o número de 1's
print(len(max(bin(int(input())).replace("0b", "").split('0'))))

#bin() -> converte o número em binário

#split() -> quebra a string e transforma e retorna uma lista de substrings

#max(list) -> retorna o maior elemento de uma lista

# len() -> retorna o tamanho do elemento (no caso o tamanho da string)   
