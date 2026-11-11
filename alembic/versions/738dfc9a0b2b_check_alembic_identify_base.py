"""check alembic identify base

Revision ID: 738dfc9a0b2b
Revises: 398642454838
Create Date: 2026-10-17 21:47:03.380309

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '738dfc9a0b2b'
down_revision: Union[str, Sequence[str], None] = '398642454838'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
