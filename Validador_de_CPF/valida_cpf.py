# from re import findall


# Recebe e executa o processo de validação
def validacpf(cpf):
    sanitiza = contacpf(cpf)
    verificador = seg_dig_verificador(sanitiza) if sanitiza != '' else ' '
    resp = ' Deve Conter 11 Números' if sanitiza == '' else ''
    return 'CPF Valido !!!' if sanitiza[9:11] == verificador else f'CPF Invalido{resp}'


'''
# limpa e sanitiza
def limpacpf(cpf):
    return ''.join(findall('[0-9]', cpf))
'''


# limpa e sanitaza
def limpacpf(cpf):
    return ''.join(c for c in str(cpf) if c in '0123456789')


# verifica se e possui 11 caracteres
def contacpf(cpf):
    return limpacpf(cpf) if len(limpacpf(cpf)) == 11 else ''


# calcula digito verificador
def dig_verificardorcpf(cpf):
    return 0 if cpf % 11 < 2 else 11 - cpf % 11


# multiplica os numeros
def mult_num_validador(inicio, cpf):
    cont = soma = 0
    for c in range(inicio, 1, -1):
        soma += int(cpf[cont]) * c
        cont += 1
    return dig_verificardorcpf(soma)


# calcula o primeiro digito verificador
def prim_dig_verificador(cpf):
    return mult_num_validador(10, cpf)


# recebe o primeiro digito verificador e calcula o segundo
def seg_dig_verificador(cpf):
    dig_ver_um = prim_dig_verificador(cpf)
    return ''.join([str(dig_ver_um), str(mult_num_validador(11, cpf[0:9] + str(dig_ver_um)))])
