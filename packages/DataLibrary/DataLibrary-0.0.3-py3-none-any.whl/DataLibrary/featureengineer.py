class FeatureEngineer:
    def create_interaction_term(self, data, column1, column2):
        data[f'{column1}x{column2}'] = data[column1] * data[column2]
        return data

    def create_ratio_term(self, data, column1, column2):
        data[f'{column1}div{column2}'] = data[column1] / data[column2]
        return data