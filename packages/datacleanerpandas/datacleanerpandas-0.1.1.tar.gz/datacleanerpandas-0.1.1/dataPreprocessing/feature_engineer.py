
class FeatureEngineer:

    @staticmethod
    def add_product(df, col1, col2, new_col_name):
        df[new_col_name] = df[col1] * df[col2]
        return df

    @staticmethod
    def add_square(df, col, new_col_name):
        df[new_col_name] = df[col] ** 2
        return df

    @staticmethod
    def add_sum(df, col1, col2, new_col_name):
        df[new_col_name] = df[col1] + df[col2]
        return df



    @staticmethod
    def add_difference(df, col1, col2, new_col_name):
        df[new_col_name] = df[col1] - df[col2]
        return df
