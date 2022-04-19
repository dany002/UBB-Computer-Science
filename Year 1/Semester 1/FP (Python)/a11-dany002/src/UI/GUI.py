import pygame

pygame.init()

display_width = 1366
display_height = 1000
window = pygame.display.set_mode((display_width, display_height))

class GUI(object):
    def __init__(self, display_width, display_height):
        self._display_width = display_width
        self._display_height = display_height
        self.main()

    def main(self):
        # Put all variables up here
        stopped = False
        white = (255, 255, 255)

        pygame.display.update()
        window.fill((0, 0, 0))
        #self.draw_button(10, 10, white)
        self._create_board()
        self._main_menu()
        print("Where do you want to be the cabin ?")
        while stopped == False:

            # Event Tasking
            # Add all your event tasking things here
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() # for exit
                    quit()
                elif event.type == pygame.KEYDOWN:
                    stopped = True
            pygame.display.update()
            # Add things like player updates here
            # Also things like score updates or drawing additional items
            # Remember things on top get done first so they will update in the order yours is set at

            # Remember to update your clock and display at the end



        # If you need to reset variables here
        # This includes things like score resets

    # After your main loop throw in extra things such as a main menu or a pause menu
    # Make sure you throw them in your main loop somewhere where

    def _create_board(self):
        first_coordinate = 120
        second_coordinate = 120
        while second_coordinate < 900:
            self.draw_button(first_coordinate, second_coordinate, (255, 255, 255))
            if first_coordinate > 1000:
                second_coordinate += 80
                first_coordinate = 20
            first_coordinate += 100


    def _main_menu(self):
        pygame.draw.rect(window, (234, 20, 0), (250, 10, 690, 50))
        pygame.display.update()


    def draw_button(self, first_coordinate, second_coordinate, color):
        pygame.draw.rect(window, color,(first_coordinate, second_coordinate, 50, 50))
        pygame.display.update()



if __name__ == "__main__":
    GUI(display_width, display_height)