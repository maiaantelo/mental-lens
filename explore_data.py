import pandas as pd

# 1. LOAD THE DATA (This defines 'df')
df = pd.read_csv("data/Combined Data.csv")

# 2. FILTER THE DATA (This defines 'anxiety_data')
# We use lowercase 'status' because that's how it is in the CSV
anxiety_data = df[df['status'] == 'Anxiety']

# 3. DEFINE THE AI ACTION
def simulate_ai_response(statement, status):
    if status == 'Anxiety':
        print(f"\n[AI MONITOR]: High-stress markers detected: '{statement[:50]}...'")
        print("---------- ACTION TRIGGERED ----------")
        print("AI: 'I've noticed your patterns indicate rising anxiety. Let's try the 5-4-3-2-1 Grounding Technique.'")
        print("1. Name 5 things you can see...")
    else:
        print("\n[AI MONITOR]: Baseline normal.")

# 4. RUN THE SIMULATION
print(f"Total Anxiety samples found: {len(anxiety_data)}")

# Test the first 3 samples
for i in range(3):
    sample_text = anxiety_data['statement'].iloc[i]
    sample_status = anxiety_data['status'].iloc[i]
    simulate_ai_response(sample_text, sample_status)