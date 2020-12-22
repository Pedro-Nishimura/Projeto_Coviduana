"""vendas table

Revision ID: c7fc1185734e
Revises: 
Create Date: 2020-12-22 01:51:38.217160

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c7fc1185734e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('vendas', sa.Column('codigo', sa.Integer(), autoincrement=True, nullable=False))
    op.alter_column('vendas', 'id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('vendas', 'id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_column('vendas', 'codigo')
    # ### end Alembic commands ###
