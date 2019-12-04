from typing import Tuple, List

import pygame
from pygame.math import Vector2

from Edges import Edges
import random
from Button import Button
from Vertices import Vertices


#   also occur from

def render_paragraphs(screen, paragragh_font, black):
    screen.blit(paragragh_font.render("Water: Cholera is a waterborne bacterium that", True, black), [865, 20])
    screen.blit(paragragh_font.render("causes diarrhea, vomiting, and leg cramps in", True, black), [865, 40])
    screen.blit(paragragh_font.render("about 10% of the people infected. Without ", True, black), [865, 60])
    screen.blit(paragragh_font.render("treatment in these 10%, death can occur within", True, black), [865, 80])
    screen.blit(paragragh_font.render("hours. An estimated 95,00 deaths occur", True, black), [865, 100])
    screen.blit(paragragh_font.render("worldwide annually. Cholera is found in water ", True, black), [865, 120])
    screen.blit(paragragh_font.render("or food that have been contaminated with the ", True, black), [865, 140])
    screen.blit(paragragh_font.render("feces of a person who has cholera. It can also  ", True, black), [865, 160])
    screen.blit(paragragh_font.render("occur from eating raw shellfish.", True, black), [865, 180])

    screen.blit(paragragh_font.render("Air: The Spanish Flu was an influenza ", True, black), [865, 230])
    screen.blit(paragragh_font.render("pandemic that occurred in 1918-1919. It’s ", True, black), [865, 250])
    screen.blit(paragragh_font.render("estimated about 500 million people (one-third ", True, black), [865, 270])
    screen.blit(paragragh_font.render("of the world’s population) became infected ", True, black), [865, 290])
    screen.blit(paragragh_font.render("with the virus. The death rate is estimated to ", True, black), [865, 310])
    screen.blit(paragragh_font.render("be between 50 to 100 million people worldwide.", True, black), [865, 330])

    screen.blit(paragragh_font.render("Animals: The Plague was rampant between", True, black), [865, 400])
    screen.blit(paragragh_font.render(" 1346-1353, mostly  within Europe. It’s caused", True, black), [865, 420])
    screen.blit(paragragh_font.render("by a bacterium called Yersina pestis which is", True, black), [865, 440])
    screen.blit(paragragh_font.render("transmitted by flea bites. While the exact", True, black), [865, 460])
    screen.blit(paragragh_font.render("number of deaths is unknown, it’s estimated", True, black), [865, 480])
    screen.blit(paragragh_font.render("that around 50 million people died. The", True, black), [865, 500])
    screen.blit(paragragh_font.render("Black Death is not eradicated, and still", True, black), [865, 520])
    screen.blit(paragragh_font.render("an average of 500 people worldwide annually.", True, black), [865, 540])


def isIncident(city, edges):
    for e in edges:
        if e.first[0] == city or e.second[0] == city:
            return True
    return False


def generateEdges(cities, edges, type):
    for node in cities:
        if isIncident(node, edges):
            cityEdges = []
            for e in edges:
                if e.first[0] == node or e.second[0] == node:
                    cityEdges.append(e)
            for i in range(int(len(cityEdges) / 2)):
                edge = random.randint(0, len(cityEdges) - 1)
                cityEdges[edge].type = type

    if isIncident((70, 320), edges):
        cityEdges = []
        for e in edges:
            if e.first[0] == (70, 320) or e.second[0] == (70, 320):
                cityEdges.append(e)
        for i in range(int(len(cityEdges) / 2)):
            edge = random.randint(0, len(cityEdges) - 1)
            cityEdges[edge].type = type

    if isIncident((720, 490), edges):
        cityEdges = []
        for e in edges:
            if e.first[0] == (720, 490) or e.second[0] == (720, 490):
                cityEdges.append(e)
        for i in range(int(len(cityEdges) / 2)):
            edge = random.randint(0, len(cityEdges) - 1)
            cityEdges[edge].type = type


