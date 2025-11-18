"""
ARCHIVO GENERADO POR GEMINI CLI.

Ejemplo del Patrón de Diseño Método de Fábrica (Factory Method)
"""

from abc import ABC, abstractmethod

# 1. Interfaz del Producto (Product)
# Define la interfaz común para todos los transportes.
class Transporte(ABC):
    """
    La interfaz de Transporte declara las operaciones que todos los productos
    concretos (tipos de transporte) deben implementar.
    """
    @abstractmethod
    def entregar(self) -> str:
        pass

# 2. Productos Concretos (Concrete Products)
# Implementaciones de la interfaz Transporte.
class Camion(Transporte):
    """
    El Camión es una implementación de un producto concreto.
    """
    def entregar(self) -> str:
        return "Entrega por tierra en un camión."

class Barco(Transporte):
    """
    El Barco es otra implementación de un producto concreto.
    """
    def entregar(self) -> str:
        return "Entrega por mar en un barco."
    
class Avion(Transporte):
    """
    El Avión es otra implementación de un producto concreto.
    """
    def entregar(self) -> str:
        return "Entrega por cielo en un avión."

# 3. Creador (Creator)
# Declara el método de fábrica que devuelve un objeto de tipo Transporte.
class Logistica(ABC):
    """
    La clase Creador declara el método de fábrica que debe devolver un
    objeto de la clase Transporte. Las subclases de Logistica suelen
    proporcionar la implementación de este método.
    """
    @abstractmethod
    def crear_transporte(self) -> Transporte:
        """
        Este es el "método de fábrica" (factory method).
        """
        pass

    def planificar_entrega(self) -> str:
        """
        El código principal del Creador no depende de los productos concretos, 
        sino que funciona a través de la interfaz.
        """
        # Llama al método de fábrica para crear un objeto Producto.
        transporte = self.crear_transporte()

        # Ahora, usa el producto.
        resultado = f"Logística: El transporte dice '{transporte.entregar()}'"
        return resultado

# 4. Creadores Concretos (Concrete Creators)
# Implementan el método de fábrica para crear productos concretos.
class LogisticaTerrestre(Logistica):
    """
    Este Creador Concreto anula el método de fábrica para devolver una
    instancia de Camion.
    """
    def crear_transporte(self) -> Transporte:
        return Camion()

class LogisticaMaritima(Logistica):
    """
    Este Creador Concreto anula el método de fábrica para devolver una
    instancia de Barco.
    """
    def crear_transporte(self) -> Transporte:
        return Barco()

class LogisticaAerea(Logistica):
    """
    Este Creador Concreto anula el método de fábrica para devolver una
    instancia de Avion.
    """
    def crear_transporte(self) -> Transporte:
        return Avion()

# --- Código Cliente ---
def cliente(creador: Logistica):
    """
    El código cliente funciona con una instancia de un creador concreto, 
    aunque a través de su interfaz base. Mientras el cliente siga 
    trabajando con el creador a través de la interfaz base, puedes
    pasarle cualquier subclase de creador.
    """
    print(f"Cliente: No conozco el tipo de creador, pero funciona.\n"
          f"{creador.planificar_entrega()}", end="\n\n")


if __name__ == "__main__":
    print("Lanzando la aplicación con Logística Terrestre.")
    cliente(LogisticaTerrestre())

    print("Lanzando la aplicación con Logística Marítima.")
    cliente(LogisticaMaritima())

    print("Lanzando la aplicación con Logística Aérea.")
    cliente(LogisticaAerea())
