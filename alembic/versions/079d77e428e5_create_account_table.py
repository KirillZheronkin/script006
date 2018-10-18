"""create account table

Revision ID: 079d77e428e5
Revises: 
Create Date: 2018-10-16 14:25:16.442437

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '079d77e428e5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'account',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('description', sa.Unicode(200)),
    )
    return


def downgrade():
    op.drop_table('account')
    return
