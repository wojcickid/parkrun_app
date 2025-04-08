import streamlit as st



last_event = st.Page("last_event.py", title="Ostatnie spotkanie", icon="🗓️", default=True)
best_time = st.Page("best_time.py", title="Najlepsze czasy", icon="👟" )
last_month = st.Page("last_month.py", title="Ostatni miesiąc", icon="📅" )
challange_1111 = st.Page("challange_1111.py", title="Wyzwanie 1111", icon="🕒" )
challange_fib = st.Page("challange_fib.py", title="Wyzwanie ciągu Fibonacciego", icon="🕒" )
challange_palindrome = st.Page("challange_palindrome.py", title="Wyzwanie Palindrom", icon="🕒" )

pg = st.navigation(
    {
        "Twój wybór": [last_event, 
                       best_time
                       ],
        "Wyzwania": [challange_1111,
                    challange_fib,
                    challange_palindrome ]
    }
)

pg.run()