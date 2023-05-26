"""

    This file is a part of the 'Pygame Examples (pgex)' source code.
    The source code is distributed under the MIT license.

    Polygon collision calculations in this example uses
    an algorithm called SAT (Separating Axis Theorem).
    Here are some good resources on it for further information:
      https://www.sevenson.com.au/programming/sat
      http://programmerart.weebly.com/separating-axis-theorem.html

"""

from dataclasses import dataclass
from math import sin
import asyncio

import pygame


@dataclass
class Circle:
    """
    Circle is the most basic collision shape.
    It is defined by just a center position and radius.
    """

    center: pygame.Vector2
    radius: float


@dataclass
class Polygon:
    """
    Convex polygons are the most expensive collision shapes.
    Calculation gets more costly as the number of vertices increase.    
    """

    center: pygame.Vector2
    vertices: list[pygame.Vector2]
    angle: float = 0.0

    def local_to_world(self) -> list[pygame.Vector2]:
        """ Transform vertices from local space to world space. """
        return [vertex.rotate(self.angle) + self.center for vertex in self.vertices]


def circle_x_circle(circle_a: Circle, circle_b: Circle) -> bool:
    """ Check collision between two circles. """

    distance = circle_b.center.distance_squared_to(circle_a.center)
    radii = (circle_a.radius + circle_b.radius) ** 2

    return distance <= radii

def rect_x_circle(rect: pygame.FRect, circle: Circle) -> bool:
    """ Check collision between rectangle and circle. """

    center = circle.center.copy()

    # Rect borders
    right = rect.x + rect.width
    left = rect.x
    bottom = rect.y + rect.height
    top = rect.y

    # Check circle center against rect borders
    if center.x > right: center.x = right
    elif center.x < left: center.x = left
    if center.y > bottom: center.y = bottom
    elif center.y < top: center.y = top

    # Check distance against original center
    return center.distance_squared_to(circle.center) < circle.radius ** 2

def project_circle(
        circle: Circle,
        axis: pygame.Vector2
        ) -> tuple[float, float]:
    """ SAT helper function to project circle onto an axis. """

    axis_radius = axis.normalize() * circle.radius

    p1 = circle.center + axis_radius
    p2 = circle.center - axis_radius

    min_ = p1.dot(axis)
    max_ = p2.dot(axis)

    # Swap min max values if needed
    if (min_ > max_):
        min_, max_ = max_, min_

    return (min_, max_)

def project_polygon(
        polygon: Polygon,
        axis: pygame.Vector2
        ) -> tuple[float, float]:
    """ SAT helper function to project polygon vertices onto an axis. """

    min_ = float("inf")
    max_ = float("-inf")

    for vertex in polygon.local_to_world():
        projection = vertex.dot(axis)

        if projection < min_: min_ = projection

        if projection > max_: max_ = projection

    return (min_, max_)

def polygon_x_circle(polygon: Polygon, circle: Circle) -> bool:
    """ Check collision between polygon and circle. """

    vertices = polygon.local_to_world()
    n = len(vertices)

    for i in range(n):
        va = vertices[i]
        vb = vertices[(i + 1) % n]

        edge = vb - va
        axis = edge.normalize()
        axis = pygame.Vector2(-axis.y, axis.x)

        min_a, max_a = project_polygon(polygon, axis)
        min_b, max_b = project_circle(circle, axis)

        if min_a >= max_b or min_b >= max_a:
            return False
    
    return True

def polygon_x_rect(polygon: Polygon, rect: pygame.FRect) -> bool:
    """ Check collision between polygon and rectangle. """

    # IMPORTANT: A better approach would be clipping the polygon and testing
    #            against the rect. But for now we are just treating the rect
    #            as another polygon.

    rect_center = pygame.Vector2(*rect.center)

    rect_vertices = [
        pygame.Vector2(*rect.topleft) - rect_center,
        pygame.Vector2(*rect.topright) - rect_center,
        pygame.Vector2(*rect.bottomright) - rect_center,
        pygame.Vector2(*rect.bottomleft) - rect_center
    ]

    rect_poly = Polygon(rect_center, rect_vertices)

    return polygon_x_polygon(polygon, rect_poly)

def polygon_x_polygon(polygon_a: Polygon, polygon_b: Polygon) -> bool:
    """ Check collision between two polygons. """

    vertices_a = polygon_a.local_to_world()
    vertices_b = polygon_b.local_to_world()
    na = len(vertices_a)
    nb = len(vertices_b)

    # Check for polygon A's edges
    for i in range(na):
        va = vertices_a[i]
        vb = vertices_a[(i + 1) % na]

        edge = vb - va
        axis = edge.normalize()
        axis = pygame.Vector2(-axis.y, axis.x)

        min_a, max_a = project_polygon(polygon_a, axis)
        min_b, max_b = project_polygon(polygon_b, axis)

        if min_a >= max_b or min_b >= max_a:
            return False
    
    # Check for polygon B's edges
    for i in range(nb):
        va = vertices_b[i]
        vb = vertices_b[(i + 1) % nb]

        edge = vb - va
        axis = edge.normalize()
        axis = pygame.Vector2(-axis.y, axis.x)

        min_a, max_a = project_polygon(polygon_a, axis)
        min_b, max_b = project_polygon(polygon_b, axis)

        if min_a >= max_b or min_b >= max_a:
            return False
        
    return True


