import os
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# 1. Use Pathlib for robust path handling
# This gets the directory where the script is located
BASE_DIR = Path(__file__).resolve().parent

# Define output paths
save_path_1 = BASE_DIR / 'digital_disconnect.png'
save_path_2 = BASE_DIR / 'ai_market_growth.png'
save_path_3 = BASE_DIR / 'strategic_matrix.png'

try:
    plt.style.use('seaborn-v0_8-whitegrid') # Updated style name for newer Matplotlib
except:
    plt.style.use('ggplot')

def save_chart(fig, path):
    """Saves the figure, ensuring the directory exists and path is clean."""
    # Ensure the parent directory exists
    path.parent.mkdir(parents=True, exist_ok=True)
    
    try:
        print(f'Attempting to save to: {path}')
        # Converting Path object to string for Matplotlib compatibility
        fig.savefig(str(path), dpi=300, bbox_inches='tight')
        print(f'Successfully saved: {path.name}')
    except Exception as e:
        print(f'Error saving {path.name}: {e}')
    finally:
        plt.close(fig)

def create_bar_chart(path):
    fig, ax = plt.subplots(figsize=(8, 6))
    categories = ['Marketing Budget', 'Revenue Generated']
    percentages = [25, 5]
    colors = ['#e63946', '#457b9d']

    bars = ax.bar(categories, percentages, color=colors, width=0.5)
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval + 0.5, f'{yval}%', 
                ha='center', va='bottom', fontweight='bold')

    ax.set_ylim(0, 30)
    ax.set_ylabel('Percentage (%)')
    ax.set_title('The Digital Disconnect', fontsize=14, fontweight='bold', pad=15)
    save_chart(fig, path)

def create_growth_chart(path):
    fig, ax = plt.subplots(figsize=(9, 6))
    years = np.arange(2026, 2032)
    initial_value = 18.64
    cagr = 0.347
    values = [initial_value * ((1 + cagr) ** i) for i in range(len(years))]

    ax.plot(years, values, marker='o', color='#1d3557', linewidth=3)
    ax.fill_between(years, values, alpha=0.2, color='#457b9d')
    ax.set_title('Projected AI Retail Growth', fontweight='bold')
    save_chart(fig, path)

def create_matrix_chart(path):
    fig, ax = plt.subplots(figsize=(10, 6))
    labels = ['Omnichannel', 'Flagship+', 'B2B Pivot', 'Platform']
    data = np.array([22, 18, 12, 10])
    ax.bar(labels, data, color='#1d3557')
    ax.set_title('Strategic Evaluation', fontweight='bold')
    save_chart(fig, path)

if __name__ == '__main__':
    # Sanity check: Print current location
    print(f"Script location identified as: {BASE_DIR}")
    
    create_bar_chart(save_path_1)
    create_growth_chart(save_path_2)
    create_matrix_chart(save_path_3)