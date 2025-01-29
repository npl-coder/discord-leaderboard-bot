from .config import worksheet
import pandas as pd

df = pd.DataFrame(worksheet.get_all_records())


def get_top_k_individual(k: int):
    sorted_data = df.sort_values(by="Score").head(k)
    # Converting Pandas DF to list of dict so that it becomes easier for sending API Response
    list_of_dicts = sorted_data.to_dict(orient='records')
    return list_of_dicts


def get_top_k_place(place: str, k: int):
    place = place.capitalize()
    top_k_places = df.groupby(place)["Score"].mean().sort_values(
        ascending=False).head(k).reset_index(name='Average Score')
    list_of_dicts = top_k_places.to_dict(orient="records")
    return list_of_dicts


def add_new_user(name, username, province, district, school):
    new_user = [name, username, province, district, school, 0] # Score is 0 for new user
    worksheet.append_row(new_user)


def increase_score(username, increase_point):
    cell = worksheet.find(username)
    row_number = cell.row
    current_score = int(worksheet.cell(row_number, 6).value)
    new_score = current_score + increase_point
    worksheet.update_cell(row_number, 6, new_score)
    return (f"Updated {username}'s score to {new_score}")


