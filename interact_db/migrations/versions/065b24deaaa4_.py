"""empty message

Revision ID: 065b24deaaa4
Revises: 
Create Date: 2017-05-21 01:10:59.595956

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '065b24deaaa4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('User',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('linkedin_url', sa.String(length=120), nullable=False),
    sa.Column('color', sa.String(length=120), nullable=True),
    sa.Column('phone_number', sa.String(length=20), nullable=True),
    sa.Column('title', sa.String(length=250), nullable=False),
    sa.Column('image_url', sa.String(length=250), nullable=False),
    sa.Column('access_token', sa.String(length=2500), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('access_token'),
    sa.UniqueConstraint('color'),
    sa.UniqueConstraint('linkedin_url'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('phone_number')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('User')
    # ### end Alembic commands ###
