from rutas_y_sabores.database import PKModel

class Categoria(PKModel):
    __tablename__ = "categorias"
    nombre = Column(db.String(100), nullable=False, unique=True)
    descripcion= Column(db.String(250), nullable=False)

    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"