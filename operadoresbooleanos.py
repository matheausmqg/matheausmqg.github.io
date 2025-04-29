# and/or/not

print('----- INÍCIO -----')

estou_com_fome = input('Estou com fome? (Digite s para sim)') == 's'
tenho_comida = input('Tenho comida? (Digite s para sim)') == 's'

if estou_com_fome and not tenho_comida:
    print('Ir ao mercado')
    print('Voltar para casa')
    print('Preparar uma refeição')
    print('Comer a comida')

if estou_com_fome and tenho_comida:
    print('Preparar uma refeição')
    print('Comer a comida')

print('\n----- FIM -----')