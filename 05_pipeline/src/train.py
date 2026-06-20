import os, random, argparse
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import pandas as pd

def set_seed(seed):
    os.environ['PYTHONHASHSEED'] = str(seed)   # 1. Python hashing
    random.seed(seed)                          # 2. Python random
    np.random.seed(seed)                       # 3. NumPy
    # 4. framework + GPU (uncomment if using PyTorch):
    # import torch
    # torch.manual_seed(seed); torch.cuda.manual_seed_all(seed)
    # torch.use_deterministic_algorithms(True)

def main(seed=42):
    set_seed(seed)
    df = pd.read_csv('data/citizen_security_lima_1000.csv')

    # Variable objetivo
    target = "Tipo_Evento"

    # Features
    X = df.drop(columns=[target])

    # Target
    y = df[target]

    # Codificar target
    le = LabelEncoder()
    y = le.fit_transform(y)


    cat_cols = ["Distrito"]

    num_cols = [c for c in X.columns if c not in cat_cols]

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), num_cols),
            ("cat", OneHotEncoder(handle_unknown="ignore"), cat_cols)
        ]
    )  


    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.25,
        stratify=y,
        random_state=42
    )


    model = Pipeline([
        ("preprocessor", preprocessor),
        ("classifier",
         LogisticRegression(
             multi_class="multinomial",
             solver="lbfgs",
             max_iter=1000,
             random_state=seed
         ))
    ])


    model.fit(X_train, y_train)

    acc = accuracy_score(y_test, model.predict(X_test))
    print(f'seed={seed}  accuracy={acc:.4f}')
    return model, acc

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--seed', type=int, default=42)
    main(ap.parse_args().seed)
