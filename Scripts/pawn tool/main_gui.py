import tkinter as tk
from components.MenuFrame import MenuFrame
from components.SpecialInfoBox import SpecialInfoBox
from components.InfoBox import InfoBox

# Used to get the screen resolution for sizing the tkinter box
import screeninfo



# Current design is that the menu frame controls all of the other frames. Have to look into 
class MainApplication(tk.Tk):

    def __init__(self, screen_width, screen_height):
        super().__init__()
        # Creates the root window and makes it 60% the screen size
        self.title("Frame Example")
        self.config(bg="skyblue")

        root_width = int(screen_width * 0.6)
        root_height = int(screen_height * 0.6)
        self.maxsize(root_width, root_height)
    #    root.geometry(f'{root_width}x{root_height}')

        # Make the frame for displaying the info on top left for blank for now.
        # * Maybe this could be like an area for telling me the forfeiture rate for 
        # that person *
        # left_frame = Frame(root, width=root_width // 4, height=root_height * 0.2, bg="white")
        # left_frame.grid(row=0, column=0, padx=10, pady=5)

        # # Make the frame for displaying the info on bottom left for menu options 
        # left_frame_2 = Frame(root, width=root_width // 4, height=root_height * .8, bg="white")
        # left_frame_2.grid(row=1, column=0, padx=10, pady=5)

        # # Make the frame for displaying the majority of the info on the right
        # right_frame = Frame(root, width=root_width * 0.75, height=root_height * 0.95, bg="white")
        # right_frame.grid(row=0, column=1)
        
        # Try strategy with two vertical boxes to build other boxes into
        left_frame = tk.Frame(self, width = int(root_width // 4.1), height=int(root_height * 0.95))
        left_frame.grid(row=0, column=0, padx=int(root_width * 0.005), pady=int(root_height * 0.005))

        right_frame = tk.Frame(self, width = int(root_width * 0.7), height=int(root_height * 0.95))
        right_frame.grid(row=0, column=1, padx=int(root_width * 0.005), pady=int(root_height * 0.005))

        
        # Right Frame info
        self.info_box = InfoBox(right_frame, height=int(root_height * 0.9), width=int(root_width * 0.75))

        # Left Frame info
        self.menu_box = MenuFrame(left_frame, height=int(root_height * 0.7), width=int(root_width // 4))

        self.special_info_box = SpecialInfoBox(left_frame, height=int(root_height * 0.1), width=root_width // 4)

    def update_info_box(frame, height, width):
        # self.info_box = frame(right_frame 
        pass

if __name__ == "__main__":
    monitor = screeninfo.get_monitors()[0]
    app = MainApplication(monitor.width, monitor.height)
    app.mainloop()