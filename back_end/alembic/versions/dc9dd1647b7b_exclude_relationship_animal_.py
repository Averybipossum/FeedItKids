"""exclude relationship Animal ConsumoAnimal

Revision ID: dc9dd1647b7b
Revises: 0218dbae3496
Create Date: 2024-05-30 22:08:12.647693

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dc9dd1647b7b'
down_revision: Union[str, None] = '0218dbae3496'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('consumo_animal_id_animal_key', 'consumo_animal', type_='unique')
    op.drop_constraint('consumo_animal_id_animal_fkey', 'consumo_animal', type_='foreignkey')
    op.drop_column('consumo_animal', 'id_animal')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('consumo_animal', sa.Column('id_animal', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('consumo_animal_id_animal_fkey', 'consumo_animal', 'animal', ['id_animal'], ['id_animal'])
    op.create_unique_constraint('consumo_animal_id_animal_key', 'consumo_animal', ['id_animal'])
    # ### end Alembic commands ###
