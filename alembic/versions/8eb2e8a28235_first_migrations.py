"""first migrations

Revision ID: 8eb2e8a28235
Revises: 3e3484c69845
Create Date: 2023-12-30 02:51:30.174797

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8eb2e8a28235'
down_revision: Union[str, None] = '3e3484c69845'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
