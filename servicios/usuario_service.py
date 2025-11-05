from typing import List, Any
from entidades.usuario import Usuario


class UsuarioService:
    """
    Maneja al usuario/dueño y sus dispositivos.
    """

    def registrar_dispositivo(self, usuario: Usuario, dispositivo: Any) -> None:
        usuario.dispositivos.append(dispositivo)
        print(f"[USUARIO] {usuario.nombre} agregó dispositivo: {dispositivo}")

    def listar_dispositivos(self, usuario: Usuario) -> List[Any]:
        print(f"[USUARIO] Dispositivos de {usuario.nombre}:")
        for d in usuario.dispositivos:
            print(f"  - {d}")
        return list(usuario.dispositivos)
