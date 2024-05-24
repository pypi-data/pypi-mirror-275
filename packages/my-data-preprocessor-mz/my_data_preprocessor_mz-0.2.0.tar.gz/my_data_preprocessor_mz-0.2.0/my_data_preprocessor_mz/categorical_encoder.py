from sklearn.preprocessing import OneHotEncoder, LabelEncoder
import pandas as pd


class CategoricalEncoder:
    @staticmethod
    def one_hot_encode(df, columns):

        df_encoded = df.copy()
        encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
        encoded_columns = pd.DataFrame(encoder.fit_transform(df_encoded[columns]),
                                       columns=encoder.get_feature_names_out(columns))
        df_encoded = pd.concat([df_encoded, encoded_columns], axis=1)
        df_encoded.drop(columns, axis=1, inplace=True)
        return df_encoded

    @staticmethod
    def label_encode(df, columns):

        df_encoded = df.copy()
        encoder = LabelEncoder()
        for column in columns:
            df_encoded[column] = encoder.fit_transform(df_encoded[column])
        return df_encoded

