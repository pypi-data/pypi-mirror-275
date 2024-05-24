import pandas as pd
def Filter(input_df,column,value,output_df):
    output_df = input_df[input_df[column]==value]
    return output_df
