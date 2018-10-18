"""Add a column

Revision ID: 36253d22ac4c
Revises: 079d77e428e5
Create Date: 2018-10-16 14:28:30.668695

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '36253d22ac4c'
down_revision = '079d77e428e5'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('account', sa.Column('last_transaction_date', sa.DateTime))
    pass


def downgrade():
    op.drop_column('account', 'last_transaction_date')
    pass
