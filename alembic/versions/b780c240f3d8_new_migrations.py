"""new migrations

Revision ID: b780c240f3d8
Revises: d3aa0994a0ab
Create Date: 2023-12-30 13:37:17.479403

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b780c240f3d8'
down_revision: Union[str, None] = 'd3aa0994a0ab'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
