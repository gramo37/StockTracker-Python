from bsedata.bse import BSE
import pickle
import pandas as pd
import time


# Store all data(dictionary) to .pkl file
def store_data_to_file(file_name):
    b = BSE()
    b = BSE(update_codes = True)
    data = b.getScripCodes()          # Get all the data from bseIndia
    file_name = file_name + ".pkl"    
    f = open(file_name,"wb")
    pickle.dump(data,f)
    f.close()

# store_data_to_file("file")    # Run this only once to store data in .pkl file

# This method returns price by taking the "key provided by user"
def find_price(key_provided_by_user):
    file_name = "file"
    c_data = {}
    b = BSE()
    file_name = file_name + ".pkl" 
    try:
        unpickled_df = pd.read_pickle(file_name)
    except:
        store_data_to_file("file")
        unpickled_df = pd.read_pickle(file_name)
        
    print(len(unpickled_df))
    for key, val in unpickled_df.items():
        if key_provided_by_user.lower() in val.lower() and "fund" not in val.lower():
            try:
                quote = b.getQuote(key)
                c_data[val] = quote["currentValue"]
            except Exception:
                pass
                # print("Not available")
    print(c_data)
    return(c_data)

# Testing of above code
# file_name = "file"
# codelist = find_price("IDFC")
# codelist = find_price("IDFC First Bank Ltd")


