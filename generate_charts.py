import os
import matplotlib.pyplot as plt
import numpy as np
# Set style for a professional business report look
plt.style.use('seaborn-v0_8-whitegrid')

# =========================================================
# Graph 1: The Digital Disconnect (Spend vs. Return)
# =========================================================
fig1, ax1 = plt.subplots(figsize=(8, 6))
categories = ['Marketing Budget Consumed', 'Total Revenue Generated']
percentages = [25, 5]
colors = ['#e63946', '#457b9d']

# Create the bars
bars = ax1.bar(categories, percentages, color=colors, width=0.5)

# Add data labels on top of the bars
for bar in bars:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, yval + 0.5, f'{yval}%', 
             ha='center', va='bottom', fontsize=12, fontweight='bold')

# Formatting
ax1.set_ylim(0, 30)
ax1.set_ylabel('Percentage (%)', fontsize=12)
ax1.set_title('The Digital Disconnect: Online Channel Spend vs. Return', 
              fontsize=14, fontweight='bold', pad=15)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

# Get the folder where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Create an absolute path for the image
save_path_1 = os.path.join(script_dir, 'digital_disconnect.png')

plt.tight_layout()
plt.savefig(save_path_1, dpi=300)
plt.close(fig1)
# =========================================================
# Graph 2: AI in Retail Market Growth (2026-2031)
# =========================================================
fig2, ax2 = plt.subplots(figsize=(9, 6))
years = np.arange(2026, 2032)
initial_value = 18.64
cagr = 0.347 # 34.7% compound annual growth rate
values = [initial_value * ((1 + cagr) ** i) for i in range(len(years))]

# Create line and shaded area chart
ax2.plot(years, values, marker='o', color='#1d3557', linewidth=3, markersize=8)
ax2.fill_between(years, values, alpha=0.2, color='#457b9d')

# Add data labels for the first and last year
for i, (year, val) in enumerate(zip(years, values)):
    if i == 0 or i == len(years) - 1:
        ax2.text(year, val + 3, f'${val:.1f}B', ha='center', va='bottom', 
                 fontsize=11, fontweight='bold')

# Formatting
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Market Size (Billions USD)', fontsize=12)
ax2.set_title('Projected Growth: AI in Retail Market (34.7% CAGR)', 
              fontsize=14, fontweight='bold', pad=15)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.set_xticks(years)

save_path_2 = os.path.join(script_dir, 'ai_market_growth.png')

plt.tight_layout()
plt.savefig(save_path_2, dpi=300)
plt.close(fig2)
# =========================================================
# Graph 3: Strategic Alternatives Evaluation Matrix
# =========================================================
fig3, ax3 = plt.subplots(figsize=(10, 6))

labels = ['Full Omnichannel\n(79/100)', 'Flagship Plus\n(75/100)', 
          'B2B Pivot\n(71/100)', 'Platform-First\n(60/100)']

# The raw data arrays based on the evaluation matrix in the report
customer = np.array([22, 18, 12, 10])
strat = np.array([20, 18, 15, 5])
risk = np.array([10, 15, 16, 18])  
tco = np.array([12, 16, 18, 15])   
scale = np.array([15, 8, 10, 12])

width = 0.6

# Create stacked bars
ax3.bar(labels, customer, width, label='Customer Impact (25%)', color='#1d3557')
ax3.bar(labels, strat, width, bottom=customer, label='Strategic Alignment (20%)', color='#457b9d')
ax3.bar(labels, risk, width, bottom=customer+strat, label='Impl. Risk (20%)', color='#a8dadc')
ax3.bar(labels, tco, width, bottom=customer+strat+risk, label='TCO (20%)', color='#e63946')
ax3.bar(labels, scale, width, bottom=customer+strat+risk+tco, label='Scalability (15%)', color='#f1faee', edgecolor='gray')

# Formatting
ax3.set_ylabel('Weighted Score (Out of 100)', fontsize=12)
ax3.set_title('Strategic Alternatives: Weighted Evaluation Matrix', 
              fontsize=14, fontweight='bold', pad=15)
ax3.legend(loc='upper right', bbox_to_anchor=(1.25, 1))

# Add total score labels on top of the stacked bars
totals = customer + strat + risk + tco + scale
for i, total in enumerate(totals):
    ax3.text(i, total + 1, str(int(total)), ha='center', va='bottom', 
             fontweight='bold', fontsize=12)

ax3.spines['top'].set_visible(False)
ax3.spines['right'].set_visible(False)

save_path_3 = os.path.join(script_dir, 'strategic_matrix.png')

plt.tight_layout()
plt.savefig(save_path_3, dpi=300)
plt.close(fig3)