"""empty message

Revision ID: 204d3ffd0d2d
Revises: 8e59d4e1103a
Create Date: 2024-07-13 20:19:23.690792

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '204d3ffd0d2d'
down_revision = '8e59d4e1103a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tasks', schema=None) as batch_op:
        batch_op.add_column(sa.Column('title', sa.String(length=225), nullable=False))
        batch_op.drop_column('name')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tasks', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.VARCHAR(length=225), nullable=False))
        batch_op.drop_column('title')

    # ### end Alembic commands ###
