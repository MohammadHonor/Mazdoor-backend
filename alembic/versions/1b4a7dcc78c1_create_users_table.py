"""create users table

Revision ID: 1b4a7dcc78c1
Revises: d121da196ffa
Create Date: 2026-10-03 01:31:25.455217

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1b4a7dcc78c1'
down_revision: Union[str, Sequence[str], None] = 'd121da196ffa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
