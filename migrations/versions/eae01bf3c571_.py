"""empty message

Revision ID: eae01bf3c571
Revises: 
Create Date: 2023-06-12 19:52:17.191555

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eae01bf3c571'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('facts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('submitter', sa.String(length=250), nullable=True),
    sa.Column('fact', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('facts')
    # ### end Alembic commands ###
