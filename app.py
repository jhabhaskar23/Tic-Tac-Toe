import streamlit as st
import tictactoe as ttt # Imports your logic

st.title("Tic-Tac-Toe AI")

# Streamlit uses session state to keep track of the board between clicks
if "board" not in st.session_state:
    st.session_state.board = ttt.initial_state()

# Create a 3x3 grid of web buttons
for i in range(3):
    cols = st.columns(3)
    for j in range(3):
        with cols[j]:
            current_val = st.session_state.board[i][j]
            label = current_val if current_val is not None else " "
            
            if st.button(label, key=f"{i}-{j}", disabled=(current_val is not None)):
                # Update your board state using your tictactoe.py logic here
                # st.session_state.board = ttt.result(st.session_state.board, (i, j))
                st.rerun()import streamlit as st
import tictactoe as ttt # Imports your logic

st.title("Tic-Tac-Toe AI")

# Streamlit uses session state to keep track of the board between clicks
if "board" not in st.session_state:
    st.session_state.board = ttt.initial_state()

# Create a 3x3 grid of web buttons
for i in range(3):
    cols = st.columns(3)
    for j in range(3):
        with cols[j]:
            current_val = st.session_state.board[i][j]
            label = current_val if current_val is not None else " "
            
            if st.button(label, key=f"{i}-{j}", disabled=(current_val is not None)):
                # Update your board state using your tictactoe.py logic here
                # st.session_state.board = ttt.result(st.session_state.board, (i, j))
                st.rerun()
