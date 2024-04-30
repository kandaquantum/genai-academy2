# import streamlit as st

# st.title('My Streamlit App')
# st.write('Hello, World!')




import streamlit as st

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

genre = st.radio(
    "What's your favorite movie genre",
    ('Comedy', 'Drama', 'Documentary'))

if genre == 'Comedy':
    st.write('You selected comedy.')
else:
    st.write("You didn't select comedy.")


# import streamlit as st
# import pandas as pd
# import numpy as np

# chart_data = pd.DataFrame(
#     np.random.randn(20, 3),
#     columns=['a', 'b', 'c'])

# st.line_chart(chart_data)