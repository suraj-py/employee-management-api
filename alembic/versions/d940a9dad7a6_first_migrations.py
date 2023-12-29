"""first migrations

Revision ID: d940a9dad7a6
Revises: 8eb2e8a28235
Create Date: 2023-12-30 02:52:04.729075

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd940a9dad7a6'
down_revision: Union[str, None] = '8eb2e8a28235'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
