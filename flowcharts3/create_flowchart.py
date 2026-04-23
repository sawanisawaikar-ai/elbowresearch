import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Polygon
import numpy as np

fig, ax = plt.subplots(1, 1, figsize=(16, 20))
ax.set_xlim(0, 16)
ax.set_ylim(0, 20)
ax.axis('off')

# Colors
colors = {
    'start': '#e3f2fd',
    'start_border': '#1565c0',
    'process': '#e8f5e9',
    'process_border': '#388e3c',
    'decision': '#fff3e0',
    'decision_border': '#f57c00',
    'group_a': '#bbdefb',
    'group_a_border': '#1976d2',
    'group_b': '#d1c4e9',
    'group_b_border': '#7c4dbf',
    'outcome': '#c8e6c9',
    'outcome_border': '#4caf50',
    'end': '#ffecb3',
    'end_border': '#ffc107',
}

def draw_box(ax, x, y, w, h, text, fc, bc, fs=9):
    box = FancyBboxPatch((x-w/2, y-h/2), w, h,
                         boxstyle="round,pad=0.03,rounding_size=0.2",
                         facecolor=fc, edgecolor=bc, linewidth=2)
    ax.add_patch(box)
    ax.text(x, y, text, ha='center', va='center', fontsize=fs, fontweight='bold', wrap=True)

def draw_diamond(ax, x, y, size, text, fs=8):
    pts = np.array([[x, y+size], [x+size, y], [x, y-size], [x-size, y]])
    poly = Polygon(pts, facecolor=colors['decision'], edgecolor=colors['decision_border'], linewidth=2)
    ax.add_patch(poly)
    ax.text(x, y, text, ha='center', va='center', fontsize=fs, fontweight='bold')

def arrow(ax, x1, y1, x2, y2):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color='#555', lw=1.5))

# Title
ax.text(8, 19.5, 'IASTM Study Procedure - Randomized Controlled Trial', 
        ha='center', va='center', fontsize=14, fontweight='bold', color='#333')
ax.text(8, 19, 'Sprinters with Hamstring Tightness', 
        ha='center', va='center', fontsize=11, color='#666')

# START
draw_box(ax, 8, 18.3, 5, 0.6, 'START: Participant Recruitment', colors['start'], colors['start_border'])

# Screening
arrow(ax, 8, 18, 8, 17.4)
draw_box(ax, 8, 17.1, 5.5, 0.6, 'Screening based on Inclusion/Exclusion Criteria', colors['process'], colors['process_border'])

# Eligibility check
arrow(ax, 8, 16.8, 8, 16.2)
draw_diamond(ax, 8, 16, 0.5, 'Eligible?')

# No - Exclude
arrow(ax, 7.5, 16, 5, 16)
draw_box(ax, 3.5, 16, 2, 0.5, 'Excluded', colors['end'], colors['end_border'], fs=8)

# Yes - Consent
arrow(ax, 8.5, 16, 10, 16)
draw_box(ax, 11.5, 16, 3, 0.5, 'Written Informed\nConsent Obtained', colors['process'], colors['process_border'], fs=8)

# Baseline Assessment
arrow(ax, 11.5, 15.75, 11.5, 15.2)
draw_box(ax, 11.5, 14.9, 4.5, 1.1, 'BASELINE ASSESSMENT\n• Stride Length (Kinovea)\n• Sprint Time (Stopwatch, 30m)\n• Hamstring Flexibility (AKE Test)', colors['process'], colors['process_border'], fs=8)

# Randomization
arrow(ax, 11.5, 14.35, 11.5, 13.7)
draw_box(ax, 11.5, 13.4, 4, 0.5, 'Random Allocation (Lottery)', colors['decision'], colors['decision_border'])

# Split into two groups
arrow(ax, 11.5, 13.15, 11.5, 12.5)
arrow(ax, 9, 13.4, 5, 13.4)
arrow(ax, 5, 13.4, 5, 12.7)

draw_box(ax, 11, 12.5, 3.5, 0.5, 'GROUP A\n(n= participants)', colors['group_a'], colors['group_a_border'])
draw_box(ax, 5, 12.5, 3.5, 0.5, 'GROUP B\n(n= participants)', colors['group_b'], colors['group_b_border'])

