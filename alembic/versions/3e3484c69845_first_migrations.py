"""first migrations

Revision ID: 3e3484c69845
Revises: e4ba6d374c96
Create Date: 2023-12-30 02:44:06.198308

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3e3484c69845'
down_revision: Union[str, None] = 'e4ba6d374c96'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
