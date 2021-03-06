"""empty message

Revision ID: 012f6d60ecde
Revises: 
Create Date: 2019-11-25 20:02:21.257159

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '012f6d60ecde'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ratings',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('place', sa.String(length=32), nullable=True),
    sa.Column('rating', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=32), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=False),
    sa.Column('city', sa.String(length=32), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('state', sa.String(length=32), nullable=True),
    sa.Column('occupation', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('ratings')
    # ### end Alembic commands ###
