"""initialized again

Revision ID: f5cc19651f4f
Revises: 738dfc9a0b2b
Create Date: 2026-10-17 22:07:42.474355

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f5cc19651f4f'
down_revision: Union[str, Sequence[str], None] = '738dfc9a0b2b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
