def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def is_safe(board, row, col, n):
    # 1. Sol taraftaki yatay sırayı kontrol et
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    # 2. Sol üst çaprazı kontrol et
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # 3. Sol alt çaprazı kontrol et
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    return True

def solve_n_queens(board, col, n):
    # Temel Durum: Tüm vezirler yerleştiyse çözüm tamamdır
    if col >= n:
        return True

    # Bu sütundaki her satırı dene
    for i in range(n):
        if is_safe(board, i, col, n):
            # Veziri koy
            board[i][col] = 'Q'

            # Bir sonraki sütunu çözmeye çalış (Recursive)
            if solve_n_queens(board, col + 1, n):
                return True

            # ÇÖZÜM YOKSA: BACKTRACK (Geri İzleme)
            # Veziri kaldır ve döngüdeki bir sonraki satırı dene
            board[i][col] = '.'

    return False

def n_queens(n):
    # NxN boş tahta oluştur
    board = [['.' for _ in range(n)] for _ in range(n)]

    if not solve_n_queens(board, 0, n):
        print("Çözüm bulunamadı!")
        return

    print(f"{n} Vezir İçin Çözüm:")
    print_board(board)

# --- TEST ---
if __name__ == "__main__":
    # 4 Vezir problemi (4x4 tahta)
    n_queens(4)
    
    print("-" * 20)
    
    # 8 Vezir problemi (Klasik Satranç Tahtası)
    n_queens(8)