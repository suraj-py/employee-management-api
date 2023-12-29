"""first migrations

Revision ID: e4ba6d374c96
Revises: 563eba7a47a3
Create Date: 2023-12-30 02:40:43.832330

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e4ba6d374c96'
down_revision: Union[str, None] = '563eba7a47a3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
