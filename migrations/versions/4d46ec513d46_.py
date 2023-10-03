"""empty message

Revision ID: 4d46ec513d46
Revises: 
Create Date: 2023-10-03 19:54:12.128142

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4d46ec513d46'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome_completo', sa.String(length=200), nullable=True),
    sa.Column('idade', sa.Integer(), nullable=True),
    sa.Column('sexo', sa.String(length=9), nullable=True),
    sa.Column('cpf', sa.String(length=11), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cpf')
    )
    op.create_table('variantes',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('cromossomo', sa.String(length=2), nullable=True),
    sa.Column('posicao', sa.Integer(), nullable=True),
    sa.Column('base_ref', sa.String(length=1), nullable=True),
    sa.Column('base_alt', sa.String(length=1), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('variantes')
    op.drop_table('users')
    # ### end Alembic commands ###