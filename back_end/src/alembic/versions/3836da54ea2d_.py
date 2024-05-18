"""empty message

Revision ID: 3836da54ea2d
Revises: 
Create Date: 2024-05-11 22:51:09.224755

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils



# revision identifiers, used by Alembic.
revision: str = '3836da54ea2d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('alimento',
    sa.Column('grupo_alimento', sa.String(length=32), nullable=False),
    sa.PrimaryKeyConstraint('grupo_alimento')
    )
    op.create_table('animal',
    sa.Column('id_animal', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=32), nullable=False),
    sa.PrimaryKeyConstraint('id_animal')
    )
    op.create_table('objetivos',
    sa.Column('id_objetivo', sa.Integer(), nullable=False),
    sa.Column('descricao', sa.String(length=255), nullable=False),
    sa.Column('pontuacao', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id_objetivo')
    )
    op.create_table('usuarios',
    sa.Column('id_usuario', sqlalchemy_utils.types.email.EmailType(length=255), nullable=False),
    sa.Column('nome', sa.String(length=64), nullable=False),
    sa.Column('senha', sa.String(length=128), nullable=False),
    sa.Column('papel', sa.String(length=32), nullable=False),
    sa.Column('id_animal', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_animal'], ['animal.id_animal'], ),
    sa.PrimaryKeyConstraint('id_usuario')
    )

    op.create_table('status',
    sa.Column('id_status', sa.Integer(), nullable=False),
    sa.Column('alimentacao_saudavel', sa.Integer(), nullable=True),
    sa.Column('energia', sa.Integer(), nullable=True),
    sa.Column('forca', sa.Integer(), nullable=True),
    sa.Column('resistencia', sa.Integer(), nullable=True),
    sa.Column('felicidade', sa.Integer(), nullable=True),
    sa.Column('grupo_alimento', sa.String(length=32), nullable=True),
    sa.ForeignKeyConstraint(['grupo_alimento'], ['alimento.grupo_alimento'], ),
    sa.PrimaryKeyConstraint('id_status')
    )
    op.create_table('ObjetivoCompleto',
    sa.Column('id_usuario', sqlalchemy_utils.types.email.EmailType(length=255), nullable=False),
    sa.Column('id_objetivo', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_objetivo'], ['objetivos.id_objetivo'], ),
    sa.ForeignKeyConstraint(['id_usuario'], ['usuarios.id_usuario'], ),
    sa.PrimaryKeyConstraint('id_usuario', 'id_objetivo')
    )
    op.create_table('consumo_Animal',
    sa.Column('id_consumo', sa.Integer(), nullable=False),
    sa.Column('id_usuario', sqlalchemy_utils.types.email.EmailType(length=255), nullable=True),
    sa.Column('grupo_alimento', sa.String(length=32), nullable=True),
    sa.Column('alimento', sa.String(length=64), nullable=True),
    sa.Column('qtd_consumo', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['grupo_alimento'], ['alimento.grupo_alimento'], ),
    sa.ForeignKeyConstraint(['id_usuario'], ['usuarios.id_usuario'], ),
    sa.PrimaryKeyConstraint('id_consumo')
    )
    op.create_table('status_animal',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_status', sa.Integer(), nullable=True),
    sa.Column('id_animal', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['id_animal'], ['animal.id_animal'], ),
    sa.ForeignKeyConstraint(['id_status'], ['status.id_status'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('status_animal')
    op.drop_table('consumo_Animal')
    op.drop_table('ObjetivoCompleto')
    op.drop_table('status')
    op.drop_table('usuarios')
    op.drop_table('objetivos')
    op.drop_table('animal')
    op.drop_table('alimento')
    # ### end Alembic commands ###
