import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")

SCOPED_CREDS = CREDS.with_scopes(SCOPE)

GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

SHEET = GSPREAD_CLIENT.open("love_sandwiches")

def get_sales_data():
    """ 
    Get sales figures input from the user.
    Run a While loop to collect a vaild string of data from the user
    via the terminal, which mst be a string of 6 numbers separated 
    by commas. The loop will repeatedly request data, until it is valid
    """
    while True:

        print("Please enter sales data from the last market.")
        print("Data should be six numbers, separated by commas.")
        print("Example: 10, 20, 30, 40, 50, 60 \n")

        data_str = input("Enter your data here: ")
    
        sales_data = data_str.split(",")

        if validate_data(sales_data):
            print("Your Data Is Valid!")
            break

    return sales_data


def validate_data(values):

    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,#
    or if there aren't exactly 6 values
    """
    try:
        [int(value) for value in values] 
        if len(values) != 6:

            raise ValueError(
                f"Exactly 6 Values required, you provided {len(values)}"
            )
        
    except ValueError as e:
        print(f"Invalid Data: {e}, please try again. \n")
        return False
    
    return True


def update_sales_worksheet(data):
    """ 
    update sales worksheet, add new row with the list data provided.
    """
    print("Updating Sales Worksheet.....\n")
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(data)
    print("Sales Worksheet Updated Successfully. \n")

data = get_sales_data()
sales_data = [int(num) for num in data] 

update_sales_worksheet(sales_data)
