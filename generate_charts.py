import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle
import numpy as np
import os

# Create images directory if it doesn't exist
os.makedirs('images', exist_ok=True)

# Set up the style for professional charts
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['axes.facecolor'] = 'white'

# ============================================================================
# CHART 1: The Elixir Evolution Timeline
# ============================================================================
fig, ax = plt.subplots(figsize=(14, 8))

# Timeline data
events = [
    (1993, 'Founded\nTraining &\nConsulting', 1),
    (1996, 'Pivot to\nCASE Tools', 2),
    (1999, 'Launch\nElixir Report\n(ER)', 3),
    (2003, 'OSS Disruption\nPivot to BI', 4),
    (2007, 'Financial Crisis\nElixir Repertoire', 5)
]

years = [e[0] for e in events]
labels = [e[1] for e in events]
phases = [e[2] for e in events]

# Draw main timeline
ax.plot([1992, 2008], [0, 0], 'k-', linewidth=4, alpha=0.3, zorder=1)

# Color scheme
colors = ['#3498db', '#2ecc71', '#f39c12', '#e74c3c', '#9b59b6']

# Draw events
for i, (year, label, phase) in enumerate(zip(years, labels, phases)):
    # Draw marker
    circle = Circle((year, 0), 0.3, color=colors[i], ec='black',
                    linewidth=2.5, zorder=5)
    ax.add_patch(circle)

    # Add vertical line
    y_pos = 3 if i % 2 == 0 else -3
    ax.plot([year, year], [0.3, y_pos], 'k--', alpha=0.3, linewidth=1.5)

    # Add text box with description
    bbox_props = dict(boxstyle="round,pad=0.5", facecolor=colors[i],
                      alpha=0.85, edgecolor='black', linewidth=2)
    ax.text(year, y_pos, label, ha='center',
            va='center' if i % 2 == 0 else 'center',
            fontsize=10, fontweight='bold', color='white',
            bbox=bbox_props)

    # Add year label
    ax.text(year, 0.8, str(year), ha='center', va='bottom',
            fontsize=11, fontweight='bold')

# Add phase progression line
ax.plot(years, phases, 'o--', color='#667eea', linewidth=3,
        markersize=10, alpha=0.6, zorder=3)

ax.set_xlim(1990, 2010)
ax.set_ylim(-4.5, 5.5)
ax.set_xlabel('Year', fontsize=12, fontweight='bold')
ax.set_title('The Elixir Evolution Timeline: 15 Years of Strategic Pivots',
             fontsize=14, fontweight='bold', pad=20)

# Remove spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.set_yticks([])

# Add legend
legend_elements = [
    mpatches.Patch(color='#667eea', label='Business Maturity Stage'),
    mpatches.Patch(color='#3498db', label='Foundation'),
    mpatches.Patch(color='#2ecc71', label='Strategic Pivot'),
    mpatches.Patch(color='#f39c12', label='Market Response'),
    mpatches.Patch(color='#e74c3c', label='Crisis & Evolution'),
    mpatches.Patch(color='#9b59b6', label='Enterprise Focus')
]
ax.legend(handles=legend_elements, loc='upper left', fontsize=10,
          framealpha=0.95)

plt.tight_layout()
plt.savefig('images/01_elixir_evolution_timeline.png', dpi=300,
            bbox_inches='tight', facecolor='white')
plt.close()

# ============================================================================
# CHART 2: The Resilience & Agility Framework (Venn-like Pillar Chart)
# ============================================================================
fig, ax = plt.subplots(figsize=(12, 9))

# Create concentric circles for Venn diagram effect
circle_colors = ['#3498db', '#2ecc71', '#f39c12']
circle_labels = ['Boundary\nOpenness', 'Organizational\nAdaptability',
                 'Balanced\nAmbidexterity']
circle_positions = [(0.35, 0.6), (0.65, 0.6), (0.5, 0.35)]
circle_radius = 0.18

for i, (pos, color, label) in enumerate(
    zip(circle_positions, circle_colors, circle_labels)
):
    circle = Circle(pos, circle_radius, color=color, alpha=0.6,
                    edgecolor='black', linewidth=2)
    ax.add_patch(circle)
    ax.text(pos[0], pos[1], label, ha='center', va='center', fontsize=11,
            fontweight='bold', color='white')

# Add Financial Prudence at the base
financial_box = FancyBboxPatch((0.35, 0.05), 0.3, 0.12,
                               boxstyle="round,pad=0.01",
                               edgecolor='black', facecolor='#e74c3c',
                               linewidth=2.5, alpha=0.85)
ax.add_patch(financial_box)
ax.text(0.5, 0.11, 'Financial Prudence\n(Risk Buffering Foundation)',
        ha='center', va='center', fontsize=10, fontweight='bold',
        color='white')

# Add connecting lines
ax.plot([0.5, 0.5], [0.17, 0.25], 'k--', linewidth=2, alpha=0.5)

