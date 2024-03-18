import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window_width = 1024
window_height = 768
tick_time = 60

class Cube:

    def __init__(self):
        self.vertices = (
            (1, -1, -1),
            (1, 1, -1),
            (-1, 1, -1),
            (-1, -1, -1),
            (1, -1, 1),
            (1, 1, 1),
            (-1, -1, 1),
            (-1, 1, 1)
        )

        self.edges = (
            (0, 1),
            (0, 3),
            (0, 4),
            (2, 1),
            (2, 3),
            (2, 7),
            (6, 3),
            (6, 4),
            (6, 7),
            (5, 1),
            (5, 4),
            (5, 7)
        )

        self.colors = (
            (235/255, 52/255, 186/255),
            (134/255, 52/255, 235/255),
            (255/255, 0/255, 111/255),
            (253/255, 145/255, 255/255),
            (255/255, 0/255, 111/255),
            (253/255, 145/255, 255/255),
            (134/255, 52/255, 235/255),
            (235/255, 52/255, 186/255)
        )

    def draw(self):
        glBegin(GL_LINES)
        for edge in self.edges:
            for vertex in edge:
                glColor3fv(self.colors[vertex])
                glVertex3fv(self.vertices[vertex])
        glEnd()

def main():
    pygame.init()
    display = (window_width, window_height)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.10, 50.0)
    glTranslatef(0.0, 0.0, -5)

    clock = pygame.time.Clock()
    fps = 0
    cube = Cube()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        cube.draw()
        pygame.display.flip()
        fps = clock.get_fps()
        pygame.display.set_caption('Qube - FPS: {}'.format(int(fps)))
        clock.tick(int(tick_time))

if __name__ == "__main__":
    main()
