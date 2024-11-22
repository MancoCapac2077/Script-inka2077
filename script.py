import time
import random
import sys

def loading_bar(progress, total, prefix='', suffix='', length=50, fill='█', print_end="\r"):
    """Display a dynamic loading bar."""
    percent = f"{100 * (progress / float(total)):.1f}"
    filled_length = int(length * progress // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=print_end)
    if progress == total:
        print()

def simulate_hack():
    systems = [
        "Qorikancha Quantum Core",
        "Cusco Neural Network",
        "Inti Raymi AI Firewall",
        "Tahuantinsuyo Cyber Grid",
        "Andean Cloud Database"
    ]

    print("🌐 Connecting to advanced Incan systems...\n")
    time.sleep(2)

    for system in systems:
        print(f"🔍 Attempting to breach {system}...")
        time.sleep(random.uniform(1, 2))
        loading_bar(0, 100, prefix=f'Hacking {system}', suffix='Progress', length=30)
        for i in range(101):
            time.sleep(random.uniform(0.01, 0.03))  # Simulate progress
            loading_bar(i, 100, prefix=f'Hacking {system}', suffix='Complete', length=30)
        print(f"✅ {system} hacked successfully!\n")
        time.sleep(1)

    print("💾 Extracting critical data packets...\n")
    for _ in range(5):
        data_packet = f"Packet#{random.randint(1000, 9999)}: [Encrypted Stream: ##########]"
        print(data_packet)
        time.sleep(random.uniform(0.5, 1.0))

    print("\n🚀 Hack complete. Systems compromised.")
    print("🎉 Hacked successfully! Time to celebrate with a pachamanca! 🥔🌽🍖")
    
    # Resultados del hackoe: aHR0cHM6Ly9wYXN0ZWJpbi5jb20vZUI4Tlhhc3U=

if __name__ == "__main__":
    simulate_hack()
