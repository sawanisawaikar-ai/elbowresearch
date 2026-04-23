import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch

fig, ax = plt.subplots(1, 1, figsize=(14, 18))
ax.set_xlim(0, 14)
ax.set_ylim(0, 18)
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
    'treatment': '#bbdefb',
    'surgery': '#d1c4e9',
}

def draw_rounded_box(ax, x, y, width, height, text, facecolor, bordercolor, fontsize=9):
    box = FancyBboxPatch((x - width/2, y - height/2), width, height,
                         boxstyle="round,pad=0.05,rounding_size=0.3",
                         facecolor=facecolor, edgecolor=bordercolor, linewidth=2)
    ax.add_patch(box)
    ax.text(x, y, text, ha='center', va='center', fontsize=fontsize,
            fontweight='bold', wrap=True)

def draw_diamond(ax, x, y, size, text, fontsize=8):
    diamond = plt.Polygon([(x, y + size), (x + size, y), (x, y - size), (x - size, y)],
                          facecolor=colors['decision'], edgecolor=colors['border_decision'], linewidth=2)
    ax.add_patch(diamond)
    ax.text(x, y, text, ha='center', va='center', fontsize=fontsize, fontweight='bold')

def draw_arrow(ax, start, end, color='#666666'):
    ax.annotate('', xy=end, xytext=start,
                arrowprops=dict(arrowstyle='->', color=color, lw=2))

# Title
ax.text(7, 17.5, 'Lateral Epicondylopathy (Tennis Elbow) - Clinical Management',
        ha='center', va='center', fontsize=14, fontweight='bold', color='#333')

# START
draw_rounded_box(ax, 7, 16.5, 4, 0.6, 'Patient presents with\nlateral elbow pain', 
                 colors['start'], colors['border_start'])

# Assessment
draw_arrow(ax, (7, 16.2), (7, 15.6))
draw_rounded_box(ax, 7, 15.3, 4, 0.6, 'Clinical Assessment\n(Cozen\'s test, Mill\'s test, palpation)', 
                 colors['process'], colors['border_process'])

# Diagnosis diamond
draw_arrow(ax, (7, 14.95), (7, 14.4))
draw_diamond(ax, 7, 14.2, 0.5, 'Confirmed?')

# NO - Rule out
draw_arrow(ax, (6.5, 14.2), (4, 14.2))
draw_rounded_box(ax, 2.5, 14.2, 2, 0.6, 'Rule out other\nconditions', 
                 colors['warning'], colors['border_warning'], fontsize=8)

# YES - Confirmed
draw_arrow(ax, (7.5, 14.2), (10, 14.2))
draw_rounded_box(ax, 11.5, 14.2, 2.5, 0.6, 'Confirmed\ndiagnosis', 
                 colors['success'], colors['border_success'], fontsize=9)

# Duration check
draw_arrow(ax, (11.5, 13.9), (11.5, 13.4))
draw_diamond(ax, 11.5, 13.2, 0.5, 'Duration?')

# Acute path
draw_arrow(ax, (11, 13.2), (9, 13.2))
draw_rounded_box(ax, 8, 13.2, 2, 0.6, 'Acute\n(< 3 mo)', 
                 colors['treatment'], '#2196f3', fontsize=9)

# Chronic path
draw_arrow(ax, (11.5, 12.7), (11.5, 12.3))
draw_rounded_box(ax, 11.5, 12, 2, 0.6, 'Chronic\n(> 3 mo)', 
                 colors['surgery'], '#7c4dbf', fontsize=9)

# Treatment boxes
draw_rounded_box(ax, 5, 12, 3, 1, 'Phase 1: Acute\n• Activity modification\n• Ice therapy\n• Isometric exercises',
                 colors['treatment'], '#2196f3', fontsize=8)

draw_rounded_box(ax, 10, 11, 3, 1, 'Phase 2: Chronic\n• Eccentric exercises\n• Physical therapy\n• Consider surgery if needed',
                 colors['surgery'], '#7c4dbf', fontsize=8)

# Converge
draw_arrow(ax, (5, 11.5), (5, 10.5))
draw_arrow(ax, (10, 10.5), (5, 10.5))
draw_arrow(ax, (5, 10.5), (7, 10.5))
draw_arrow(ax, (7, 10.5), (7, 9.7))

# Progress check
draw_diamond(ax, 7, 9.5, 0.5, 'Better?')

# Yes path
draw_arrow(ax, (7.5, 9.5), (10, 9.5))
draw_rounded_box(ax, 11.5, 9.5, 2.5, 0.6, 'Continue\ntreatment', 
                 colors['success'], colors['border_success'], fontsize=9)

# No path  
draw_arrow(ax, (7, 9), (7, 8.5))
draw_rounded_box(ax, 7, 8.2, 4, 0.6, 'Consider alternative\ntreatments or surgery',
                 colors['surgery'], '#7c4dbf', fontsize=9)

# Outcome
draw_arrow(ax, (11.5, 9.2), (11.5, 8.2))
draw_arrow(ax, (11.5, 8.2), (7, 8.2))
draw_arrow(ax, (7, 8.2), (7, 7.9))
draw_arrow(ax, (7, 7.9), (7.3, 7.9))

draw_rounded_box(ax, 7, 7.5, 5, 0.6, '90-95% success with\nconservative treatment', 
                 colors['success'], colors['border_success'], fontsize=10)

# Prevention
draw_arrow(ax, (7, 7.2), (7, 6.6))
draw_rounded_box(ax, 7, 6.3, 4.5, 0.6, 'Prevention: Activity modification,\nergonomic adjustments',
                 '#e0f7fa', '#00bcd4', fontsize=9)

# Legend
legend_y = 5
ax.text(7, legend_y + 0.5, 'Legend', ha='center', va='center', fontsize=11, fontweight='bold')

legend_items = [
    ('Assessment/Diagnosis', colors['process'], colors['border_process']),
    ('Treatment', colors['treatment'], '#2196f3'),
    ('Caution', colors['warning'], colors['border_warning']),
    ('Success/Outcome', colors['success'], colors['border_success'])
]

for i, (label, fc, bc) in enumerate(legend_items):
    x_pos = 2 + (i * 2.8)
    rect = FancyBboxPatch((x_pos - 1.2, legend_y - 0.25), 2.4, 0.5,
                          boxstyle="round,pad=0.02,rounding_size=0.1",
                          facecolor=fc, edgecolor=bc, linewidth=2)
    ax.add_patch(rect)
    ax.text(x_pos, legend_y, label, ha='center', va='center', fontsize=8)

# Footer
ax.text(7, 1, 'Based on clinical guidelines for lateral epicondylopathy management',
        ha='center', va='center', fontsize=10, color='#666', style='italic')

plt.tight_layout()
plt.savefig('/workspace/project/elbowresearch/flowchart2/flowchart.png', dpi=150, bbox_inches='tight', 
            facecolor='white', edgecolor='none')
plt.savefig('/workspace/project/elbowresearch/flowchart2/flowchart.pdf', bbox_inches='tight',
            facecolor='white', edgecolor='none')
print("Flowchart saved as PNG and PDF")