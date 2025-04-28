sdnt_inv = []

while True:
    name_input = input("Por favor, digite o nome do aluno: ")
    gpa_input = int(input("Por favor, digite o GPA do aluno: "))
    continueX = input("Continuar? Sim/Não \n")
    if continueX == "Não":
        break
    stdnt = {'Name': name_input, 'GPA': gpa_input}
    sdnt_inv.append(stdnt)


print(sdnt_inv)