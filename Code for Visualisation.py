
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data1 = {
    "Training on": ["Dataset A", "Dataset B", "Dataset A + B"],
    "Box": [0.872, 0.631, 0.639],
    "Precision": [0.749, 0.477, 0.568],
    "Recall": [0.816, 0.536, 0.603],
    "mAP50": [0.605, 0.303, 0.308]
}

data2 = {
    "Evaluation on": ["Dataset A", "Dataset B", "Dataset A + B"],
    "Box": [0.614, 0.579, 0.639],
    "Precision": [0.651, 0.521, 0.568],
    "Recall": [0.280, 0.555, 0.603],
    "mAP50": [0.336, 0.555, 0.308]
}

df1 = pd.DataFrame(data1).set_index("Training on")
df2 = pd.DataFrame(data2).set_index("Evaluation on")

combined = pd.DataFrame({
    "Dataset A (eval on A)": df1.loc["Dataset A"],
    "Dataset B (eval on B)": df1.loc["Dataset B"],
    "Dataset A+B (eval on A)": df2.loc["Dataset A"],
    "Dataset A+B (eval on B)": df2.loc["Dataset B"],
    "Dataset A+B (eval on A+B)": df2.loc["Dataset A + B"],
})


plt.figure(figsize=(10, 6))
sns.heatmap(combined, annot=True, cmap="YlGnBu", fmt=".3f",
            annot_kws={"size": 10, "weight": "bold"})
plt.title("Model Performance (Training vs Evaluation)", fontsize=14, weight="bold")
plt.yticks(rotation=0, fontsize=11, weight="bold")
plt.xticks(rotation=30, ha="right", fontsize=10, weight="bold")
plt.tight_layout()
plt.savefig("/Users/Joc/Downloads/training_eval_combined.png", dpi=300)
plt.show()
