"""new migrations

Revision ID: 47ac76aef815
Revises: d940a9dad7a6
Create Date: 2023-12-30 12:34:23.984375

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '47ac76aef815'
down_revision: Union[str, None] = 'd940a9dad7a6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
