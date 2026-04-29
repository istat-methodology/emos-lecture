import matplotlib as mpl
import matplotlib.pyplot as plt

def plot_division_match(codes, matching):
    norm = mpl.colors.Normalize(vmin=0, vmax=1)
    cmap = plt.cm.RdYlGn

    fig, ax = plt.subplots(figsize=(16, 7))

    colors = cmap(norm(matching))

    ax.bar(codes, matching, color=colors, alpha=0.9)

    ax.set_xlabel("Division")
    ax.set_ylabel("Average Match@5")
    ax.set_title("Average Match@5 by Division")

    plt.setp(ax.get_xticklabels(), rotation=90, ha="center")

    ax.grid(True, axis='y', linestyle='--', alpha=0.7)

    ax.set_xlim(-0.9, len(codes)-0.1)

    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    cbar = fig.colorbar(sm, ax=ax)
    cbar.set_label("Match@5 Value")

    fig.tight_layout()
    plt.show()


def plot_thresholds(similarity_thresholds, n_classified, matching):

    fig, ax1 = plt.subplots(figsize=(12, 6))

    ax1.plot(similarity_thresholds, n_classified, color="tab:blue", marker="o", label="Classified")
    ax1.set_xlabel("Similarity Threshold")
    ax1.set_ylabel("Classified Count", color="tab:blue")
    ax1.tick_params(axis="y", labelcolor="tab:blue")

    ax2 = ax1.twinx()
    ax2.plot(similarity_thresholds, matching, color="tab:red", marker="s", label="Matching Ratio")
    ax2.set_ylabel("Matching Ratio", color="tab:red")
    ax2.tick_params(axis="y", labelcolor="tab:red")

    plt.title("Effect of Similarity Threshold on Classification and Matching")

    ax1.grid(True, linestyle="--", alpha=0.5)
    fig.tight_layout()

    plt.show()
