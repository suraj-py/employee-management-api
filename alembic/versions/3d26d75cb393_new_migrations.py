"""new migrations

Revision ID: 3d26d75cb393
Revises: f89a678b3afb
Create Date: 2023-12-30 12:42:20.970678

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3d26d75cb393'
down_revision: Union[str, None] = 'f89a678b3afb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
