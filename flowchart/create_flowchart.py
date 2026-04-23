import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

fig, ax = plt.subplots(1, 1, figsize=(16, 22))
ax.set_xlim(0, 16)
ax.set_ylim(0, 22)
ax.axis('off')
ax.set_aspect('equal')

# Colors
colors = {
    'start': '#e3f2fd',
    'border_start': '#1976d2',
    'decision': '#fff3e0',
    'border_decision': '#f57c00',
    'process': '#e8f5e9',
    'border_process': '#388e3c',
    'success': '#c8e6c9',
    'border_success': '#4caf50',
    'warning': '#ffcdd2',
    'border_warning': '#f44336',
    'treatment_acute': '#bbdefb',
    'treatment_subacute': '#b2dfdb',
    'treatment_chronic': '#d1c4e9',
    'surgery': '#d1c4e9',
    'final': '#e0f7fa'
}

def draw_rounded_box(ax, x, y, width, height, text, facecolor, bordercolor, fontsize=9):
    box = FancyBboxPatch((x - width/2, y - height/2), width, height,
                         boxstyle="round,pad=0.05,rounding_size=0.3",
                         facecolor=facecolor, edgecolor=bordercolor, linewidth=2)
    ax.add_patch(box)
    ax.text(x, y, text, ha='center', va='center', fontsize=fontsize,
            fontweight='bold', wrap=True,
            bbox=dict(boxstyle='round', facecolor=facecolor, edgecolor='none', alpha=0))

def draw_diamond(ax, x, y, size, text, facecolor, bordercolor, fontsize=8):
    diamond = plt.Polygon([(x, y + size), (x + size, y), (x, y - size), (x - size, y)],
                          facecolor=facecolor, edgecolor=bordercolor, linewidth=2)
    ax.add_patch(diamond)
    ax.text(x, y, text, ha='center', va='center', fontsize=fontsize,
            fontweight='bold', wrap=True)

def draw_arrow(ax, start, end, color='#666666'):
    ax.annotate('', xy=end, xytext=start,
                arrowprops=dict(arrowstyle='->', color=color, lw=2))

# Title
ax.text(8, 21.5, 'Tennis Elbow (Lateral Epicondylopathy) - Clinical Management Flowchart',
        ha='center', va='center', fontsize=16, fontweight='bold', color='#333')
ax.text(8, 21, 'Based on Evidence-Based Guidelines', ha='center', va='center', fontsize=11, color='#666')

# START - Patient presents
draw_rounded_box(ax, 8, 20.3, 4.5, 0.7, 'Patient Presents with\nLateral Elbow Pain', 
                 colors['start'], colors['border_start'])

# Assessment box
draw_arrow(ax, (8, 19.95), (8, 19.3))
draw_rounded_box(ax, 8, 19, 4.5, 0.6, 'Assessment: History & Clinical Exam', 
                 colors['process'], colors['border_process'])

# Arrows down
draw_arrow(ax, (8, 18.7), (8, 18.1))

# Diagnosis diamond
draw_diamond(ax, 8, 17.8, 0.7, 'Confirmed\nDiagnosis?', colors['decision'], colors['border_decision'])

# Left arrow - NO (Rule out)
draw_arrow(ax, (7.3, 17.8), (5.5, 17.8))
draw_rounded_box(ax, 4, 17.8, 2.5, 0.9, 'Rule Out:\n• Radial Tunnel Syndrome\n• Cervical Radiculopathy',
                 colors['warning'], colors['border_warning'], fontsize=8)

# Right arrow - YES
draw_arrow(ax, (8.7, 17.8), (10.5, 17.8))
draw_rounded_box(ax, 12, 17.8, 3, 0.9, 'Confirmed\nLateral Epicondylopathy', 
                 colors['success'], colors['border_success'])

# Duration assessment
draw_arrow(ax, (12, 17.35), (12, 16.5))
draw_diamond(ax, 12, 16.2, 0.6, 'Duration?', colors['decision'], colors['border_decision'])

# Three paths based on duration
# Acute path
draw_arrow(ax, (11.4, 16.2), (10, 16.2))
draw_rounded_box(ax, 8.5, 16.2, 2.3, 0.8, 'Acute (< 3 mo)\nPhase 1', 
                 colors['treatment_acute'], '#2196f3', fontsize=9)

# Subacute path
draw_arrow(ax, (12, 15.6), (12, 15.1))
draw_rounded_box(ax, 12, 14.8, 2.3, 0.8, 'Subacute (3-4 wks)\nPhase 2', 
                 colors['treatment_subacute'], '#009688', fontsize=9)

# Chronic path  
draw_arrow(ax, (12.6, 16.2), (14, 16.2))
draw_rounded_box(ax, 15.3, 16.2, 2.3, 0.8, 'Chronic (> 4 wks)\nPhase 3', 
                 colors['treatment_chronic'], '#7c4dbf', fontsize=9)

# Treatment details boxes
draw_rounded_box(ax, 5.5, 15.2, 3.5, 1.3, 'Phase 1: Acute\n• Activity modification\n• Ice/heat therapy\n• Isometric exercises',
                 colors['treatment_acute'], '#2196f3', fontsize=8)