def main() -> None:
    cities = {
        (765, 175): [(735, 220), (560, 190), (480, 130)],  # New York
        (735, 220): [(630, 340), (560, 190), (720, 490)],  # DC
        (630, 340): [(420, 420), (720, 490), (560, 190)],  # Atlanta
        (560, 190): [(480, 130), (420, 420), (300, 230)],  # Chicago
        (480, 130): [(300, 230), (80, 30)],  # Minneapolis
        (80, 30): [(70, 320), (300, 230)],  # Seattle
        (420, 420): [(300, 230), (70, 320), (720, 490)],  # Austin
        (300, 230): [(70, 320)],  # Denver
        # Vertices(pos=(200, 400))
    }

    pygame.init()
    screen = pygame.display.set_mode([1200, 625], pygame.FULLSCREEN)
    bg_color = [255, 255, 255]
    screen.fill(bg_color)
    black = [0, 0, 0]
    pygame.display.set_caption('Disease Graph')
    image = pygame.image.load('us.gif')
    font = pygame.font.Font("freesansbold.ttf", 16)
    paragragh_font = pygame.font.Font("freesansbold.ttf", 14)

    buttons = [
        Button(80, 40, (1100, 180), "Cholera", [0, 0, 150], font, "Cholera"),
        Button(100, 40, (1085, 350), "Spanish Flu", [150, 0, 0], font, "Flu"),
        Button(80, 40, (1100, 560), "Plague", [0, 150, 0], font, "Plague")
    ]

    # Game loop
    running = True
    fps = 60
    dt = 1 / fps
    clock = pygame.time.Clock()
    is_selected = False
    disease_selected = ""
    city_selected = False

    vertices = [
        Vertices(10, pos=Vector2(765, 175), id="New York"),
        Vertices(10, pos=Vector2(735, 220), id="DC"),
        Vertices(10, pos=Vector2(630, 340), id="Atlanta"),
        Vertices(10, pos=Vector2(560, 190), id="Chicago"),
        Vertices(10, pos=Vector2(420, 420), id="Austin"),
        Vertices(10, pos=Vector2(70, 320), id="LA"),
        Vertices(10, pos=Vector2(480, 130), id="Minneapolis"),
        Vertices(10, pos=Vector2(720, 490), id="Miami"),
        Vertices(10, pos=Vector2(80, 30), id="Seattle"),
        Vertices(10, pos=Vector2(300, 230), id="Denver")
    ]

    edges = []

    for node in cities:
        for neighbor in cities[node]:
            edge = Edges()
            edge.add_edge(node, neighbor)
            edge.generate_weights()
            # edge.generate_edge_type()
            edges.append(edge)

    connected_edges = []
    lowest = 21
    unselected_vertices = []
    selected_vertices = []
    type = ""

    for v in vertices:
        unselected_vertices.append(v)

    while running:
        screen.fill(bg_color)
        screen.blit(image, (0, 0))

        render_paragraphs(screen, paragragh_font, black)

        screen.blit(font.render("Legend for edges:", True, black), [35, 445])
        screen.blit(font.render("Water", True, (0, 0, 255)), [60, 475])
        screen.blit(font.render("Air", True, black), [60, 500])
        screen.blit(font.render("Animals", True, (255, 0, 0)), [60, 525])

        screen.blit(font.render("New York", True, black), [775, 170])
        screen.blit(font.render("DC", True, black), [745, 230])
        screen.blit(font.render("Atlanta", True, black), [640, 330])
        screen.blit(font.render("Chicago", True, black), [560, 165])
        screen.blit(font.render("Austin", True, black), [420, 435])
        screen.blit(font.render("LA", True, black), [40, 295])
        screen.blit(font.render("Minneapolis", True, black), [480, 105])
        screen.blit(font.render("Miami", True, black), [730, 465])
        screen.blit(font.render("Seattle", True, black), [20, 40])
        screen.blit(font.render("Denver", True, black), [320, 240])

        # New York-DC
        screen.blit(font.render(str(edges[0].weight), True, black), [755, 200])
        # New York-Chicago
        screen.blit(font.render(str(edges[1].weight), True, black), [665, 165])
        # New York-Minneapolis
        screen.blit(font.render(str(edges[2].weight), True, black), [625, 135])
        # Dc-Atlanta
        screen.blit(font.render(str(edges[3].weight), True, black), [690, 280])
        # DC-Chicago
        screen.blit(font.render(str(edges[4].weight), True, black), [650, 210])
        # DC-Miami
        screen.blit(font.render(str(edges[5].weight), True, black), [735, 355])
        # Atlanta-Austin
        screen.blit(font.render(str(edges[6].weight), True, black), [535, 380])
        # Atlata-Miami
        screen.blit(font.render(str(edges[7].weight), True, black), [685, 400])
        # Atlanta-Chicago
        screen.blit(font.render(str(edges[8].weight), True, black), [600, 245])
        # Chicago-Minneapolis
        screen.blit(font.render(str(edges[9].weight), True, black), [520, 145])
        # Chicago-Austin
        screen.blit(font.render(str(edges[10].weight), True, black), [500, 300])
        # Chicago-Denver
        screen.blit(font.render(str(edges[11].weight), True, black), [440, 215])
        # Minneapolis-Denver
        screen.blit(font.render(str(edges[12].weight), True, black), [405, 175])
        # Minneapolis-Seattle
        screen.blit(font.render(str(edges[13].weight), True, black), [250, 80])
        # Seattle-LA
        screen.blit(font.render(str(edges[14].weight), True, black), [50, 170])
        # Seattle-Denver
        screen.blit(font.render(str(edges[15].weight), True, black), [170, 140])
        # Austin-Denver
        screen.blit(font.render(str(edges[16].weight), True, black), [370, 320])
        # Austin-LA
        screen.blit(font.render(str(edges[17].weight), True, black), [230, 375])
        # Austin-Miami
        screen.blit(font.render(str(edges[18].weight), True, black), [575, 440])
        # Denver-LA
        screen.blit(font.render(str(edges[19].weight), True, black), [180, 255])

        for e in edges:
            if not e.selected:
                e.draw(screen)
            else:
                e.draw(screen, [255, 0, 255])

        for b in buttons:
            b.draw(screen)

        for v in vertices:
            v.draw(screen)

        if city_selected:
            if disease_selected == "Cholera":
                type = "water"
            elif disease_selected == "Flu":
                type = "air"
            elif disease_selected == "Plague":
                type = "animals"

            while len(selected_vertices) < 9:
                connected_edges.clear()
                for v in unselected_vertices:
                    if v.id == the_city_selected:
                        selected_vertices.append(v)
                        unselected_vertices.remove(v)

                for e in edges:
                    for vert in selected_vertices:
                        if e.type == type:
                            if e.first[0] == vert.pos or e.second[0] == vert.pos:
                                # if not connected_edges.__contains__(e) and not e.selected:
                                if e.first[0] not in selected_vertices and e.second[0] not in selected_vertices:
                                    connected_edges.append(e)
                        if e.type == type:
                            if e.first[0] == vert.pos or e.second[0] == vert.pos:
                                if e.first[0] not in selected_vertices and e.second[0] not in selected_vertices:
                                    connected_edges.append(e)
                        if e.type == type:
                            if e.first[0] == vert.pos or e.second[0] == vert.pos:
                                if e.first[0] not in selected_vertices and e.second[0] not in selected_vertices:
                                    connected_edges.append(e)

                for ce in connected_edges:
                    print(ce.weight)
                    if ce.weight < lowest and not ce.selected:
                        if not (any(x.pos == ce.first[0] for x in selected_vertices) and any(
                                y.pos == ce.second[0] for y in selected_vertices)):
                            lowest = ce.weight
                            lowest_edge = ce

                for ce in connected_edges:

                    if ce == lowest_edge:
                        ce.draw(screen, [255, 0, 255])
                        ce.selected = True

                        for vs in selected_vertices:
                            if ce.first[0] == vs.pos:
                                temp = ce.second[0]
                                for v in unselected_vertices:
                                    if v.pos == temp:
                                        the_city_selected = v.id
                                        for ve in vertices:
                                            if ve.id == v.id:
                                                ve.change_color([255, 0, 255])
                            elif ce.second[0] == vs.pos:
                                temp = ce.first[0]
                                for v in unselected_vertices:
                                    if v.pos == temp:
                                        the_city_selected = v.id
                                        for ve in vertices:
                                            if ve.id == v.id:
                                                ve.change_color([255, 0, 255])
                lowest = 21

        pygame.display.flip()
        # Event Loop
        for e in pygame.event.get():
            if e.type == pygame.QUIT or e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                running = False
            elif e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                for v in vertices:
                    if v.rect.collidepoint(pygame.mouse.get_pos()):
                        if v.id == "New York" and not city_selected and is_selected:
                            city_selected = True
                            v.change_color([255, 0, 255])
                            the_city_selected = "New York"
                        elif v.id == "DC" and not city_selected and is_selected:
                            city_selected = True
                            v.change_color([255, 0, 255])
                            the_city_selected = "DC"
                        elif v.id == "Atlanta" and not city_selected and is_selected:
                            city_selected = True
                            v.change_color([255, 0, 255])
                            the_city_selected = "Atlanta"
                        elif v.id == "Chicago" and not city_selected and is_selected:
                            city_selected = True
                            v.change_color([255, 0, 255])
                            the_city_selected = "Chicago"
                        elif v.id == "Austin" and not city_selected and is_selected:
                            city_selected = True
                            v.change_color([255, 0, 255])
                            the_city_selected = "Austin"
                        elif v.id == "LA" and not city_selected and is_selected:
                            city_selected = True
                            v.change_color([255, 0, 255])
                            the_city_selected = "LA"
                        elif v.id == "Minneapolis" and not city_selected and is_selected:
                            city_selected = True
                            v.change_color([255, 0, 255])
                            the_city_selected = "Minneapolis"
                        elif v.id == "Miami" and not city_selected and is_selected:
                            city_selected = True
                            v.change_color([255, 0, 255])
                            the_city_selected = "Miami"
                        elif v.id == "Seattle" and not city_selected and is_selected:
                            city_selected = True
                            v.change_color([255, 0, 255])
                            the_city_selected = "Seattle"
                        elif v.id == "Denver" and not city_selected and is_selected:
                            city_selected = True
                            v.change_color([255, 0, 255])
                            the_city_selected = "Denver"

                for b in buttons:
                    if b.rect.collidepoint(pygame.mouse.get_pos()):
                        if b.id == "Cholera":
                            if is_selected:
                                for bu in buttons:
                                    if disease_selected == "Flu" and bu.id == "Flu":
                                        bu.change_background([150, 0, 0])
                                    elif disease_selected == "Plague" and bu.id == "Plague":
                                        bu.change_background([0, 150, 0])
                            b.change_background([255, 255, 0])
                            is_selected = True
                            disease_selected = "Cholera"
                            generateEdges(cities, edges, "water")

                            for e in edges:
                                if e.type != "water":
                                    e.type = random.choice(["air", "animals"])
                        elif b.id == "Flu":
                            if is_selected:
                                for bu in buttons:
                                    if disease_selected == "Cholera" and bu.id == "Cholera":
                                        bu.change_background([0, 0, 150])
                                    elif disease_selected == "Plague" and bu.id == "Plague":
                                        bu.change_background([0, 150, 0])
                            b.change_background([255, 255, 0])
                            is_selected = True
                            disease_selected = "Flu"
                            generateEdges(cities, edges, "air")

                            for e in edges:
                                if e.type != "air":
                                    e.type = random.choice(["water", "animals"])
                        elif b.id == "Plague":
                            if is_selected:
                                for bu in buttons:
                                    if disease_selected == "Flu" and bu.id == "Flu":
                                        bu.change_background([150, 0, 0])
                                    elif disease_selected == "Cholera" and bu.id == "Cholera":
                                        bu.change_background([0, 0, 150])
                            b.change_background([255, 255, 0])
                            is_selected = True
                            disease_selected = "Plague"
                            generateEdges(cities, edges, "animals")

                            for e in edges:
                                if e.type != "animals":
                                    e.type = random.choice(["air", "water"])

                        for e in edges:
                            e.draw(screen)

    # Shut down pygame
    pygame.quit()


if __name__ == "__main__":
    try:
        main()
    finally:
        pygame.quit()
