import os
import pickle
from excepciones.domotica_excepcion import ErrorPersistenciaException

class RegistroDomoticoService:

    def persistir(self, usuario_nombre, estado):
        try:
            os.makedirs("data", exist_ok=True)
            path = f"data/{usuario_nombre}.dat"
            with open(path, "wb") as f:
                pickle.dump(estado, f)
            print(f"[PERSISTENCIA] Estado domótico guardado en {path}")
        except Exception as e:
            raise ErrorPersistenciaException("escritura", str(e))
