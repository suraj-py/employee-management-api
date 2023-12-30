"""new migrations

Revision ID: 866196f73203
Revises: e8a91fc4129b
Create Date: 2023-12-30 12:38:34.112667

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '866196f73203'
down_revision: Union[str, None] = 'e8a91fc4129b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
