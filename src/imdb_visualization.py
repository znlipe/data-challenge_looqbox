import pandas as pd
import matplotlib.pyplot as plt
import database as db


def load_imdb_movies():
    connection = db.get_connection()
    try:
        query = """
                SELECT *
                FROM IMDB_movies
                """
        df = pd.read_sql(query, connection)
        return df
    finally:
        connection.close()


def plot_top10_movies_by_metascore():
    movies_df = load_imdb_movies()
    print("Generating Metascore bar chart...")
    top_10 = (
        movies_df
        .dropna(subset=["Metascore"])
        .sort_values(by=["Metascore", "Votes"],
                     ascending=[False, False]
                     ).head(10)
    )

    chart_data = top_10.set_index("Title")["Metascore"]

    plt.figure(figsize=(10, 10))
    ax = chart_data.sort_values(ascending=True).plot(kind="barh")
    ax.bar_label(ax.containers[0], fmt="%.0f", padding=3)
    plt.title('Top 10 movies by Metascore')
    plt.xlabel("Metascore")
    plt.ylabel("Title")
    plt.tight_layout()
    plt.savefig("top10_movies_by_metascore.png", dpi=300,bbox_inches="tight")
    plt.show()
    plt.close()


def plot_scatter_revenue_metascore():
    movies_df = load_imdb_movies()
    print("Generating Revenue vs Metascore scatter plot...")
    scatter_df = movies_df[["Title", "RevenueMillions", "Metascore"]].copy()
    print(f"Original dataset shape: {movies_df.shape}")

    scatter_df = scatter_df.dropna(
        subset=["RevenueMillions", "Metascore"]
    )
    scatter_df = scatter_df[
        scatter_df["RevenueMillions"] > 0
    ]

    print(f"Cleaned scatter dataset shape: {scatter_df.shape}")

    plt.figure(figsize=(10, 8))
    plt.scatter(
        scatter_df["RevenueMillions"],
        scatter_df["Metascore"],
        alpha=0.6
    )
    # Log scale improves readability because revenue values are highly spread out.
    plt.xscale("log")

    plt.title("Revenue vs Metascore")
    plt.xlabel("Revenue in millions (log scale)")
    plt.ylabel("Metascore")
    plt.tight_layout()
    plt.savefig("revenue_vs_metascore.png", dpi=300,bbox_inches="tight")
    plt.show()
    plt.close()


if __name__ == '__main__':
    # Top 10 movies by Metascore
    plot_top10_movies_by_metascore()

    # Relationship between Revenue and Metascore
    plot_scatter_revenue_metascore()
