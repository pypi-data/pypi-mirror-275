import pandas as pd
import sys

def calculate_wellbeing_score(row):
    # Example formula to calculate wellbeing score
    score = (
        (24 - row['sns_usage']) * 0.2 +
        row['sleep_time'] * 0.3 +
        row['exercise_time'] * 0.3 -
        row['stress_level'] * 0.2
    )
    return score

def main():
    if len(sys.argv) != 2:
        print("Usage: wellbeing_calculator <path_to_csv>")
        sys.exit(1)
    
    csv_file = sys.argv[1]
    data = pd.read_csv(csv_file)
    
    if not all(col in data.columns for col in ['sns_usage', 'sleep_time', 'exercise_time', 'stress_level']):
        print("CSV file must contain columns: 'sns_usage', 'sleep_time', 'exercise_time', 'stress_level'")
        sys.exit(1)
    
    data['wellbeing_score'] = data.apply(calculate_wellbeing_score, axis=1)
    print(data[['user_id', 'wellbeing_score']])

if __name__ == "__main__":
    main()