draw_rounded_box(ax, 8, 13.8, 3.5, 1.3, 'Phase 2: Subacute\n• Progressive stretching\n• Light resistance\n• Counterforce brace',
                 colors['treatment_subacute'], '#009688', fontsize=8)

draw_rounded_box(ax, 14, 14.8, 3.5, 1.3, 'Phase 3: Chronic\n• Eccentric strengthening\n• Resistance training\n• Functional exercises',
                 colors['treatment_chronic'], '#7c4dbf', fontsize=8)

# Converge arrow
draw_arrow(ax, (5.5, 14.55), (5.5, 13.5))
draw_arrow(ax, (8, 13.15), (8, 12.5))
draw_arrow(ax, (14, 14.15), (14, 13.5))
draw_arrow(ax, (14, 13.5), (9.5, 13.5))
draw_arrow(ax, (5.5, 13.5), (8, 13.5))
draw_arrow(ax, (8, 13.5), (8, 12.2))

# Progress check diamond
draw_diamond(ax, 8, 12, 0.6, 'Progress?', colors['decision'], colors['border_decision'])

# Left branch - No progress
draw_arrow(ax, (7.4, 12), (6, 12))
draw_rounded_box(ax, 4.5, 12, 2.5, 0.8, 'Continue\nConservative Tx', 
                 colors['process'], colors['border_process'], fontsize=9)

# Right branch - Still failing
draw_arrow(ax, (8.6, 12), (10, 12))
draw_diamond(ax, 11.5, 12, 0.6, '3+ mo\nFailed?', colors['decision'], colors['border_decision'])

# Surgery option
draw_arrow(ax, (12.1, 12), (14, 12))
draw_rounded_box(ax, 15.5, 12, 3, 1.2, 'Surgical Options:\n• Percutaneous release\n• Arthroscopic release\n• Open debridement',
                 colors['surgery'], '#7c4dbf', fontsize=8)

# Outcome box
draw_arrow(ax, (8, 11.4), (8, 10.7))
draw_rounded_box(ax, 8, 10.4, 5, 0.8, 'Outcome: 90-95% Success with Conservative Treatment', 
                 colors['success'], colors['border_success'], fontsize=10)

# Final boxes
draw_arrow(ax, (8, 10), (8, 9.3))
draw_rounded_box(ax, 8, 9, 4.5, 0.6, 'Prevention & Education', 
                 colors['final'], '#00bcd4', fontsize=10)

draw_arrow(ax, (15.5, 11.4), (15.5, 9))
draw_arrow(ax, (15.5, 9), (10.5, 9))
draw_arrow(ax, (10.5, 9), (10.5, 9.3))
draw_arrow(ax, (10.5, 9.3), (10.25, 9.3))

# Recurrence note
draw_rounded_box(ax, 5.5, 9, 3.5, 0.7, 'Note: 20-30% recurrence rate\nActivity modification recommended', 
                 '#ffecb3', '#ffc107', fontsize=8)

# Legend
legend_y = 7.5
ax.text(8, legend_y + 1.5, 'Treatment Evidence Levels', ha='center', va='center', 
        fontsize=12, fontweight='bold')

legend_items = [
    ('Strong Evidence', colors['success'], colors['border_success']),
    ('Moderate Evidence', colors['treatment_acute'], '#2196f3'),
    ('Chronic/Alternative', colors['treatment_chronic'], '#7c4dbf'),
    ('Caution Required', colors['warning'], colors['border_warning'])
]

for i, (label, fc, bc) in enumerate(legend_items):
    x_pos = 2 + (i * 3.5)
    rect = FancyBboxPatch((x_pos - 1.3, legend_y - 0.3), 2.6, 0.6,
                          boxstyle="round,pad=0.02,rounding_size=0.1",
                          facecolor=fc, edgecolor=bc, linewidth=2)
    ax.add_patch(rect)
    ax.text(x_pos, legend_y, label, ha='center', va='center', fontsize=9)

# Sources
ax.text(8, 5.5, 'Sources', ha='center', va='center', fontsize=12, fontweight='bold')
sources_text = """• GOV.UK - Tennis Elbow Guidelines
• UBC (2016) - Lateral Epicondyle Tendinopathy Evidence
• JOSPT (2022) - Clinical Practice Guidelines
• JSciMed Central (2017) - Treatment Review
• Melbourne Hand Therapy (2020) - Management Guidelines"""

ax.text(8, 4.8, sources_text, ha='center', va='top', fontsize=9, linespacing=1.5)

# Footer
ax.text(8, 1, 'Evidence-based clinical flowchart for lateral epicondylopathy management',
        ha='center', va='center', fontsize=10, color='#666', style='italic')

plt.tight_layout()
plt.savefig('/workspace/project/elbowresearch/flowchart/flowchart.png', dpi=150, bbox_inches='tight', 
            facecolor='white', edgecolor='none')
plt.savefig('/workspace/project/elbowresearch/flowchart/flowchart.pdf', bbox_inches='tight',
            facecolor='white', edgecolor='none')
print("Flowchart saved as PNG and PDF")