"""empty message

Revision ID: 4c085e7f2c9f
Revises: None
Create Date: 2017-06-02 02:53:19.235835

"""

# revision identifiers, used by Alembic.
revision = '4c085e7f2c9f'
down_revision = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('access_token', sa.String(), nullable=True),
    sa.Column('refresh_token', sa.String(), nullable=True),
    sa.Column('target', sa.Integer(), nullable=True),
    sa.Column('activities', postgresql.ARRAY(sa.String()), nullable=True),
    sa.Column('distances', postgresql.ARRAY(sa.Integer()), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###