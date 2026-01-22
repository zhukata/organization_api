"""seed_test_data

Revision ID: 71f1e47fa066
Revises: 7fb2c4b1def4
Create Date: 2026-01-20 18:51:03.717900

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '71f1e47fa066'
down_revision: Union[str, None] = '7fb2c4b1def4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Insert test data into buildings table
    op.bulk_insert(
        sa.table(
            'buildings',
            sa.column('id', sa.Integer),
            sa.column('address', sa.String),
            sa.column('latitude', sa.Float),
            sa.column('longitude', sa.Float),
        ),
        [
            {'id': 1, 'address': 'ул. Ленина, 1', 'latitude': 55.7558, 'longitude': 37.6173},
            {'id': 2, 'address': 'ул. Пушкина, 2', 'latitude': 55.7559, 'longitude': 37.6174},
        ]
    )
    
    # Insert test data into activities table
    op.bulk_insert(
        sa.table(
            'activities',
            sa.column('id', sa.Integer),
            sa.column('name', sa.String),
            sa.column('parent_id', sa.Integer),
        ),
        [
            {'id': 1, 'name': 'Спорт', 'parent_id': None},
            {'id': 2, 'name': 'Футбол', 'parent_id': 1},
            {'id': 3, 'name': 'Баскетбол', 'parent_id': 1},
            {'id': 4, 'name': 'Образование', 'parent_id': None},
            {'id': 5, 'name': 'Курсы', 'parent_id': 4},
        ]
    )
    
    # Insert test data into organizations table
    op.bulk_insert(
        sa.table(
            'organizations',
            sa.column('id', sa.Integer),
            sa.column('name', sa.String),
            sa.column('building_id', sa.Integer),
        ),
        [
            {'id': 1, 'name': 'Организация 1', 'building_id': 1},
            {'id': 2, 'name': 'Организация 2', 'building_id': 2},
        ]
    )
    
    # Insert test data into organization_activity table
    op.bulk_insert(
        sa.table(
            'organization_activity',
            sa.column('organization_id', sa.Integer),
            sa.column('activity_id', sa.Integer),
        ),
        [
            {'organization_id': 1, 'activity_id': 1},
            {'organization_id': 1, 'activity_id': 2},
            {'organization_id': 2, 'activity_id': 3},
            {'organization_id': 2, 'activity_id': 4},
        ]
    )
    
    # Insert test data into phone_numbers table
    op.bulk_insert(
        sa.table(
            'phone_numbers',
            sa.column('id', sa.Integer),
            sa.column('number', sa.String),
            sa.column('organization_id', sa.Integer),
        ),
        [
            {'id': 1, 'number': '+79991112233', 'organization_id': 1},
            {'id': 2, 'number': '+79992223344', 'organization_id': 1},
            {'id': 3, 'number': '+79993334455', 'organization_id': 2},
        ]
    )


def downgrade() -> None:
    # Remove all test data
    op.execute('DELETE FROM phone_numbers')
    op.execute('DELETE FROM organization_activity')
    op.execute('DELETE FROM organizations')
    op.execute('DELETE FROM activities')
    op.execute('DELETE FROM buildings')
