
import pandas as pd
from EinesDeJardinerClasses.model_class import RandForModel

file_path = "/Users/javier/Desktop/BSE/computing_for_DS/3_python/Hw6/sample_diabetes_mellitus_data.csv"
df = pd.read_csv(file_path)
df = df.dropna(how="any")
target = "diabetes_mellitus"
features = ['age', 'height', 'weight', 'aids', 'cirrhosis', 'hepatic_failure',
            'immunosuppression', 'leukemia', 'lymphoma',
            'solid_tumor_with_metastasis']
SEED = 1

hyperpars = {
    "n_estimators":10,
    "criterion": "gini",
    "max_depth":10,
    "n_jobs":2,
    "random_state":SEED
}

model = RandForModel(features, target, hyperpars)
model.train(df)
df["prediction"] = model.predict(df)[:, 1]
print(df[df[target] == 1])