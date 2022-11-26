## b) Create a preprocessor class that removes those rows that contain NaN values in the columns: age,
#gender, ethnicity.
          

class NanRemover:
    @staticmethod
    def Nan_Remover(df, columns_to_remove):
        return df.dropna(subset=columns_to_remove, how='any')






