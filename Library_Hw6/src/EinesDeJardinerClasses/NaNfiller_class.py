#Create a preprocessor class that fills NaN with the mean value of the column in the columns:
#height, weight.



class NanFiller:
    @staticmethod
    def Nan_Filler(df, columns_to_fill):
        for column in columns_to_fill:
            mean = df[column].mean()
            df[column] = df[column].fillna(mean)
        return df
