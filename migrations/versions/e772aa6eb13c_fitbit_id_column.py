"""fitbit id column

Revision ID: e772aa6eb13c
Revises: 99a10178f3c2
Create Date: 2017-06-04 01:02:31.754565

"""

# revision identifiers, used by Alembic.
revision = 'e772aa6eb13c'
down_revision = '99a10178f3c2'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('fitbitid', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'fitbitid')
    # ### end Alembic commands ###
