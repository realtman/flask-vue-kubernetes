from flask.cli import FlaskGroup

from project import create_app, db
from project.api.models import SupplyModel


app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command('seed_db')
def seed_db():
    """Seeds the database."""
    db.session.add(SupplyModel(
        label = "test",
        starting_inventory = 170,
        price = 775,
        shortage = 1200,
        salvage = 21,
        production_na = 4000,
        processing_na = 53,
        production_sa = 4000,
        processing_sa = 67,
        # yield_prob_na = [],
        yield_na = [],
        # yield_prob_sa = [],
        yield_sa = [],
        # demand_prob = [],
        demand = []
    ))
    db.session.commit()


if __name__ == '__main__':
    cli()
