
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Set up the style for professional charts
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['axes.facecolor'] = 'white'

# Create figure with 2x2 subplots
fig, axes = plt.subplots(2, 2, figsize=(14, 12))
fig.suptitle('Elixir Technology: Agile Business Transformation Analysis', fontsize=16, fontweight='bold', y=0.98)

# Chart 1: Evolution Timeline - Revenue/Focus Areas
ax1 = axes[0, 0]
phases = ['1993-1998\nTraining &\nConsulting', '1998-2003\nCASE Tools', '2003-2007\nBI Solutions\n(ER)', '2007-2012\nElixir\nRepertoire', '2012+\nEnterprise\nAnalytics']
years = [1995, 2000, 2005, 2009, 2015]
revenue_trend = [1, 3, 6, 8, 10]  # Relative scale
agility_score = [3, 5, 8, 9, 10]  # Agility capability score

ax1_twin = ax1.twinx()
bars = ax1.bar(range(len(phases)), revenue_trend, color='#3498db', alpha=0.7, label='Business Scale')
line = ax1_twin.plot(range(len(phases)), agility_score, color='#e74c3c', marker='o', linewidth=3, markersize=8, label='Agility Score')

ax1.set_xticks(range(len(phases)))
ax1.set_xticklabels(phases, fontsize=9)
ax1.set_ylabel('Relative Business Scale', fontsize=10, color='#3498db')
ax1_twin.set_ylabel('Agility Capability Score', fontsize=10, color='#e74c3c')
ax1.set_title('Business Evolution & Agility Development', fontsize=12, fontweight='bold')
ax1.legend(loc='upper left')
ax1_twin.legend(loc='upper right')

# Chart 2: Success Factors - Radar Chart Style (Bar representation)
ax2 = axes[0, 1]
factors = ['Leadership\nVision', 'Technical\nExpertise', 'Market\nSensitivity', 'Innovation\nInvestment', 'Financial\nPrudence', 'Customer\nFocus']
scores = [9, 8, 9, 8, 7, 9]
colors = ['#2ecc71', '#3498db', '#9b59b6', '#f39c12', '#e74c3c', '#1abc9c']

bars = ax2.barh(factors, scores, color=colors, alpha=0.8, edgecolor='black', linewidth=1)
ax2.set_xlim(0, 10)
ax2.set_xlabel('Importance Score (1-10)', fontsize=10)
ax2.set_title('Key Success Factors', fontsize=12, fontweight='bold')
for i, (bar, score) in enumerate(zip(bars, scores)):
    ax2.text(score + 0.2, i, str(score), va='center', fontsize=10, fontweight='bold')

# Chart 3: Resilience Mechanisms - Circular/Donut Chart
ax3 = axes[1, 0]
mechanisms = ['Boundary\nOpenness', 'Organizational\nAdaptability', 'Balanced\nAmbidexterity', 'Financial\nRisk Buffering']
values = [30, 25, 25, 20]
colors_donut = ['#3498db', '#2ecc71', '#f39c12', '#e74c3c']
explode = (0.05, 0.05, 0.05, 0.05)

wedges, texts, autotexts = ax3.pie(values, labels=mechanisms, colors=colors_donut, autopct='%1.0f%%',
                                   startangle=90, explode=explode, shadow=True)
for autotext in autotexts:
    autotext.set_fontsize(10)
    autotext.set_fontweight('bold')
ax3.set_title('Resilience & Agility Enablers', fontsize=12, fontweight='bold')

# Chart 4: Strategic Critique - Strengths vs Limitations
ax4 = axes[1, 1]
categories = ['Proactive\nDisruption', 'Market\nDiversification', 'Learning\nOrientation', 'Predictive\nCapability', 'Resource\nScale', 'Institutional\nAgility']
strengths = [9, 8, 9, 4, 3, 5]  # Positive scores
limitations = [0, 0, 0, 6, 7, 5]  # Inverted for visual comparison

x = np.arange(len(categories))
width = 0.35

bars1 = ax4.bar(x - width/2, strengths, width, label='Strategic Strengths', color='#2ecc71', alpha=0.8)
bars2 = ax4.bar(x + width/2, limitations, width, label='Areas for Improvement', color='#e74c3c', alpha=0.8)

ax4.set_ylabel('Score (0-10)', fontsize=10)
ax4.set_title('Strategic Critique: Strengths vs Limitations', fontsize=12, fontweight='bold')
ax4.set_xticks(x)
ax4.set_xticklabels(categories, fontsize=9)
ax4.legend()
ax4.set_ylim(0, 10)

# Add value labels
for bar in bars1:
    height = bar.get_height()
    if height > 0:
        ax4.annotate(f'{height}', xy=(bar.get_x() + bar.get_width()/2, height),
                    xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=9)
