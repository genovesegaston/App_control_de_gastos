from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


DATABASE_URL = "sqlite:///./db/control_gastos.db"


engine = create_engine(
    DATABASE_URL,
    echo=True,  # imprime en consola las queries (útil en desarrollo)
    future=True,  # habilita comportamiento estilo SQLAlchemy 2.0
    # pool_pre_ping=True,  # evita errores por conexiones "muertas" (recomendado para MySQL)
    connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

session = SessionLocal()

Base = declarative_base()

Base.metadata.create_all(engine)
