from bot.database.main import engine, Base


def register_models() -> None:
    Base.metadata.create_all(engine)


