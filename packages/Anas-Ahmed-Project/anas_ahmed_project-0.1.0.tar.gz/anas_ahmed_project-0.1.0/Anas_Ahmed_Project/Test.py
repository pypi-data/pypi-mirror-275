import pandas as pd 
import numpy as np 
from .Main import (
    MissingValueHandler,
    OutlierHandler,
    TextCleaner,
    CategoricalEncoder,
    DateTimeHandler,
    DataTypeConverter,
    Scaler
)

file_path ="synthetic_sample_data_minimal.csv"

df = pd.read_csv(file_path)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)


numeric_columns = df.select_dtypes(include=['number']).columns
columns=df[['Movie Id','Release Date','Budget in USD']]

while True:
    print("1 - Missing Value Handler")
    print("2 - Outlier Handler")
    print("3 - Scaler")
    print("4 - Text Cleaner")
    print("5 - Data Type Converter")
    print("6 - Categorical Encoder")
    print("7 - DateTime Handler")
    print("0 - Exit")

    choice = input("Enter the Submodule You want to Test: ")
    if choice == '1':
        print("DataFrame before handling missing values:")
        print(columns)

        print("\nStrategy 1: Fill with mean")
        mean_handler = MissingValueHandler(strategy='mean')
        df_mean_filled = mean_handler.fit_transform(columns)
        print(df_mean_filled)
        
        print("\nStrategy 2: Fill with median")
        median_handler = MissingValueHandler(strategy='median')
        df_median_filled = median_handler.fit_transform(columns)
        print(df_median_filled)
        
        print("\nStrategy 3: Fill with constant value 0")
        constant_handler = MissingValueHandler(strategy='constant', fill_value=0)
        df_constant_filled = constant_handler.fit_transform(columns)
        print(df_constant_filled)
        
        print("\nStrategy 4: Delete rows with missing values")
        delete_handler = MissingValueHandler(strategy='delete')
        df_deleted = delete_handler.fit_transform(columns)
        print(df_deleted)

    elif choice == '2':
        print("DataFrame before handling outliers:")
        print(df[numeric_columns])

        outlier_handler = OutlierHandler(threshold=1.5)
        df_corrected = outlier_handler.process_dataframe(df, numeric_columns)

        print("\nDataFrame after handling outliers:")
        print(df_corrected[numeric_columns])

    elif choice == '3':
        columns_to_scale = ['Budget in USD', 'Rating']
        data_to_scale = df[columns_to_scale]

        scaler_minmax = Scaler(method='minmax')
        scaled_data_minmax = scaler_minmax.fit_transform(data_to_scale)

        scaler_standard = Scaler(method='standard')
        scaled_data_standard = scaler_standard.fit_transform(data_to_scale)

        print("Original Data:")
        print(data_to_scale.head())

        print("\nMin-Max Scaled Data:")
        print(scaled_data_minmax.head())

        print("\nStandard Scaled Data:")
        print(scaled_data_standard.head())

    elif choice == '4':
        print('Before Cleaning Summary')
        print(df['Summary'])
        cleaner = TextCleaner()

        df['Summary_cleaned'] = df['Summary'].apply(cleaner.clean_text)

        print(df['Summary_cleaned'])

    elif choice == '5':
        print("Data types before conversion:")
        print(df.dtypes)

        converter = DataTypeConverter()

        df_numeric = converter.convert_to_numeric(df, df.columns)

        print("\nData types after converting to numeric:")
        print(df_numeric.dtypes)

        df_categorical = converter.convert_to_categorical(df_numeric, df_numeric.columns)

        print("\nData types after converting to categorical:")
        print(df_categorical.dtypes)

    elif choice == '6':
        print('Before Encoding')
        print(df[['Genre', 'Shooting Location']])
        encoder_label = CategoricalEncoder(encoding_type='label')
        encoder_label.fit(df, ['Genre', 'Shooting Location'])
        print("Label Encodings:")
        for column, encodings in encoder_label.label_encodings.items():
            print(f"{column}: {encodings}")

    elif choice == '7':
        print('Before')
        print(df['Release Date'])

        handler = DateTimeHandler()

        df_datetime = handler.convert_to_datetime(df, columns=['Release Date'])

        df_features = handler.extract_datetime_features(df_datetime, column='Release Date')

        print(df_features[['Release Date', 'year', 'month', 'day', 'hour', 'minute', 'second']])

    elif choice == '0':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")