for bar in bars2:
    height = bar.get_height()
    if height > 0:
        ax4.annotate(f'{height}', xy=(bar.get_x() + bar.get_width()/2, height),
                    xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=9)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig('/mnt/kimi/output/elixir_technology_analysis.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.show()

print("Chart 1: Business Evolution & Agility Development - Shows how Elixir evolved through 5 phases with increasing agility")
print("Chart 2: Key Success Factors - Scores the 6 main factors contributing to Elixir's success")
print("Chart 3: Resilience & Agility Enablers - Distribution of the 4 mechanisms that enabled resilience")
print("Chart 4: Strategic Critique - Comparison of strategic strengths vs limitations")





import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.patches import FancyBboxPatch, Circle
import matplotlib.patches as mpatches

# Create figure with 2 subplots for Agile Principles and Application
fig, axes = plt.subplots(1, 2, figsize=(16, 8))
fig.suptitle('Agile Methodology: Principles and Application to Elixir Technology', fontsize=16, fontweight='bold', y=0.98)

# Chart 1: Agile Principles - How Elixir Applied Each
ax1 = axes[0]
principles = ['Customer\nCollaboration', 'Responding\nto Change', 'Working\nProducts', 'Individuals\n& Interactions', 'Iterative\nDevelopment']
elixir_application = [9, 10, 8, 9, 9]  # How well Elixir applied each principle
traditional_approach = [4, 3, 6, 5, 3]  # Traditional approach comparison

x = np.arange(len(principles))
width = 0.35

bars1 = ax1.bar(x - width/2, elixir_application, width, label='Elixir Technology (Agile)', color='#2ecc71', alpha=0.8, edgecolor='black')
bars2 = ax1.bar(x + width/2, traditional_approach, width, label='Traditional Approach', color='#95a5a6', alpha=0.8, edgecolor='black')

ax1.set_ylabel('Application Score (0-10)', fontsize=11)
ax1.set_title('Agile Principles: Elixir vs Traditional Approach', fontsize=13, fontweight='bold')
ax1.set_xticks(x)
ax1.set_xticklabels(principles, fontsize=10)
ax1.legend(loc='upper left', fontsize=10)
ax1.set_ylim(0, 11)

# Add value labels
for bar in bars1:
    height = bar.get_height()
    ax1.annotate(f'{height}', xy=(bar.get_x() + bar.get_width()/2, height),
                xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=10, fontweight='bold')
for bar in bars2:
    height = bar.get_height()
    ax1.annotate(f'{height}', xy=(bar.get_x() + bar.get_width()/2, height),
                xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=10, fontweight='bold')

# Add horizontal line at 7.5 for "excellent" threshold
ax1.axhline(y=7.5, color='#e74c3c', linestyle='--', alpha=0.5, linewidth=2)
ax1.text(4.5, 7.8, 'Excellence Threshold', fontsize=9, color='#e74c3c', ha='right')

# Chart 2: Timeline of Disruptions and Responses
ax2 = axes[1]

# Create timeline data
events = [
    (1993, 'Founded\n(Training)'),
    (1998, 'Pivot to\nCASE Tools'),
    (2003, 'OSS Disruption\n→ BI Pivot'),
    (2007, 'Elixir\nRepertoire'),
    (2008, 'Financial\nCrisis'),
    (2012, 'Enterprise\nAnalytics')
]

years = [e[0] for e in events]
labels = [e[1] for e in events]

# Create horizontal timeline
ax2.set_xlim(1990, 2015)
ax2.set_ylim(0, 10)

# Draw timeline line
ax2.plot([1990, 2015], [5, 5], 'k-', linewidth=3, alpha=0.3)

# Color coding for event types
colors = ['#3498db', '#2ecc71', '#e74c3c', '#2ecc71', '#f39c12', '#2ecc71']
markers = ['o', 's', '^', 's', 'D', 's']

for i, (year, label, color, marker) in enumerate(zip(years, labels, colors, markers)):
    # Alternate above and below line
    y_pos = 7 if i % 2 == 0 else 3
    
    # Draw connection line
    ax2.plot([year, year], [5, y_pos], 'k--', alpha=0.5, linewidth=1)
    
    # Draw marker
    ax2.scatter(year, 5, s=200, c=color, marker=marker, edgecolors='black', linewidth=2, zorder=5)
    
    # Add text box
    bbox_props = dict(boxstyle="round,pad=0.3", facecolor=color, alpha=0.7, edgecolor='black')
    ax2.text(year, y_pos, label, ha='center', va='center', fontsize=9, 
             fontweight='bold', bbox=bbox_props)

# Add legend
legend_elements = [
    mpatches.Patch(color='#3498db', label='Foundation'),
    mpatches.Patch(color='#2ecc71', label='Strategic Pivot'),
    mpatches.Patch(color='#e74c3c', label='Disruption Response'),
    mpatches.Patch(color='#f39c12', label='Crisis Management')
]
ax2.legend(handles=legend_elements, loc='upper left', fontsize=10)

ax2.set_title('Timeline: Disruptions and Agile Responses (1993-2015)', fontsize=13, fontweight='bold')
ax2.set_xlabel('Year', fontsize=11)
ax2.set_yticks([])
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['left'].set_visible(False)

# Add annotations
ax2.annotate('First Pivot:\nTraining → CASE', xy=(1998, 5), xytext=(1996, 2),
            arrowprops=dict(arrowstyle='->', color='black', alpha=0.7),
            fontsize=9, ha='center')
ax2.annotate('Second Pivot:\nCASE → BI', xy=(2003, 5), xytext=(2005, 2),
            arrowprops=dict(arrowstyle='->', color='black', alpha=0.7),
            fontsize=9, ha='center')

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig('/mnt/kimi/output/elixir_agile_principles.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.show()

print("Chart 1: Agile Principles Application - Shows how Elixir excelled at agile principles compared to traditional approaches")
print("Chart 2: Timeline of Disruptions - Visualizes Elixir's agile responses to market disruptions over time")
