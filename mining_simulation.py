import hashlib
import time
import tkinter as tk

class Block:
    def __init__(self, index, data, previousHash=''):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previousHash = previousHash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        # Calculate SHA-256 hash of block contents including nonce
        contents = f"{self.index}{self.timestamp}{self.data}{self.previousHash}{self.nonce}"
        return hashlib.sha256(contents.encode()).hexdigest()

    def mineBlock(self, difficulty, update_callback):
        # Mining tries to find a hash with difficulty number of leading zeros
        prefix_str = '0' * difficulty
        attempts = 0
        start_time = time.time()

        # Keep incrementing nonce until hash meets difficulty condition
        while not self.hash.startswith(prefix_str):
            self.nonce += 1
            self.hash = self.calculate_hash()
            attempts += 1

            # Update the UI every 1000 attempts to keep interface responsive
            if attempts % 1000 == 0:
                elapsed = time.time() - start_time
                update_callback(self.nonce, self.hash, attempts, elapsed)

        elapsed = time.time() - start_time
        update_callback(self.nonce, self.hash, attempts, elapsed)

        # Log mining completion details
        print(f"[MINING COMPLETE] Nonce found: {self.nonce}")
        print(f"[MINING COMPLETE] Hash: {self.hash}")
        print(f"[MINING COMPLETE] Total attempts: {attempts}")
        print(f"[MINING COMPLETE] Time taken: {elapsed:.2f} seconds")

def start_mining():
    difficulty = 4  # Number of leading zeros required
    btn_start.config(state='disabled')
    block.nonce = 0
    block.hash = block.calculate_hash()

    def update_ui(nonce, hash_val, attempts, elapsed):
        # Update labels with current mining status
        nonce_var.set(f"Nonce: {nonce}")
        hash_var.set(f"Hash: {hash_val[:30]}...")
        attempts_var.set(f"Attempts: {attempts}")
        time_var.set(f"Time: {elapsed:.2f} s")
        root.update()

    print("[MINING STARTED] Beginning mining process...")
    block.mineBlock(difficulty, update_ui)
    print("[MINING FINISHED] Mining process completed.")
    btn_start.config(state='normal')

block = Block(1, "Visual Mining Block", "0"*64)

root = tk.Tk()
root.title("Proof-of-Work Mining Visualization")

nonce_var = tk.StringVar(value="Nonce: 0")
hash_var = tk.StringVar(value="Hash: ")
attempts_var = tk.StringVar(value="Attempts: 0")
time_var = tk.StringVar(value="Time: 0.00 s")

tk.Label(root, text="Mining a Block with Difficulty 4 (hash starts with '0000')", font=("Arial", 14)).pack(pady=10)
tk.Label(root, textvariable=nonce_var, font=("Courier", 12)).pack()
tk.Label(root, textvariable=hash_var, font=("Courier", 12)).pack()
tk.Label(root, textvariable=attempts_var, font=("Courier", 12)).pack()
tk.Label(root, textvariable=time_var, font=("Courier", 12)).pack()

btn_start = tk.Button(root, text="Start Mining", command=start_mining)
btn_start.pack(pady=20)

root.mainloop()
