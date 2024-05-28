

from typing import List, Dict, Optional

import gzip, json, os
import pandas as pd

from ...tags import USER, ITEM, TIMESTAMP, RATING


INTER_FIELDS = {
    'user_id': USER.name,
    'asin': ITEM.name,
    'rating': RATING.name,
    'timestamp': TIMESTAMP.name,
    'parent_asin': 'parent_asin'
}

ITEM_FIELDS = {
    'parent_asin': 'parent_asin',
    'title': 'title',
    'features': 'features',
    'description': 'description'
}

def open_and_read_json_gz(root, file) -> List:
    data = []
    for line in gzip.open(os.path.join(root, file)):
        data.append(json.loads(line.strip()))
    return data

def extract_from_amazon2023(
    root: str,
    review_file: Optional[str] = None,
    meta_file: Optional[str] = None,
    inter_fields: Dict = INTER_FIELDS,
    item_fields: Dict = ITEM_FIELDS
):
    gz_files =  [file.endswith('gz')  for file in os.listdir(root)]
    if meta_file is None:
        meta_file = next(filter(lambda file: file.startswith('meta'), gz_files))
    if review_file is None:
        review_file = next(filter(lambda file: not file.startswith('meta'), gz_files))

    inter_fields.update(INTER_FIELDS)
    item_fields.update(ITEM_FIELDS)
    raw_inter = open_and_read_json_gz(root, review_file)
    ego_cols, cur_cols = list(inter_fields.keys()), list(inter_fields.values())
    inter_df = pd.DataFrame(
        [[row[key] for key in ego_cols] for row in raw_inter],
        columns=cur_cols
    )

    ego_cols, cur_cols = list(item_fields.keys()), list(item_fields.values())
    raw_meta = {
        row['parent_asin']: [row[key] for key in ego_cols] in item_fields for row in open_and_read_json_gz(root, meta_file)
    }
    uniques = inter_df.groupby(ITEM.name).head(0)
    items, parents = uniques[ITEM.name], uniques['parent_asin']
    raw_item = [
        [item_id] + raw_meta[parent_id] for (item_id, parent_id) in zip(items, parents)
    ]
    item_df = pd.DataFrame(
        raw_item,
        columns=[ITEM.name] + cur_cols
    )

    return inter_df, item_df