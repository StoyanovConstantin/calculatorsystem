import streamlit as st 

sis_list = ['2 (двоичная)', '8 (восьмеричная)', '10 (десетичная)', '16 (шеснадцатиричная)']
alph = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}

def convert(result):
    x = int(start_sis[:start_sis.find(' ')])
    y = int(last_sis[:last_sis.find(' ')])
    if y == 10:
        z = int(start_num, x)
    elif y == 2 and x == 10:
        z = bin(int(start_num))[2:]
    else:
        prom_otv = int(start_num, x)
        z = ''
        while prom_otv != 0:
            if y == 16 and prom_otv % y > 9:
                z += alph[prom_otv % y]
            else:
                z += str(prom_otv % y)
            prom_otv //= y
        z = z[::-1]
    result.subheader(f'Результат: {z}')
    


start_num = st.text_input(label='Исходное число')
start_sis = st.selectbox(label='Направление перевода', options=sis_list)
last_sis = st.selectbox(label='↕', options=sis_list)
btn = st.button(label='Конвертировать', type='primary')
result = st.subheader('Результат: ')
if btn:
    convert(result)
