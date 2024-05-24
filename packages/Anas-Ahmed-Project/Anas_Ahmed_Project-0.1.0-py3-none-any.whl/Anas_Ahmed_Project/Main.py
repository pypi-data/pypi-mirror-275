import pandas as pd  
import numpy as np 
import re
import nltk
from nltk.corpus import stopwords

class MissingValueHandler:
    def __init__(self, strategy='mean', fill_value=None):
        self.strategy = strategy
        self.fill_value = fill_value
        self.fill_values_ = {}

    def fit(self, df):
        if self.strategy == 'mean':
            self.fill_values_ = df.select_dtypes(include=['number']).mean()
        elif self.strategy == 'median':
            self.fill_values_ = df.select_dtypes(include=['number']).median()
        elif self.strategy == 'constant':
            if self.fill_value is None:
                raise ValueError("fill_value must be specified when strategy is 'constant'")
            self.fill_values_ = {col: self.fill_value for col in df.columns}
        elif self.strategy == 'delete':
            self.fill_values_ = {}
        else:
            raise ValueError("Invalid strategy. Supported strategies: 'mean', 'median', 'constant', 'delete'")

    def transform(self, df):
        if self.strategy == 'delete':
            return df.dropna()
        else:
            return df.fillna(self.fill_values_)

    def fit_transform(self, df):
        self.fit(df)
        return self.transform(df)

class OutlierHandler:
    def __init__(self, threshold=1.5):
        self.threshold = threshold

    def detect_outliers(self, series):
        Q1 = series.quantile(0.25)
        Q3 = series.quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - self.threshold * IQR
        upper_bound = Q3 + self.threshold * IQR
        return (series < lower_bound) | (series > upper_bound)

    def correct_outliers(self, series):
        Q1 = series.quantile(0.25)
        Q3 = series.quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - self.threshold * IQR
        upper_bound = Q3 + self.threshold * IQR
        corrected_series = series.copy()
        corrected_series[series < lower_bound] = lower_bound
        corrected_series[series > upper_bound] = upper_bound
        return corrected_series

    def process_dataframe(self, df, columns):
        df_corrected = df.copy()
        for column in columns:
            outliers = self.detect_outliers(df_corrected[column])
            print(f'Outliers detected in column {column}:')
            print(df_corrected[column][outliers])
            df_corrected[column] = self.correct_outliers(df_corrected[column])
        return df_corrected

class TextCleaner:
    def __init__(self, remove_stopwords=True, use_stemming=False, use_lemmatization=True):
        self.remove_stopwords = remove_stopwords
        self.use_stemming = use_stemming
        self.use_lemmatization = use_lemmatization
        
        self.stopwords = set(stopwords.words('english')) if remove_stopwords else set()
        self.stemmer = nltk.PorterStemmer() if use_stemming else None
        self.lemmatizer = nltk.WordNetLemmatizer() if use_lemmatization else None

    def clean_text(self, text):
        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)
        text = re.sub(r'\d+', '', text)
        words = text.split()
        if self.remove_stopwords:
            words = [word for word in words if word not in self.stopwords]
        if self.use_stemming:
            words = [self.stemmer.stem(word) for word in words]
        elif self.use_lemmatization:
            words = [self.lemmatizer.lemmatize(word) for word in words]
        cleaned_text = ' '.join(words)
        return cleaned_text

class CategoricalEncoder:
    def __init__(self, encoding_type='onehot'):
        if encoding_type not in ['onehot', 'label']:
            raise ValueError("Invalid encoding type. Supported types: 'onehot', 'label'")
        self.encoding_type = encoding_type
        self.label_encodings = {}

    def fit(self, df, columns):
        if self.encoding_type == 'label':
            for column in columns:
                self.label_encodings[column] = {label: idx for idx, label in enumerate(df[column].unique())}

    def transform(self, df, columns):
        df_copy = df.copy()
        if self.encoding_type == 'onehot':
            df_copy = pd.get_dummies(df_copy, columns=columns)
        elif self.encoding_type == 'label':
            for column in columns:
                df_copy[column] = df_copy[column].map(self.label_encodings[column])
        return df_copy

    def fit_transform(self, df, columns):
        self.fit(df, columns)
        return self.transform(df, columns)

class DateTimeHandler:
    def convert_to_datetime(self, df, columns):
        for column in columns:
            df[column] = pd.to_datetime(df[column], errors='coerce', dayfirst=True)
        return df
    
    def extract_datetime_features(self, df, column):
        df['year'] = df[column].dt.year.astype('Int64')
        df['month'] = df[column].dt.month.astype('Int64')
        df['day'] = df[column].dt.day.astype('Int64')
        df['hour'] = df[column].dt.hour.astype('Int64')
        df['minute'] = df[column].dt.minute.astype('Int64')
        df['second'] = df[column].dt.second.astype('Int64')
    
        # Fill NaN values for rows where 'Release Date' couldn't be converted
        df.loc[df[column].isnull(), ['year', 'month', 'day', 'hour', 'minute', 'second']] = np.nan
    
        return df
    

class DataTypeConverter:
    def convert_to_numeric(self, df, columns):
        for column in columns:
            df[column] = pd.to_numeric(df[column], errors='coerce')
        return df
    
    def convert_to_categorical(self, df, columns):
        for column in columns:
            df[column] = df[column].astype('category')
        return df

class Scaler:
    def __init__(self, method='minmax'):
        self.method = method
        self.params = {}

    def fit(self, data):
        if self.method == 'minmax':
            self.params['min'] = data.min()
            self.params['max'] = data.max()
        elif self.method == 'standard':
            self.params['mean'] = data.mean()
            self.params['std'] = data.std()
        else:
            raise ValueError("Unsupported scaling method. Use 'minmax' or 'standard'.")

    def transform(self, data):
        if self.method == 'minmax':
            return (data - self.params['min']) / (self.params['max'] - self.params['min'])
        elif self.method == 'standard':
            return (data - self.params['mean']) / self.params['std']

    def fit_transform(self, data):
        self.fit(data)
        return self.transform(data)

    def inverse_transform(self, scaled_data):
        if self.method == 'minmax':
            return scaled_data * (self.params['max'] - self.params['min']) + self.params['min']
        elif self.method == 'standard':
            return scaled_data * self.params['std'] + self.params['mean']