# d) Create at least two feature classes that transform some of the columns in the data set. 
# # Thesefeature classes need to have the same structure defined by an abstract parent class (Remember: polymorphism).

from abc import ABCMeta, abstractmethod

# Parent abstract class:

class Transformer(metaclass=ABCMeta):
    def _init_(self, df, column):
        self.df = df
        self.column = column

    @abstractmethod
    def transform_df(self):
        return NotImplementedError

# Child features classes:

from datetime import date

class age_to_birth_year(Transformer):
    @staticmethod
    def transform_df(df, column):
        df_copy = df.copy()
        age = df[column]
        today = date.today().year
        birth_year = today - age
        df_copy[column] = birth_year
        return df_copy

class heightcm_to_inches(Transformer):
    @staticmethod
    def transform_df(df, column):
        df_copy = df.copy()
        height = df[column]
        height_inches = 0.394 * height
        df_copy[column] = height_inches
        return df_copy