"""token expiry field

Revision ID: 99a10178f3c2
Revises: ca17e014a0bf
Create Date: 2017-06-03 14:14:36.779803

"""

# revision identifiers, used by Alembic.
revision = '99a10178f3c2'
down_revision = 'ca17e014a0bf'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('token_expires_at', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'token_expires_at')
    # ### end Alembic commands ###
