"""empty message

Revision ID: ea73b620f964
Revises: 00bdbc4b430c
Create Date: 2017-11-19 23:58:59.093235

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea73b620f964'
down_revision = '00bdbc4b430c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('transport_lines',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('transport_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['transport_id'], ['transports.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transport_lines')
    # ### end Alembic commands ###
