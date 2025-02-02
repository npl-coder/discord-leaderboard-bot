from .config import worksheet
import pandas as pd

def get_df():
    # Get all records including headers
    all_data = worksheet.get_all_values()
    if not all_data:
        print("Warning: No data found in sheet")
        return pd.DataFrame()
        
    # Get headers from first row
    headers = all_data[0]
    print(f"Sheet headers: {headers}")
    
    # Get actual data (excluding headers)
    data = all_data[1:]
    if not data:
        print("Warning: No data rows found")
        return pd.DataFrame(columns=headers)
    
    # Create DataFrame
    df = pd.DataFrame(data, columns=headers)
    print(f"Data sample:\n{df.head()}")
    return df

def get_top_k_individual(k: int):
    df = get_df()  # Get fresh data
    if df.empty:
        print("Warning: DataFrame is empty")
        return []
        
    # Make sure Score column exists and is numeric
    if 'Score' in df.columns:
        df['Score'] = pd.to_numeric(df['Score'], errors='coerce')
    else:
        print(f"Warning: Score column not found. Available columns: {df.columns.tolist()}")
        return []
        
    sorted_data = df.sort_values(by="Score", ascending=False).head(k)
    list_of_dicts = sorted_data.to_dict(orient='records')
    print(f"Returning data: {list_of_dicts}")
    return list_of_dicts


def get_top_k_place(place: str, k: int):
    df = get_df()  # Get fresh data
    if df.empty:
        print("Warning: DataFrame is empty")
        return []
        
    place = place.capitalize()
    if place in df.columns:
        top_k_places = df.groupby(place)["Score"].mean().sort_values(
            ascending=False).head(k).reset_index(name='Average Score')
        list_of_dicts = top_k_places.to_dict(orient="records")
        print(f"Returning data: {list_of_dicts}")
        return list_of_dicts
    else:
        print(f"Warning: {place} column not found. Available columns: {df.columns.tolist()}")
        return []


def add_new_user(name, username, province, district, school):
    new_user = [name, username, province, district, school, 0] # Score is 0 for new user
    worksheet.append_row(new_user)


def increase_score(username, increase_point):
    cell = worksheet.find(username)
    row_number = cell.row
    current_score = int(worksheet.cell(row_number, 6).value)
    new_score = current_score + increase_point
    worksheet.update_cell(row_number, 6, new_score)
    print(f"Updated {username}'s score to {new_score}")
    return (f"Updated {username}'s score to {new_score}")
