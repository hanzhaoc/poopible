"""create user prefered poopable table

Revision ID: 71c5d4958297
Revises: 4b773595b1bb
Create Date: 2020-02-22 00:22:08.363427

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '71c5d4958297'
down_revision = '4b773595b1bb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users_prefered_poopables',
    sa.Column('slack_user_id', sa.String(length=9), nullable=False),
    sa.Column('poopable_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['poopable_id'], ['poopable.id'], ),
    sa.ForeignKeyConstraint(['slack_user_id'], ['user.slack_user_id'], ),
    sa.PrimaryKeyConstraint('slack_user_id', 'poopable_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users_prefered_poopables')
    # ### end Alembic commands ###
