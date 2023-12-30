"""new migrations

Revision ID: d3aa0994a0ab
Revises: 3d26d75cb393
Create Date: 2023-12-30 13:22:39.242990

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd3aa0994a0ab'
down_revision: Union[str, None] = '3d26d75cb393'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
