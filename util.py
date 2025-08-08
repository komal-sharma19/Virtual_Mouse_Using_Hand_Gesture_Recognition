import numpy as np

# -------------------
# Utility functions
# -------------------
def get_distance(landmark_list):
    """Calculate distance between two normalized points and scale."""
    (x1, y1), (x2, y2) = landmark_list[0],landmark_list[1]
    L = np.hypot(x2 - x1, y2 - y1)  # Normalized distance
    return np.interp(L,[0,1],[0,1000])  # Scale to pixel-like value

def get_angle(a, b, c):
    """Calculate angle between three points (normalized coords)."""
    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(np.degrees(radians))
    return angle