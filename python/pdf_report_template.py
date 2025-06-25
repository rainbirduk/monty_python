import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib import gridspec

# Sample data
data = np.random.normal(loc=50, scale=10, size=100)
iterations = 500

# Summary statistics (transposed)
summary = {
    "Mean": np.mean(data),
    "Median": np.median(data),
    "Std Dev": np.std(data),
    "Min": np.min(data),
    "Max": np.max(data),
    "Q1": np.percentile(data, 25),
    "Q3": np.percentile(data, 75),
}
summary_df = pd.DataFrame(summary, index=["Value"]).round(2)

# A5 landscape size in inches
fig = plt.figure(figsize=(8.3, 5.8))  # A5 landscape
gs = gridspec.GridSpec(4, 1, height_ratios=[0.15, 2, 0.6, 0.25])  # [title, plot, table, text]

# Title
fig.text(0.5, 0.96, "Summary Report", ha="center", va="top", fontsize=16, weight="bold")

# Boxplot (takes up 2/3 of the page)
ax_plot = fig.add_subplot(gs[1])
ax_plot.boxplot(data, vert=True)
ax_plot.set_title("Boxplot of Sample Data", fontsize=12)
ax_plot.set_xticks([])

# Table (transposed and margin-aware)
ax_table = fig.add_subplot(gs[2])
ax_table.axis("off")
table = ax_table.table(
    cellText=summary_df.values,
    colLabels=summary_df.columns,
    rowLabels=summary_df.index,
    loc="upper left",
    cellLoc="center"
)
table.scale(1.0, 1.2)

# Custom text
ax_text = fig.add_subplot(gs[3])
ax_text.axis("off")
ax_text.text(0, 0.8, f"Number of iterations: {iterations}", fontsize=10)
ax_text.text(0, 0.4, "Generated using Python and Matplotlib", fontsize=9)


# Save to PDF
with PdfPages("summary_report.pdf") as pdf:
    pdf.savefig(fig)
    plt.close()

print("PDF saved as summary_report.pdf")
