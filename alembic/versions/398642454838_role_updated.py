"""role updated

Revision ID: 398642454838
Revises: 1b4a7dcc78c1
Create Date: 2026-10-17 21:37:40.269235

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '398642454838'
down_revision: Union[str, Sequence[str], None] = '1b4a7dcc78c1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
