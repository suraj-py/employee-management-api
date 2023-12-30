"""new migrations

Revision ID: e8a91fc4129b
Revises: 47ac76aef815
Create Date: 2023-12-30 12:38:12.149050

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e8a91fc4129b'
down_revision: Union[str, None] = '47ac76aef815'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
