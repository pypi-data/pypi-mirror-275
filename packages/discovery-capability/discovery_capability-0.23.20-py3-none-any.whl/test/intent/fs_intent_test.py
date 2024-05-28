import unittest
import os
from pathlib import Path
import shutil
import ast
from datetime import datetime
from pprint import pprint

import pandas as pd
import pyarrow as pa
import pyarrow.compute as pc
import pyarrow.parquet as pq

from ds_capability import FeatureEngineer, FeatureSelect
from ds_capability.components.commons import Commons
from ds_core.properties.property_manager import PropertyManager
from ds_capability.intent.feature_select_intent import FeatureSelectIntent

# Pandas setup
pd.set_option('max_colwidth', 320)
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 99)
pd.set_option('expand_frame_repr', True)


class FeatureEngineererTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        # clean out any old environments
        for key in os.environ.keys():
            if key.startswith('HADRON'):
                del os.environ[key]
        # Local Domain Contract
        os.environ['HADRON_PM_PATH'] = os.path.join('working', 'contracts')
        os.environ['HADRON_PM_TYPE'] = 'json'
        # Local Connectivity
        os.environ['HADRON_DEFAULT_PATH'] = Path('working/data').as_posix()
        # Specialist Component
        try:
            os.makedirs(os.environ['HADRON_PM_PATH'])
        except OSError:
            pass
        try:
            os.makedirs(os.environ['HADRON_DEFAULT_PATH'])
        except OSError:
            pass
        try:
            shutil.copytree('../_test_data', os.path.join(os.environ['PWD'], 'working/source'))
        except OSError:
            pass
        PropertyManager._remove_all()

    def tearDown(self):
        try:
            shutil.rmtree('working')
        except OSError:
            pass

    def test_auto_clean_headers(self):
        tbl = FeatureEngineer.from_memory().tools.get_synthetic_data_types(1000, extend=False)
        fs = FeatureSelect.from_memory()
        tools: FeatureSelectIntent = fs.tools
        result = tools.auto_clean_header(tbl, rename_map={'num': 'float'})
        self.assertEqual(['id', 'cat', 'float', 'int', 'bool', 'date', 'string'], result.column_names)
        result = tools.auto_clean_header(tbl, rename_map=['cid', 'category', 'float', 'integer', 'boolean', 'date', 'str'])
        self.assertEqual(['cid', 'category', 'float', 'integer', 'boolean', 'date', 'str'], result.column_names)


    def test_auto_drop_noise(self):
        tbl = FeatureEngineer.from_memory().tools.get_synthetic_data_types(1000, extend=True)
        fs = FeatureSelect.from_memory()
        tools: FeatureSelectIntent = fs.tools
        self.assertEqual(17, tbl.num_columns)
        result = tools.auto_drop_noise(tbl)
        self.assertEqual(14, result.num_columns)
        self.assertCountEqual(['one_string', 'nest_list', 'nulls'], Commons.list_diff(tbl.column_names, result.column_names))

    def test_auto_drop_columns(self):
        tbl = FeatureEngineer.from_memory().tools.get_synthetic_data_types(1000)
        fs = FeatureSelect.from_memory()
        tools: FeatureSelectIntent = fs.tools
        result = tools.auto_drop_columns(tbl, headers=['num', 'int'])
        self.assertCountEqual(['date', 'bool', 'string', 'cat', 'id'], result.column_names)

    def test_auto_drop_correlated(self):
        tbl = FeatureEngineer.from_memory().tools.get_synthetic_data_types(1000, extend=True)
        fs = FeatureSelect.from_memory()
        tools: FeatureSelectIntent = fs.tools
        self.assertEqual(19, tbl.num_columns)
        self.assertIn('dup_num', tbl.column_names)
        result = tools.auto_drop_correlated(tbl)
        self.assertEqual(18, result.num_columns)
        self.assertNotIn('dup_num', result.column_names)

    def test_aggrigate(self):
        tbl = FeatureEngineer.from_memory().tools.get_synthetic_data_types(5, extend=False)
        fs = FeatureSelect.from_memory()
        tools: FeatureSelectIntent = fs.tools
        result = tools.auto_aggregate(tbl, action='count', regex=['cat', 'string'], to_header='agg', drop_aggregated=True)
        # print(result.column('agg').to_pylist())
        # print(result.column_names)
        self.assertEqual([2, 2, 2, 2, 2], result.column('agg').to_pylist())
        self.assertEqual(['num', 'int', 'bool', 'date', 'agg'], result.column_names)

    def test_auto_projection(self):
        tbl = FeatureEngineer.from_memory().tools.get_noise(size=1000, num_columns=5)
        fs = FeatureSelect.from_memory()
        tools: FeatureSelectIntent = fs.tools
        result = tools.auto_projection(tbl, n_components=2)
        control = ['pca_A', 'pca_B']
        self.assertEqual(control, result.column_names)
        self.assertEqual((1000, 2), result.shape)

    def test_auto_append_tables(self):
        tbl = FeatureEngineer.from_memory().tools.get_noise(size=1000, num_columns=5)
        fs = FeatureSelect.from_memory()
        tools: FeatureSelectIntent = fs.tools
        result = tools.auto_append_tables(tbl, None)
        self.assertTrue(tbl.equals(result))
        result = tools.auto_append_tables(tbl, tbl)
        self.assertTrue(tbl.equals(result))
        tbl_types = FeatureEngineer.from_memory().tools.get_synthetic_data_types(1200)
        result = tools.auto_append_tables(tbl, tbl_types, headers=['A', 'B', 'C'], other_headers=['num', 'int'])
        self.assertEqual((1000, 5), result.shape)
        self.assertCountEqual(['A', 'B', 'C', 'num', 'int'], result.column_names)
        tbl_types = FeatureEngineer.from_memory().tools.get_synthetic_data_types(400)
        result = tools.auto_append_tables(tbl, tbl_types, headers=['A', 'B', 'C'], other_headers=['num', 'int'])
        self.assertEqual((1000, 5), result.shape)
        self.assertCountEqual(['A', 'B', 'C', 'num', 'int'], result.column_names)

    def test_raise(self):
        startTime = datetime.now()
        with self.assertRaises(KeyError) as context:
            env = os.environ['NoEnvValueTest']
        self.assertTrue("'NoEnvValueTest'" in str(context.exception))
        print(f"Duration - {str(datetime.now() - startTime)}")


