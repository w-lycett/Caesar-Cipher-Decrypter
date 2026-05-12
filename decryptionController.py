# Import model and view
from decryptionModel import CaesarModel
from decryptionView import CaesarView
# Import tkinter to initialise + connect crack button to method
import tkinter as tk

class CaesarController:
    # Constructor method
    def __init__(self, root):
        self.model = CaesarModel()
        self.view = CaesarView(root)

        # Connects button to method
        self.view.button.config(command = self.run)

    # Runs the decryption process when the button is clicked
    def run(self):
        ciphertext = self.view.get_ciphertext()
        if len(ciphertext) == 0:
            self.view.display_result("N/A", "Please enter some text to decrypt.")
            return
        else:
            shift, plaintext = self.model.crack_cipher(ciphertext)
            self.view.display_result(shift, plaintext)

# Starts application
if __name__ == "__main__":
    root = tk.Tk()
    app = CaesarController(root)
    root.mainloop()