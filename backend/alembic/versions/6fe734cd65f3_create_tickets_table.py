"""create tickets table

Revision ID: 6fe734cd65f3
Revises: 
Create Date: 2025-07-24 18:50:29.998717

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6fe734cd65f3'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'tickets',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('description', sa.String),
        sa.Column('price', sa.Float),
        sa.Column('date', sa.Date),
        sa.Column('location', sa.String),
    )


def downgrade() -> None:
    op.drop_table('tickets')
