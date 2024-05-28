import pandas as pd

# read teh file from input_path, process and save in the output_path
# return a pandas df processed

def readAndProcessData(input_path, output_path , file_name):

    df = pd.read_csv(input_path, header=0)

    # change format of columns
    df['Month of din_instante'] = pd.to_datetime(df['Month of din_instante']).dt.strftime('%Y-%m')
    df['Day of din_instante'] = df['Day of din_instante'].astype(str)
    df['datetime'] = df['Month of din_instante'] + '-' + df['Day of din_instante']
    df['datetime'] = pd.to_datetime(df['datetime'])
    df.drop(['Month of din_instante', 'Day of din_instante'], axis=1, inplace=True)
    df = df.rename(columns={"Val Geração FIXED DAY 2": "SolarPower"})

    # save to a new csv file
    df.to_csv(output_path + file_name, index=False)