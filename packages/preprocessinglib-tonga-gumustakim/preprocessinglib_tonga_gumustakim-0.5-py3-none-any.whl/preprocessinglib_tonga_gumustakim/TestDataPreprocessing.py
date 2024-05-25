import unittest
import pandas as pd
from preprocessinglib_tonga_gumustakim.MissingValueHandler import MissingValueHandler
from preprocessinglib_tonga_gumustakim.FeatureEngineer import FeatureEngineer
from preprocessinglib_tonga_gumustakim.DateTimeHandler import DateTimeHandler
from preprocessinglib_tonga_gumustakim.DataTypeConverter import DataTypeConverter
from preprocessinglib_tonga_gumustakim.CategoricalEncoder import CategoricalEncoder
from preprocessinglib_tonga_gumustakim.OutlierHandler import OutlierHandler
from preprocessinglib_tonga_gumustakim.TextCleaner import TextCleaner
from preprocessinglib_tonga_gumustakim.Scaler import Scaler


class TestDataPreprocessing(unittest.TestCase):
    pd.set_option('display.max_columns', None)
    data = pd.read_csv('C:/Users/EMRULLAH/Downloads/synthetic_sample_data_minimal.csv')

    @classmethod
    def setUpClass(cls):
        filepath = r"C:\Users\EMRULLAH\Downloads\synthetic_sample_data_minimal.csv"
        cls.data = pd.read_csv(filepath)

    def test_detect_missing_values(self):
        missing_handler = MissingValueHandler()
        result = missing_handler.detect_missing_values(self.data)
        expected_result = self.data.isnull().sum()
        self.assertTrue(result.equals(expected_result))
        print("Detected Missing Values:")
        print(result)

    def test_fill_missing_values(self):
        numeric_columns = self.data.select_dtypes(include=['number']).columns
        filled_data = self.data.copy()
        filled_data[numeric_columns] = self.data[numeric_columns].fillna(self.data[numeric_columns].mean())
        self.assertFalse(filled_data.isnull().values.any())
        print("Data after filling missing values:")
        print(filled_data.head())

    def test_remove_missing_values(self):
        cleaned_data = MissingValueHandler.remove_missing_values(self.data)
        self.assertFalse(cleaned_data.isnull().values.any())
        print("Data after removing missing values:")
        print(cleaned_data.head())

    def test_create_new_features(self):
        data_with_new_feature = FeatureEngineer.create_new_features(self.data, column1='Budget in USD',
                                                                    column2='Awards')
        self.assertTrue('NewFeature' in data_with_new_feature.columns)
        print("Data with new feature:")
        print(data_with_new_feature.head())

    def test_extract_date_features(self):
        data = self.data.copy()
        data['Date'] = pd.to_datetime(data['Release Date'], format='%d/%m/%Y')
        date_with_features = DateTimeHandler.extract_date_features(data, column='Date')

        self.assertTrue('Year' in date_with_features.columns)
        self.assertTrue('Month' in date_with_features.columns)
        self.assertTrue('Day' in date_with_features.columns)
        self.assertTrue('DayOfWeek' in date_with_features.columns)
        print("Data with extracted date features:")
        print(date_with_features.head())

    def test_convert_to_numeric(self):
        columns_to_convert = ['Budget in USD', 'Awards', 'Popular']
        numeric_data = DataTypeConverter.convert_to_numeric(self.data.copy(), columns=columns_to_convert)

        for column in columns_to_convert:
            self.assertTrue(pd.api.types.is_numeric_dtype(numeric_data[column]))
        print("Data after converting to numeric:")
        print(numeric_data.head())

    def test_convert_to_categorical(self):
        data = self.data.copy()
        columns_to_convert = ['Genre', 'Shooting Location']
        converted_data = DataTypeConverter.convert_to_categorical(data, columns=columns_to_convert)

        for column in columns_to_convert:
            self.assertTrue(isinstance(converted_data[column].dtype, pd.CategoricalDtype))
        print("Data after converting to categorical:")
        print(converted_data.head())

    def test_one_hot_encode(self):
        data = self.data.copy()
        encoded_data = CategoricalEncoder.one_hot_encode(data, columns=['Genre', 'Shooting Location'])

        for column in ['Genre', 'Shooting Location']:
            self.assertTrue(any(col.startswith(column) for col in encoded_data.columns))
        print("Data after one-hot encoding:")
        print(encoded_data.head())

    def test_label_encode(self):
        data = self.data.copy()
        label_encoded_data = CategoricalEncoder.label_encode(data, column='Genre')

        self.assertTrue(pd.api.types.is_integer_dtype(label_encoded_data['Genre']))
        print("Data after label encoding:")
        print(label_encoded_data.head())

    def test_handle_outliers(self):
        outliers_removed_data = OutlierHandler.handle_outliers(self.data.select_dtypes(include=['number']),
                                                               method='drop')
        self.assertFalse(outliers_removed_data.isnull().values.any())
        print("Data after handling outliers:")
        print(outliers_removed_data.head())

    def test_clean_text(self):
        # Örnek bir metin oluştur
        text_column = "Summary"

        # Metni temizle
        cleaned_text = TextCleaner.clean_text(self.data[text_column].values)

        # Temizlenmiş metni kontrol et
        print("Cleaned text:")
        print(cleaned_text)

    def test_standardize_data(self):
        # Ölçeklendirme için bir veri seti seç
        data_to_scale = self.data.select_dtypes(include=['number'])

        # Veriyi standartlaştır
        standardized_data = Scaler.standardize_data(data_to_scale)

        # Standartlaştırılmış veriyi kontrol et
        print("Standardized data:")
        print(standardized_data.head())

    def test_normalize_data(self):
        # Ölçeklendirme için bir veri seti seç
        data_to_scale = self.data.select_dtypes(include=['number'])

        # Veriyi normalize et
        normalized_data = Scaler.normalize_data(data_to_scale)

        # Normalize edilmiş veriyi kontrol et
        print("Normalized data:")
        print(normalized_data.head())

    if __name__ == '__main__':
        unittest.main()
