## b) Create a preprocessor class that removes those rows that contain NaN values in the columns: age,
#gender, ethnicity.
          
list_of_columns_to_remove=["gender", "age", "ethnicity"]

class NanRemover:
    @staticmethod
    def Nan_Remover(df, columns_to_remove):
        return df.dropna(subset=columns_to_remove, how='any')


Nanremover = NanRemover()
df_train = Nanremover.Nan_Remover(df_train, list_of_columns_to_remove)
df_train