# Add labels and descriptions
descriptions = [
    ('Boundary Openness', 'External market scanning\nand trend awareness'),
    ('Organizational Adaptability',
     'Quick decision-making\nand rapid reconfiguration'),
    ('Balanced Ambidexterity',
     'Exploration of new opportunities\nwhile exploiting existing strengths'),
    ('Financial Prudence',
     'Risk buffering and strategic runway\nfor agile experimentation')
]

description_positions = [(0.08, 0.75), (0.92, 0.75), (0.5, 0.85), (0.5, -0.05)]
for (title, desc), pos in zip(descriptions, description_positions):
    if pos[1] > 0.5:
        ax.text(pos[0], pos[1], f'{title}\n{desc}', ha='center', va='top',
                fontsize=9, style='italic', bbox=dict(boxstyle='round',
                facecolor='lightyellow', alpha=0.7))

ax.set_xlim(0, 1)
ax.set_ylim(-0.1, 1)
ax.set_aspect('equal')
ax.axis('off')

ax.text(0.5, 0.98,
        'The Resilience & Agility Framework:\nInterconnected Mechanisms',
        ha='center', va='top', fontsize=14, fontweight='bold')

plt.tight_layout()
plt.savefig('images/02_resilience_agility_framework.png', dpi=300,
            bbox_inches='tight', facecolor='white')
plt.close()

# ============================================================================
# CHART 3: Market Diversification Strategy (Donut + Treemap style)
# ============================================================================
fig = plt.figure(figsize=(14, 8))

# Sector Distribution (Donut)
ax1 = plt.subplot(1, 2, 1)
sectors = ['Government', 'Banking', 'Healthcare', 'Other\nSectors']
sector_sizes = [30, 35, 25, 10]
colors_sectors = ['#3498db', '#2ecc71', '#f39c12', '#95a5a6']

wedges, texts, autotexts = ax1.pie(sector_sizes, labels=sectors,
                                   colors=colors_sectors,
                                   autopct='%1.0f%%', startangle=90,
                                   textprops={'fontsize': 11,
                                              'fontweight': 'bold'})

# Create donut effect
centre_circle = Circle((0, 0), 0.70, fc='white', edgecolor='black',
                       linewidth=2)
ax1.add_artist(centre_circle)

ax1.text(0, 0, 'Sector\nFocus', ha='center', va='center', fontsize=12,
         fontweight='bold')
ax1.set_title('Market Sector Diversification', fontsize=12,
              fontweight='bold', pad=15)

# Geographic Distribution (Donut)
ax2 = plt.subplot(1, 2, 2)
geographies = ['Singapore\n(Local)', 'USA', 'Japan', 'Other\nRegions']
geo_sizes = [40, 35, 20, 5]
colors_geo = ['#e74c3c', '#9b59b6', '#1abc9c', '#95a5a6']

wedges, texts, autotexts = ax2.pie(geo_sizes, labels=geographies,
                                   colors=colors_geo,
                                   autopct='%1.0f%%', startangle=90,
                                   textprops={'fontsize': 11,
                                              'fontweight': 'bold'})

# Create donut effect
centre_circle = Circle((0, 0), 0.70, fc='white', edgecolor='black',
                       linewidth=2)
ax2.add_artist(centre_circle)

ax2.text(0, 0, 'Geographic\nReach', ha='center', va='center', fontsize=12,
         fontweight='bold')
ax2.set_title('Geographic Diversification', fontsize=12,
              fontweight='bold', pad=15)

fig.suptitle('Market Diversification Strategy: Risk Mitigation Through '
             'Portfolio Expansion',
             fontsize=14, fontweight='bold', y=0.98)

plt.tight_layout()
plt.savefig('images/03_market_diversification.png', dpi=300,
            bbox_inches='tight', facecolor='white')
plt.close()

# ============================================================================
# CHART 4: SWOT Analysis Matrix
# ============================================================================
fig, ax = plt.subplots(figsize=(14, 10))

# Define SWOT content
swot_data = {
    'Strengths': [
        '✓ Proactive Disruption Management',
        '✓ Resilience Through Diversification',
        '✓ Strong Learning Orientation',
        '✓ Customer-Centric Development',
        '✓ Technical Excellence'
    ],
    'Weaknesses': [
        '✗ Reactive Rather Than Predictive',
        '✗ Resource Constraints (SME)',
        '✗ Over-Reliance on Founders',
        '✗ Limited Strategic Control',
        '✗ Smaller Scale vs Competitors'
    ],
    'Opportunities': [
        '→ Predictive Trend Analysis',
        '→ Institutionalize Agile Capabilities',
        '→ Strategic Partnerships & Alliances',
        '→ Market Expansion Potential',
        '→ AI/ML Integration'
    ],
    'Threats': [
        '⚠ Major Competitors (IBM, Oracle, SAP)',
        '⚠ Macro-economic Crises',
        '⚠ Rapid Technology Disruption',
        '⚠ Talent Retention Challenges',
        '⚠ Market Consolidation Pressure'
    ]
}