async def main() -> None:
    pygame.init()
    window = pygame.display.set_mode((450, 140))
    pygame.display.set_caption("PGEX Collision Shapes Example")
    clock = pygame.time.Clock()
    
    # Prepare scene

    circles = []

    circles.append( Circle(pygame.Vector2(50, 50), 30) )
    circles.append( Circle(pygame.Vector2(90, 90), 20) )
    circles.append( Circle(pygame.Vector2(330, 90), 15) )

    rects = []

    rects.append( pygame.FRect(113, 25, 80, 50) )
    rects.append( pygame.FRect(180, 50, 30, 65) )

    polygons = []

    pentagon_vertices = [
        pygame.Vector2(25, 34), pygame.Vector2(40, -13), pygame.Vector2(0, -43),
        pygame.Vector2(-40, -13), pygame.Vector2(-25, 34)
    ]

    triangle_vertices = [
        pygame.Vector2(27, 27),
        pygame.Vector2(-37, 10),
        pygame.Vector2(10, -37)
    ]

    polygons.append( Polygon(pygame.Vector2(270, 50), pentagon_vertices) )
    polygons.append( Polygon(pygame.Vector2(370, 50), triangle_vertices) )

    # This list will be used to check collision between all shapes
    # Check the note in line 177
    all_shapes = circles + rects + polygons


    while True:
        clock.tick(165)
        ticks = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit(0)
            
        # Move shapes
        circles[1].center = pygame.Vector2(90, 90) + pygame.Vector2(20).rotate(ticks / 3)
        circles[2].center = pygame.Vector2(330, 90) + pygame.Vector2(20).rotate(ticks / 5)
        rects[1].center = pygame.Vector2(205, 82.5) + pygame.Vector2(0, 40).rotate(ticks / 3)
        polygons[0].angle = int(ticks / 10)
        polygons[1].angle = -int(ticks / 10)
        polygons[1].center.x = 350 + sin(ticks / 400) * 40

        # This set contains references to collided shapes each frame for rendering
        collided = []

        # Check colliding shapes
        # IMPORTANT: This is a really inefficient way if there are lots of shapes in the world.
        #            Since this is just a showcase demo we are iteratting over all shapes.
        for shape_a in all_shapes:
            for shape_b in all_shapes:

                # Early out if the two reference to same shape
                if shape_a is shape_b: continue

                # Circle and circle collision
                if isinstance(shape_a, Circle) and isinstance(shape_b, Circle):
                    if circle_x_circle(shape_a, shape_b):
                        collided.append(shape_a)
                        collided.append(shape_b)

                # Rect and circle collision
                elif isinstance(shape_a, pygame.FRect) and isinstance(shape_b, Circle):
                    if rect_x_circle(shape_a, shape_b):
                        collided.append(shape_a)
                        collided.append(shape_b)

                # Rect and rect collision
                elif isinstance(shape_a, pygame.FRect) and isinstance(shape_b, pygame.FRect):
                    if shape_a.colliderect(shape_b):
                        collided.append(shape_a)
                        collided.append(shape_b)

                # Polygon and circle collision
                elif isinstance(shape_a, Polygon) and isinstance(shape_b, Circle):
                    if polygon_x_circle(shape_a, shape_b):
                        collided.append(shape_a)
                        collided.append(shape_b)

                # Polygon and rect collision
                elif isinstance(shape_a, Polygon) and isinstance(shape_b, pygame.FRect):
                    if polygon_x_rect(shape_a, shape_b):
                        collided.append(shape_a)
                        collided.append(shape_b)

                # Polygon and polygon collision
                elif isinstance(shape_a, Polygon) and isinstance(shape_b, Polygon):
                    if polygon_x_polygon(shape_a, shape_b):
                        collided.append(shape_a)
                        collided.append(shape_b)

        # Render scene

        window.fill((255, 255, 255))

        for shape in all_shapes:
            if shape in collided:
                color = (187, 255, 77)
                outline_color = (23, 145, 97)
            else:
                color = (255, 144, 18)
                outline_color = (156, 23, 23)

            if isinstance(shape, Circle):
                pygame.draw.circle(window, color, shape.center, shape.radius)
                pygame.draw.circle(window, outline_color, shape.center, shape.radius, 1)

            elif isinstance(shape, pygame.FRect):
                pygame.draw.rect(window, color, shape)
                pygame.draw.rect(window, outline_color, shape, 1)
            
            elif isinstance(shape, Polygon):
                pygame.draw.polygon(window, color, shape.local_to_world())
                pygame.draw.polygon(window, outline_color, shape.local_to_world(), 1)

        pygame.display.flip()

        asyncio.sleep(0)


def run() -> None:
    asyncio.run(main())


if __name__ == "__main__":
    run()