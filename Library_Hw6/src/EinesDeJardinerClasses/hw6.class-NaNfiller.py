#Create a preprocessor class that fills NaN with the mean value of the column in the columns:
#height, weight.

list_of_columns_to_fill=["height", "weight"]

class NanFiller:
    @staticmethod
    def Nan_Filler(df, columns_to_fill):
        for column in columns_to_fill:
            mean = df[column].mean()
            df[column] = df[column].fillna(mean)
        return df

Nanfiller = NanFiller()
df_train = Nanfiller.Nan_Filler(df_train, list_of_columns_to_fill)
df_train
