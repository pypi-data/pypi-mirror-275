from sklearn.preprocessing import OneHotEncoder, LabelEncoder


class CategoricalEncoder:
    def __init__(self):
        self.one_hot_encoder = None
        self.label_encoder = None

    def fit_one_hot(self, data):
        self.one_hot_encoder = OneHotEncoder(sparse_output=False)
        self.one_hot_encoder.fit(data)

    def transform_one_hot(self, data):
        if self.one_hot_encoder is None:
            raise ValueError("OneHotEncoder is not fitted yet. Call fit_one_hot first.")
        return self.one_hot_encoder.transform(data)

    def fit_transform_one_hot(self, data):
        self.fit_one_hot(data)
        return self.transform_one_hot(data)

    def fit_label(self, data):
        self.label_encoder = LabelEncoder()
        self.label_encoder.fit(data)

    def transform_label(self, data):
        if self.label_encoder is None:
            raise ValueError("LabelEncoder is not fitted yet. Call fit_label first.")
        return self.label_encoder.transform(data)

    def fit_transform_label(self, data):
        self.fit_label(data)
        return self.transform_label(data)
