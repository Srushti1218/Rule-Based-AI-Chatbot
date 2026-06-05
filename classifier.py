import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, f1_score, accuracy_score

def run_classification_pipeline():
    print("====================================================")
    print("  PROJECT 2: SUPERVISED LEARNING PIPELINE (KNN)      ")
    print("====================================================\n")
    
    # 1. INPUT: Load Raw Material (The Iris Benchmark)
    iris = load_iris()
    X = iris.data  # Features: Sepal/Petal Length & Width
    y = iris.target  # Labels: Setosa (0), Versicolor (1), Virginica (2)
    
    # 2. PROCESS PHASE A: Structural Integrity (The Split)
    # Fixed parameter name from random_content_id to random_state
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )
    print(f"[INFO] Dataset split successfully.")
    print(f"       Training samples: {X_train.shape[0]} | Testing samples: {X_test.shape[0]}\n")
    
    # 3. PROCESS PHASE B: Feature Scaling (StandardScaler)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # 4. PROCESS PHASE C: Tuning & Instantiating Algorithm (K-Nearest Neighbors)
    k_value = 5
    model = KNeighborsClassifier(n_neighbors=k_value)
    
    # Fit (Memorize patterns/map)
    model.fit(X_train_scaled, y_train)
    
    # Predict (Apply decision boundary logic)
    predictions = model.predict(X_test_scaled)
    
    # 5. OUTPUT: Diagnostic Validation Matrix
    print("---------------- METRIC EVALUATION ----------------")
    accuracy = accuracy_score(y_test, predictions)
    print(f"Overall Accuracy: {accuracy * 100:.2f}%")
    
    f1 = f1_score(y_test, predictions, average='macro')
    print(f"Macro F1 Score:   {f1:.4f}\n")
    
    print("Confusion Matrix:")
    cm = confusion_matrix(y_test, predictions)
    cm_df = pd.DataFrame(cm, index=iris.target_names, columns=iris.target_names)
    print(cm_df)
    print("---------------------------------------------------\n")

if __name__ == "__main__":
    run_classification_pipeline()