# Color scheme for SWOT
swot_colors = {
    'Strengths': '#2ecc71',    # Green
    'Weaknesses': '#e74c3c',   # Red
    'Opportunities': '#3498db',  # Blue
    'Threats': '#f39c12'       # Orange
}

# Position coordinates for 2x2 matrix
positions = {
    'Strengths': (0.02, 0.52, 0.46, 0.46),    # x, y, width, height
    'Weaknesses': (0.52, 0.52, 0.46, 0.46),
    'Opportunities': (0.02, 0.02, 0.46, 0.46),
    'Threats': (0.52, 0.02, 0.46, 0.46)
}

for quadrant, items in swot_data.items():
    x, y, w, h = positions[quadrant]
    color = swot_colors[quadrant]

    # Draw rectangle
    rect = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.01",
                          edgecolor='black', facecolor=color,
                          linewidth=3, alpha=0.15, transform=ax.transAxes)
    ax.add_patch(rect)

    # Add title
    ax.text(x + w/2, y + h - 0.03, quadrant, transform=ax.transAxes,
            fontsize=16, fontweight='bold', ha='center', va='top',
            bbox=dict(boxstyle='round', facecolor=color, alpha=0.9,
                      edgecolor='black', linewidth=2))

    # Add items
    y_offset = y + h - 0.08
    for i, item in enumerate(items):
        ax.text(x + 0.02, y_offset - (i * 0.09), item, transform=ax.transAxes,
                fontsize=12, va='top', fontweight='600', color='black')

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

fig.text(0.5, 0.98, 'SWOT Analysis: Elixir Technology Strategic Position',
         ha='center', fontsize=15, fontweight='bold')

# Add strategic insights at bottom
insights = ('Strategic Insight: Elixir\'s strength lies in agility and '
            'adaptability. To overcome weaknesses,\ninstitutionalize agile '
            'capabilities and explore strategic partnerships for scale.')
fig.text(0.5, 0.01, insights, ha='center', fontsize=10, style='italic',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plt.tight_layout(rect=[0, 0.03, 1, 0.96])
plt.savefig('images/04_swot_analysis.png', dpi=300, bbox_inches='tight',
            facecolor='white')
plt.close()

# ============================================================================
# CHART 5: Business Focus Transition (100% Stacked Area Chart)
# ============================================================================
fig, ax = plt.subplots(figsize=(14, 8))

# Create data for stacked area
years_area = np.array([1993, 1996, 1999, 2003, 2007, 2012])
training = np.array([100, 60, 30, 10, 5, 2])
case_tools = np.array([0, 35, 50, 40, 20, 5])
bi_analytics = np.array([0, 5, 20, 50, 75, 93])

# Normalize to 100%
total = training + case_tools + bi_analytics
training_pct = (training / total) * 100
case_tools_pct = (case_tools / total) * 100
bi_analytics_pct = (bi_analytics / total) * 100

# Plot stacked area
ax.stackplot(years_area, training_pct, case_tools_pct, bi_analytics_pct,
             labels=['Training & Consulting', 'CASE Tools', 'BI & Analytics'],
             colors=['#3498db', '#2ecc71', '#f39c12'],
             alpha=0.85, edgecolor='black', linewidth=1.5)

# Add milestone markers
milestones = [
    (1993, 'Founded'),
    (1996, 'Pivot to\nCASE'),
    (1999, 'ER\nLaunch'),
    (2003, 'OSS\nDisruption'),
    (2007, 'Crisis &\nRepertoire'),
    (2012, 'Enterprise\nFocus')
]

for year, label in milestones:
    ax.axvline(x=year, color='gray', linestyle='--', alpha=0.5, linewidth=1)
    ax.text(year, 105, label, ha='center', fontsize=9, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.7))

ax.set_ylabel('Percentage of Company Focus (%)', fontsize=12,
              fontweight='bold')
ax.set_title('Business Focus Transition: Strategic Pivot Evolution',
             fontsize=14, fontweight='bold', pad=20)
ax.set_ylim(0, 110)
ax.set_xlim(1990, 2014)

# Format as percentage
ax.yaxis.set_major_formatter(
    plt.FuncFormatter(lambda y, _: '{:.0f}%'.format(y))
)

ax.legend(loc='center left', fontsize=11, framealpha=0.95, edgecolor='black',
          fancybox=True, shadow=True)
ax.grid(True, alpha=0.3, linestyle=':')

plt.tight_layout()
plt.savefig('images/05_business_focus_transition.png', dpi=300,
            bbox_inches='tight', facecolor='white')
plt.close()

print("✅ All charts generated successfully!")
print("📊 Chart 1: The Elixir Evolution Timeline")
print("🎯 Chart 2: The Resilience & Agility Framework")
print("🌍 Chart 3: Market Diversification Strategy")
print("📈 Chart 4: SWOT Analysis Matrix")
print("📉 Chart 5: Business Focus Transition Area Chart")
print("\nAll charts saved to: images/")
