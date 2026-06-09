gastos = []

while True:
    print('=== CONTROLE DE GASTOS ===')
    print('1 - Adicionar gasto')
    print('2 - Ver todos os gastos')
    print('3 - Ver total gasto')
    print('4 - Sair')

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        nome = input('Nome do gasto (ex: mercado, transporte): ')
        valor = float(input('Valor gasto: R$ '))
        gastos.append({'nome': nome, 'valor': valor})
        print('Gasto adicionado com sucesso!\n')

    elif opcao == '2':
        if len(gastos) == 0:
            print('Nenhum gasto registrado ainda.\n')
        else:
            print('\n--- Seus gastos ---')
            for i, gasto in enumerate(gastos, 1):
                print(f'{i}. {gasto["nome"]} - R$ {gasto["valor"]:.2f}')
            print()

    elif opcao == '3':
        if len(gastos) == 0:
            print('Nenhum gasto registrado ainda.\n')
        else:
            total = sum(gasto['valor'] for gasto in gastos)
            print(f'\nTotal gasto: R$ {total:.2f}\n')

    elif opcao == '4':
        print('Saindo... Até mais!')
        break

    else:
        print('Opção inválida!\n')
        
