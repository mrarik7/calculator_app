import streamlit as st

st.header('simple demo Calculator')
a=st.number_input('your first number:',step=0)
b=st.number_input('your second number:',step=0)


c1,c2,c3,c4 = st.columns(4)

with c1:
    if st.button('plus(+)'):
        st.text(f'{a}+{b}={a+b}')

with c2:
    if st.button('Minus(-)'):
        st.text(f'{a}-{b}={a-b}')

with c3:
    if st.button('multiplication(x)'):
        st.text(f'{a}X{b}={a*b}')
    

with c4:
    if st.button('division(/)'):
        st.text(f'{a}/{b}={b/a}')





st.text('-arik')
if st.button('info'):
    st.text('this is sample project made by arik')
    st.markdown('[About Arik](https://profilepy-3t8ez4hcjvvmwsczqmxnbz.streamlit.app/)')

