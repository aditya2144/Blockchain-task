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
        # Calculate SHA-256 hash of block contents
        contents = f"{self.index}{self.timestamp}{self.data}{self.previousHash}{self.nonce}"
        return hashlib.sha256(contents.encode()).hexdigest()

def create_block_frame(root, block, col):
    # Create GUI frame displaying block info
    frame = tk.Frame(root, relief='ridge', borderwidth=2, padx=10, pady=10)
    frame.grid(row=0, column=col, padx=10, pady=10)
    tk.Label(frame, text=f"Block {block.index}", font=("Arial", 14, "bold")).pack()
    data_label = tk.Label(frame, text=f"Data: {block.data}", wraplength=180)
    data_label.pack()
    prev_label = tk.Label(frame, text=f"Prev Hash:\n{block.previousHash[:20]}...", wraplength=180)
    prev_label.pack()
    hash_label = tk.Label(frame, text=f"Hash:\n{block.hash[:20]}...", wraplength=180)
    hash_label.pack()
    return frame, data_label, prev_label, hash_label

def update_display():
    # Update GUI labels for all blocks with current data and hashes
    for i, block in enumerate(blockchain):
        data_labels[i].config(text=f"Data: {block.data}")
        prev_labels[i].config(text=f"Prev Hash:\n{block.previousHash[:20]}...")
        hash_labels[i].config(text=f"Hash:\n{block.hash[:20]}...")
    
    # Check blockchain validity: each block's previousHash must match previous block's hash
    valid = True
    for i in range(1, len(blockchain)):
        if blockchain[i].previousHash != blockchain[i-1].hash:
            valid = False
            break

    # Update chain status label
    status_var.set("Chain Status: VALID" if valid else "Chain Status: BROKEN")
    print(f"[INFO] Chain validity checked: {'VALID' if valid else 'BROKEN'}")

def tamper_block1():
    # Tamper with Block 1's data and recalculate its hash
    print("[ACTION] Tampering Block 1 data...")
    block1.data = "Tampered Data"
    block1.hash = block1.calculate_hash()
    print(f"[INFO] New Block 1 hash: {block1.hash}")

    # Note: block2.previousHash is NOT updated, so blockchain breaks
    update_display()
    print("[RESULT] Blockchain broken because Block 2's previousHash doesn't match Block 1's new hash.")

# Create 3 linked blocks
block0 = Block(0, "Genesis Block")
block1 = Block(1, "Block 1 Data", block0.hash)
block2 = Block(2, "Block 2 Data", block1.hash)
blockchain = [block0, block1, block2]

root = tk.Tk()
root.title("Blockchain Visualization")

frames = []
data_labels = []
prev_labels = []
hash_labels = []

# Create GUI frames for each block
for i, block in enumerate(blockchain):
    f, d, p, h = create_block_frame(root, block, i)
    frames.append(f)
    data_labels.append(d)
    prev_labels.append(p)
    hash_labels.append(h)

status_var = tk.StringVar()
status_var.set("Chain Status: VALID")
status_label = tk.Label(root, textvariable=status_var, font=("Arial", 16, "bold"))
status_label.grid(row=1, column=0, columnspan=3, pady=10)

# Button to tamper block 1 and show effect on chain
btn = tk.Button(root, text="Tamper Block 1", command=tamper_block1)
btn.grid(row=2, column=1, pady=10)

root.mainloop()
