from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def render(self) -> str:
        pass

    def on_click(self) -> str:
        return "Button clicked!"
    

class Dialog(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass
    
    def render_dialog(self) -> str:
        button = self.create_button()
        return f"{button.render()}\n{button.on_click()}"


class WindowsButton(Button):
    def render(self) -> str:
        return "Rendering botón windows."
    
class HTMLButton(Button):
    def render(self) -> str:
        return "Rendering botón HTML."
    

class WindowsDialog(Dialog):
    def create_button(self) -> Button:
        return WindowsButton()
    
class HTMLDialog(Dialog):
    def create_button(self) -> Button:
        return HTMLButton()

class Application:
    def __init__(self, OS: str):
        if OS == "Windows":
            self.dialog = WindowsDialog()
        elif OS == "HTML":
            self.dialog = HTMLDialog()
        else:
            raise ValueError(f"Tipo de OS desconocido: {OS}")

    def main(self) -> str:
        print("Aplicacion: Desplegado con dialogo tipo:", type(self.dialog).__name__)
        return self.dialog.render_dialog()

if __name__ == "__main__":
    app = Application("Windows")
    print(app.main())

    print("-" * 50)

    app = Application("HTML")
    print(app.main())