def get_table():
    num = pa.array([1.0, None, 5.0, -0.46421, 3.5, 7.233, -2], pa.float64())
    val = pa.array([1, 2, 3, 4, 5, 6, 7], pa.int64())
    date = pc.strptime(["2023-01-02 04:49:06", "2023-01-02 04:57:12", None, None, "2023-01-02 05:23:50", None, None],
                       format='%Y-%m-%d %H:%M:%S', unit='ns')
    text = pa.array(["Blue", "Green", None, 'Red', 'Orange', 'Yellow', 'Pink'], pa.string())
    binary = pa.array([True, True, None, False, False, True, False], pa.bool_())
    cat = pa.array([None, 'M', 'F', 'M', 'F', 'M', 'M'], pa.string()).dictionary_encode()
    return pa.table([num, val, date, text, binary, cat], names=['num', 'int', 'date', 'text', 'bool', 'cat'])


def pm_view(capability: str, task: str, section: str = None):
    uri = os.path.join(os.environ['HADRON_PM_PATH'], f"hadron_pm_{capability}_{task}.parquet")
    tbl = pq.read_table(uri)
    tbl = tbl.column(0).combine_chunks()
    result = ast.literal_eval(tbl.to_pylist()[0]).get(capability, {}).get(task, {})
    return result.get(section, {}) if isinstance(section, str) and section in result.keys() else result


if __name__ == '__main__':
    unittest.main()
