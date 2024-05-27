import numpy as np
from math import cos, sin, radians
from pygame.math import Vector2
from pygame.locals import *


def generate_uniform_poly(origin, point_count, radius):
    origin = Vector2(origin)
    np_verts = np.array([Vector2(origin.x + (radius * cos(radians(x * (360 / point_count)))),
                             origin.y + (radius * sin(radians(x * (360 / point_count))))) for x in range(point_count)])
    return [Vector2(v) for v in np_verts.tolist()]


def rotate(vector, theta, rotation_around=None) -> np.ndarray:
    vector = np.array(vector)

    if vector.ndim == 1:
        vector = vector[np.newaxis, :]

    if rotation_around is not None:
        vector = vector - rotation_around

    vector = vector.T

    theta = np.radians(theta)

    rotation_matrix = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta), np.cos(theta)]
    ])

    output: np.ndarray = (rotation_matrix @ vector).T

    if rotation_around is not None:
        output = output + rotation_around

    return output.squeeze()


def scale(vector, scale, scale_origin=None) -> np.ndarray:
    vector = np.array(vector)

    if vector.ndim == 1:
        vector = vector[np.newaxis, :]

    if scale_origin is not None:
        vector = vector - scale_origin

    vector = vector.T

    scale_matrix = np.array([
        [scale, 0],
        [0, scale]
    ])

    output = (scale_matrix @ vector).T

    if scale_origin is not None:
        output = output + scale_origin

    return output.squeeze()


def translate(vector, offset) -> np.ndarray:
    vector = np.array(vector)
    offset = np.array(offset)
    vec = vector + offset
    return vec


def centroid(vertices):
    x, y = 0, 0
    n = len(vertices)
    signed_area = 0
    for i in range(len(vertices)):
        x0, y0 = vertices[i]
        x1, y1 = vertices[(i + 1) % n]
        # shoelace formula
        area = (x0 * y1) - (x1 * y0)
        signed_area += area
        x += (x0 + x1) * area
        y += (y0 + y1) * area

    signed_area *= 0.5
    if signed_area >= 1:
        x /= 6 * signed_area
        y /= 6 * signed_area

    return Vector2(x, y)


def point_line_distance(point, line_start, line_end):
    """Calculate the minimum distance between a point and a line segment."""
    # Convert points to numpy arrays for easier math
    p = np.array(point)
    a = np.array(line_start)
    b = np.array(line_end)

    # Calculate the vector from start to end of the line, and from start of line to point
    line_vec = b - a
    point_vec = p - a

    # Calculate the length squared of the line vector (avoiding a sqrt until absolutely necessary)
    line_len_sq = np.dot(line_vec, line_vec)

    # Calculate parameter t for the point on the line segment closest to the point
    t = max(0, min(1, np.dot(point_vec, line_vec) / line_len_sq))

    # Calculate the coordinates of the closest point on the line segment
    closest_point = a + t * line_vec

    # Return the distance from the point to this closest point
    return np.linalg.norm(p - closest_point)


def is_point_on_line(point, line_start, line_end, thickness):
    distance = point_line_distance(point, line_start, line_end)
    return distance <= thickness / 2


def pad_rect(rect, padding):
    new_rect = Rect(rect)
    new_rect[2] += padding[0] * 2
    new_rect[3] += padding[1] * 2
    return Rect(new_rect)
