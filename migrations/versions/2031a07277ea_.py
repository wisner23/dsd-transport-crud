"""empty message

Revision ID: 2031a07277ea
Revises: ea73b620f964
Create Date: 2017-11-20 00:36:05.257750

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2031a07277ea'
down_revision = 'ea73b620f964'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('transport_lines', sa.Column('hour', sa.String(length=50), nullable=True))
    op.add_column('transport_lines', sa.Column('passed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('transport_lines', 'passed')
    op.drop_column('transport_lines', 'hour')
    # ### end Alembic commands ###
