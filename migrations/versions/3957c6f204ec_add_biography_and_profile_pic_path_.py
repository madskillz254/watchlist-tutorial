"""add biography and profile pic path column to users table

Revision ID: 3957c6f204ec
Revises: d7d860ea02be
Create Date: 2019-04-17 01:59:28.054900

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3957c6f204ec'
down_revision = 'd7d860ea02be'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('bio', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('profile_pic_path', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'profile_pic_path')
    op.drop_column('users', 'bio')
    # ### end Alembic commands ###