# Group A Intervention
arrow(ax, 11, 12.25, 11, 11.6)
draw_box(ax, 11, 11.3, 5, 1.4, 'GROUP A: IASTM Intervention\n• M2T blade application\n• Prone position\n• Bilateral treatment\n• ~3 min per limb\n• Sweeping technique (origin to insertion)\n• Lubricant used', colors['group_a'], colors['group_a_border'], fs=8)

# Group B Intervention
arrow(ax, 5, 12.25, 5, 11.6)
draw_box(ax, 5, 11.3, 5, 1.0, 'GROUP B: Conventional Therapy\n• Warm-up program\n• Static hamstring stretching\n• 3 reps × 30 sec hold\n• Bilateral application', colors['group_b'], colors['group_b_border'], fs=8)

# Converge
arrow(ax, 11, 10.6, 11, 9.9)
arrow(ax, 5, 10.8, 5, 9.9)
arrow(ax, 5, 9.9, 6, 9.9)
arrow(ax, 6, 9.9, 6, 9.5)
arrow(ax, 11, 9.9, 10, 9.9)
arrow(ax, 10, 9.9, 10, 9.5)
arrow(ax, 6, 9.5, 10, 9.5)
arrow(ax, 10, 9.5, 10, 9.2)

# Post-Assessment
draw_box(ax, 8, 8.9, 5.5, 1.1, 'POST-INTERVENTION ASSESSMENT\n• Stride Length (Kinovea)\n• Sprint Time (Stopwatch, 30m)\n• Hamstring Flexibility (AKE Test)', colors['outcome'], colors['outcome_border'], fs=8)

# Data Analysis
arrow(ax, 8, 8.35, 8, 7.7)
draw_box(ax, 8, 7.4, 4, 0.5, 'Data Entry & Statistical Analysis', colors['process'], colors['process_border'])

# Results
arrow(ax, 8, 7.15, 8, 6.5)
draw_diamond(ax, 8, 6.3, 0.5, 'Results')

# Hypothesis testing
arrow(ax, 7.5, 6.3, 5, 6.3)
draw_box(ax, 3.5, 6.3, 2, 0.5, 'Reject H₀', colors['group_a'], colors['group_a_border'], fs=8)

arrow(ax, 8.5, 6.3, 10, 6.3)
draw_box(ax, 11.5, 6.3, 2, 0.5, 'Fail to\nReject H₀', colors['group_b'], colors['group_b_border'], fs=8)

# Conclusion
arrow(ax, 5, 6.05, 5, 5.5)
arrow(ax, 11.5, 6.05, 11.5, 5.5)
arrow(ax, 5, 5.5, 8, 5.5)
arrow(ax, 11.5, 5.5, 8.3, 5.5)
arrow(ax, 8, 5.5, 8, 5.2)

draw_box(ax, 8, 4.9, 6, 0.7, 'CONCLUSION & CLINICAL IMPLICATIONS', colors['outcome'], colors['outcome_border'], fs=10)

# END
arrow(ax, 8, 4.55, 8, 4)
draw_box(ax, 8, 3.7, 4, 0.5, 'END', colors['end'], colors['end_border'], fs=12)

# Legend
ax.text(8, 3, 'Legend:', ha='center', va='center', fontsize=10, fontweight='bold')
items = [
    ('Screening/Process', colors['process'], colors['process_border']),
    ('Decision Point', colors['decision'], colors['decision_border']),
    ('Group A (IASTM)', colors['group_a'], colors['group_a_border']),
    ('Group B (Conventional)', colors['group_b'], colors['group_b_border']),
]
for i, (lbl, fc, bc) in enumerate(items):
    x = 2 + i * 3.5
    rect = FancyBboxPatch((x-1.4, 2.3), 2.8, 0.5, boxstyle="round,pad=0.02,rounding_size=0.1",
                          facecolor=fc, edgecolor=bc, linewidth=2)
    ax.add_patch(rect)
    ax.text(x, 2.55, lbl, ha='center', va='center', fontsize=8)

# Footer
ax.text(8, 1.5, 'Study: IASTM vs Conventional Therapy for Hamstring Tightness in Sprinters', 
        ha='center', va='center', fontsize=9, color='#666', style='italic')

plt.tight_layout()
plt.savefig('/workspace/project/elbowresearch/flowcharts3/procedure_flowchart.png', dpi=150, bbox_inches='tight', 
            facecolor='white')
plt.savefig('/workspace/project/elbowresearch/flowcharts3/procedure_flowchart.pdf', bbox_inches='tight',
            facecolor='white')
print("Flowchart saved successfully!")