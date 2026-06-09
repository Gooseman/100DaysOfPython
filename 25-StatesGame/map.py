import tkinter as tk


class Map:
    BG_IMAGE = "blank_states_img.gif"

    def __init__(self, canvas):
        """Use the provided tkinter Canvas for the map background and drawing.
        Determine the map size from the background image.
        """
        self.canvas = canvas
        self._set_bg_image(self.BG_IMAGE)

    def _set_bg_image(self, image_path):
        """Set the background image to the provided file path and update dimensions."""
        # Load background image via Tk so we can get its dimensions and draw it
        try:
            self._bg_image = tk.PhotoImage(master=self.canvas, file=image_path)
            self.width = self._bg_image.width()
            self.height = self._bg_image.height()

            # resize canvas to image size and draw the image as background
            self.canvas.config(width=self.width, height=self.height)
            self.canvas.create_image(0, 0, image=self._bg_image, anchor="nw")
        except Exception as e:
            print(f"Error loading background image: {e}")

    def display_state(self, state_name, x, y):
        # Draw the state name onto the tkinter canvas. Coordinates are canvas pixels.
        self.canvas.create_text(
            x, y, text=state_name, font=("Arial", 10), anchor="center"
        )
    
    def clear(self):
        """Clear all state names from the canvas, leaving only the background image."""
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, image=self._bg_image, anchor="nw")
