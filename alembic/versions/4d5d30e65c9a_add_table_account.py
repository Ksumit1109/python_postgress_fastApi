"""add table account

Revision ID: 4d5d30e65c9a
Revises: 76251c3c8b00
Create Date: 2025-10-23 12:13:31.635616

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4d5d30e65c9a'
down_revision: Union[str, Sequence[str], None] = '76251c3c8b00'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('account', sa.Column('username',sa.String(),primary_key=True), sa.Column('password',sa.String(30)))


def downgrade() -> None:
   op.drop_table('account')
