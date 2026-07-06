import streamlit as st
import time
import tictactoe as ttt

# Set up page styling
st.set_page_config(page_title="Tic-Tac-Toe AI", layout="centered")

# Custom CSS to center things and style the buttons neatly
st.markdown("""
    <style>
    div.stButton > button {
        width: 100%;
        height: 80px;
        font-size: 24px !important;
        font-weight: bold;
    }
    .status-text {
        text-align: center;
        font-size: 30px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# 1. Initialize Streamlit Session State (Replaces global variables in Pygame)
if "user" not in st.session_state:
    st.session_state.user = None
if "board" not in st.session_state:
    st.session_state.board = ttt.initial_state()

board = st.session_state.board
user = st.session_state.user

# Game state checks using your tictactoe.py logic
game_over = ttt.terminal(board)
player = ttt.player(board)

# 2. SCREEN: Choose Player (X or O)
if user is None:
    st.markdown("<div class='status-text'>Play Tic-Tac-Toe</div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Play as X"):
            st.session_state.user = ttt.X
            st.rarun() if hasattr(st, "rarun") else st.rerun()
            
    with col2:
        if st.button("Play as O"):
            st.session_state.user = ttt.O
            st.rarun() if hasattr(st, "rarun") else st.rerun()

# 3. SCREEN: Main Game Board
else:
    # Header Status Control
    if game_over:
        winner = ttt.winner(board)
        if winner is None:
            status_title = "Game Over: Tie!"
        else:
            status_title = f"Game Over: {winner} wins!"
    elif user == player:
        status_title = f"Play as {user}"
    else:
        status_title = "Computer thinking..."

    st.markdown(f"<div class='status-text'>{status_title}</div>", unsafe_allow_html=True)

    # Handle AI Move automatically
    if user != player and not game_over:
        with st.spinner("AI is calculating..."):
            time.sleep(0.5)  # Mimic the thinking delay
            move = ttt.minimax(board)
            st.session_state.board = ttt.result(board, move)
        st.rerun()

    # Render the 3x3 interactive board grid
    for i in range(3):
        cols = st.columns(3)
        for j in range(3):
            with cols[j]:
                current_val = board[i][j]
                
                # Format empty spaces vs selections
                if current_val == ttt.X:
                    label = "X"
                elif current_val == ttt.O:
                    label = "O"
                else:
                    label = " "

                # Disable buttons if the game is over or it's the AI's turn or cell is filled
                button_disabled = (current_val is not ttt.EMPTY) or game_over or (user != player)
                
                if st.button(label, key=f"tile-{i}-{j}", disabled=button_disabled):
                    st.session_state.board = ttt.result(board, (i, j))
                    st.rerun()

    # 4. SCREEN: Reset Game Flow
    if game_over:
        st.write("")  # spacing
        col_reset, _ = st.columns([1, 2])
        with col_reset:
            if st.button("Play Again"):
                st.session_state.user = None
                st.session_state.board = ttt.initial_state()
                st.rerun()
