from data_package import (
    remove_duplicates, 
    strip_whitespaces, 
    calculate_mean, 
    find_maximum, 
    find_minimum
)

def main():
    user_input = input("Enter a comma-separated list of numbers (e.g., 12, 5, 12, 8 , 21): ")
    raw_list = user_input.split(",") 

    stripped_list = strip_whitespaces(raw_list) 

    try:
        num_list = [float(x) for x in stripped_list]
        cleaned_data = remove_duplicates(num_list) 

        mean_val = calculate_mean(cleaned_data) 
        max_val = find_maximum(cleaned_data) 
        min_val = find_minimum(cleaned_data) 

        print(f"Cleaned and unique data: {cleaned_data}") 
        print("-" * 20)
        print(f"Mean: {mean_val:.2f}") 
        print(f"Maximum: {max_val}")

    except ValueError:
        print("Data Error: Please make sure you only enter numbers separated by commas.")

if __name__ == "__main__": 
    main()