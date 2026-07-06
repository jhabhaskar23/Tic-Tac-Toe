import streamlit as st
import time
import tictactoe as ttt

# Set up page layout and title
st.set_page_config(page_title="Tic-Tac-Toe AI", layout="centered")

# --- HIGHLY STYLED CUSTOM INTERFACE (CSS) ---
st.markdown("""
    <style>
    /* Center the main container */
    .block-container {
        padding-top: 2rem;
        max-width: 450px !important;
    }
    
    /* Main Header Styling */
    .game-header {
        text-align: center;
        font-size: 36px;
        font-weight: 800;
        background: linear-gradient(45deg, #1e90ff, #ff4757);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 10px;
    }
    
    /* Subtitle Status text */
    .status-text {
        text-align: center;
        font-size: 20px;
        font-weight: 600;
        color: #57606f;
        margin-bottom: 25px;
        height: 30px;
    }

    /* Style the 3x3 Grid Buttons */
    div.stButton > button[key^="tile-"] {
        width: 100% !important;
        height: 110px !important;
        font-size: 38px !important;
        font-weight: bold !important;
        border-radius: 12px !important;
        border: 2px solid #e4e7eb !important;
        background-color: #ffffff !important;
        transition: all 0.2s ease;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    
    div.stButton > button[key^="tile-"]:hover {
        border-color: #1e90ff !important;
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(30,144,255,0.15);
    }
    
    /* Style the Control Menu Buttons (Play as X/O, Restart) */
    div.stButton > button:not([key^="tile-"]) {
        background: linear-gradient(135deg, #2f3542, #57606f) !important;
        color: white !important;
        font-weight: bold !important;
        border-radius: 8px !important;
        padding: 10px 20px !important;
        border: none !important;
        width: 100% !important;
    }
    </style>
""", unsafe_allow_html=True)

# 1. Initialize Session State
if "user" not in st.session_state:
    st.session_state.user = None
if "board" not in st.session_state:
    st.session_state.board = ttt.initial_state()

board = st.session_state.board
user = st.session_state.user

game_over = ttt.terminal(board)
player = ttt.player(board)

st.markdown("<div class='game-header'>Tic-Tac-Toe AI</div>", unsafe_allow_html=True)

# 2. SCREEN: Menu Selection
if user is None:
    st.markdown("<div class='status-text'>Choose your side to begin</div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Play as X"):
            st.session_state.user = ttt.X
            st.rerun()
    with col2:
        if st.button("Play as O"):
            st.session_state.user = ttt.O
            st.rerun()

# 3. SCREEN: Main Active Game Board
else:
    # Update status banner messaging 
    if game_over:
        winner = ttt.winner(board)
        if winner is None:
            status_title = "🤝 Game Over: It's a Tie!"
        else:
            status_title = f"🎉 Game Over: Player {winner} Wins!"
    elif user == player:
        status_title = f"⚡ Your Turn ({user})"
    else:
        status_title = "🤖 Computer is thinking..."

    st.markdown(f"<div class='status-text'>{status_title}</div>", unsafe_allow_html=True)

    # Trigger Engine Logic on AI's Turn
    if user != player and not game_over:
        with st.spinner(""):
            time.sleep(0.4)
            move = ttt.minimax(board)
            st.session_state.board = ttt.result(board, move)
        st.rerun()

    # Draw the polished 3x3 Tile Matrix
    for i in range(3):
        cols = st.columns(3)
        for j in range(3):
            with cols[j]:
                current_val = board[i][j]
                
                # Pre-format visual labels
                label = current_val if current_val is not None else ""
                
                # Completely lock interaction if grid filled, game over, or AI loop processing
                button_disabled = (current_val is not None) or game_over or (user != player)
                
                if st.button(label, key=f"tile-{i}-{j}", disabled=button_disabled):
                    st.session_state.board = ttt.result(board, (i, j))
                    st.rerun()

    # 4. SCREEN: Post Game Cleanup
    if game_over:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🔄 Play Again"):
            st.session_state.user = None
            st.session_state.board = ttt.initial_state()
            st.rerun()
