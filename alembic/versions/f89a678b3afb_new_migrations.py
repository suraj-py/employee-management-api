"""new migrations

Revision ID: f89a678b3afb
Revises: 866196f73203
Create Date: 2023-12-30 12:41:39.779362

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f89a678b3afb'
down_revision: Union[str, None] = '866196f73203'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
