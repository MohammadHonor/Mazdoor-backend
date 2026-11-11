"""sub_profession updated

Revision ID: bdc199d0dbfc
Revises: f5cc19651f4f
Create Date: 2026-11-11 00:09:16.197928

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bdc199d0dbfc'
down_revision: Union[str, Sequence[str], None] = 'f5cc19651f4f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
