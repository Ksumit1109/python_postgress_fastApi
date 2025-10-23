"""add column password

Revision ID: 76251c3c8b00
Revises: 
Create Date: 2025-10-23 10:52:02.086830

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '76251c3c8b00'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
   op.add_column('user', sa.Column('password', sa.String(30)))


def downgrade() -> None:
    """Downgrade schema."""
    pass
