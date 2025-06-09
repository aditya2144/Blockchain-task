import random
from collections import Counter
import tkinter as tk

def simulate_consensus():
    # Create mock miners with random computational power for PoW
    miners = [
        {'name': 'MinerA', 'power': random.randint(50, 100)},
        {'name': 'MinerB', 'power': random.randint(50, 100)},
        {'name': 'MinerC', 'power': random.randint(50, 100)}
    ]
    # Create mock stakers with random stake for PoS
    stakers = [
        {'name': 'StakerA', 'stake': random.randint(100, 1000)},
        {'name': 'StakerB', 'stake': random.randint(100, 1000)},
        {'name': 'StakerC', 'stake': random.randint(100, 1000)}
    ]
    # Voters and delegates for DPoS voting
    voters = ['Voter1', 'Voter2', 'Voter3']
    delegates = ['DelegateA', 'DelegateB', 'DelegateC']

    # Simulate voting by randomly choosing delegates
    votes = [random.choice(delegates) for _ in voters]
    vote_counts = Counter(votes)
    selected_delegate, max_votes = vote_counts.most_common(1)[0]

    # Select PoW winner by highest power
    pow_winner = max(miners, key=lambda x: x['power'])
    # Select PoS winner by highest stake
    pos_winner = max(stakers, key=lambda x: x['stake'])

    # Update GUI with participants info and results
    miners_text = '\n'.join([f"{m['name']}: Power = {m['power']}" for m in miners])
    stakers_text = '\n'.join([f"{s['name']}: Stake = {s['stake']}" for s in stakers])
    votes_text = ', '.join([f"{v}→{d}" for v, d in zip(voters, votes)])

    miners_label.config(text=miners_text)
    stakers_label.config(text=stakers_text)
    voters_label.config(text=votes_text)

    pow_result.config(text=f"Selected Miner: {pow_winner['name']} (Power: {pow_winner['power']})")
    pos_result.config(text=f"Selected Staker: {pos_winner['name']} (Stake: {pos_winner['stake']})")
    dpos_result.config(text=f"Selected Delegate: {selected_delegate} (Votes: {max_votes})")

    pow_logic.config(text="PoW Logic: Miner with highest computational power wins.")
    pos_logic.config(text="PoS Logic: Staker with highest stake gets selected.")
    dpos_logic.config(text="DPoS Logic: Delegate with most votes elected by voters.")

    # Console logs for transparency and debugging
    print("\n--- Consensus Simulation Run ---")
    print("Miners (PoW):", miners)
    print("Stakers (PoS):", stakers)
    print("Votes (DPoS):", votes)
    print(f"PoW selected: {pow_winner['name']} with power {pow_winner['power']}")
    print(f"PoS selected: {pos_winner['name']} with stake {pos_winner['stake']}")
    print(f"DPoS selected: {selected_delegate} with votes {max_votes}")

root = tk.Tk()
root.title("Consensus Mechanism Simulation")

tk.Label(root, text="Proof of Work (PoW) - Miners and Power", font=("Arial", 12, "bold")).grid(row=0, column=0, sticky="w")
miners_label = tk.Label(root, text="", font=("Courier", 11))
miners_label.grid(row=1, column=0, sticky="w")

tk.Label(root, text="Proof of Stake (PoS) - Stakers and Stake", font=("Arial", 12, "bold")).grid(row=0, column=1, sticky="w")
stakers_label = tk.Label(root, text="", font=("Courier", 11))
stakers_label.grid(row=1, column=1, sticky="w")

tk.Label(root, text="Delegated Proof of Stake (DPoS) - Voter Votes", font=("Arial", 12, "bold")).grid(row=0, column=2, sticky="w")
voters_label = tk.Label(root, text="", font=("Courier", 11))
voters_label.grid(row=1, column=2, sticky="w")

pow_result = tk.Label(root, text="", font=("Arial", 11, "bold"), fg="green")
pow_result.grid(row=2, column=0, sticky="w", pady=(10,0))
pow_logic = tk.Label(root, text="", font=("Arial", 10), wraplength=300)
pow_logic.grid(row=3, column=0, sticky="w")

pos_result = tk.Label(root, text="", font=("Arial", 11, "bold"), fg="blue")
pos_result.grid(row=2, column=1, sticky="w", pady=(10,0))
pos_logic = tk.Label(root, text="", font=("Arial", 10), wraplength=300)
pos_logic.grid(row=3, column=1, sticky="w")

dpos_result = tk.Label(root, text="", font=("Arial", 11, "bold"), fg="purple")
dpos_result.grid(row=2, column=2, sticky="w", pady=(10,0))
dpos_logic = tk.Label(root, text="", font=("Arial", 10), wraplength=300)
dpos_logic.grid(row=3, column=2, sticky="w")

btn_simulate = tk.Button(root, text="Run Simulation", command=simulate_consensus)
btn_simulate.grid(row=4, column=1, pady=20)

simulate_consensus()  # initial run

root.mainloop()
