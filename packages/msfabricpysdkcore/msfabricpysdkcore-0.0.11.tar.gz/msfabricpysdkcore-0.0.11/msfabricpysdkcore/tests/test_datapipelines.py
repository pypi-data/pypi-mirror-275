import unittest
from datetime import datetime
from dotenv import load_dotenv
from time import sleep
from msfabricpysdkcore.coreapi import FabricClientCore

load_dotenv()

class TestFabricClientCore(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestFabricClientCore, self).__init__(*args, **kwargs)
        #load_dotenv()
        self.fc = FabricClientCore()

    def test_data_pipelines(self):

        fc = self.fc
        workspace_id = 'd8a5abe0-9eed-406d-ab46-343bc57ddbe5'
        
        dps = fc.list_data_pipelines(workspace_id)
        dp_names = [dp.display_name for dp in dps]
        self.assertGreater(len(dps), 0)
        self.assertIn("pipeline1", dp_names)

        dp = fc.get_data_pipeline(workspace_id, data_pipeline_name="pipeline1")
        self.assertIsNotNone(dp.id)
        self.assertIsNotNone(dp.definition)
        self.assertEqual(dp.display_name, "pipeline1")

        dp_new = fc.create_data_pipeline(workspace_id, display_name="pipeline_new", description="asda")
        dp_new.update_definition(dp.definition)
        
        self.assertEqual(dp_new.display_name, "pipeline_new")

        dp2 = fc.update_data_pipeline(workspace_id, dp.id, display_name="pipeline2")

        dp = fc.get_data_pipeline(workspace_id, data_pipeline_id=dp.id)
        self.assertEqual(dp.display_name, "pipeline2")
        self.assertEqual(dp.id, dp2.id)

        dp2 = fc.update_data_pipeline(workspace_id, dp.id, display_name="pipeline1")

        dp = fc.get_data_pipeline(workspace_id, data_pipeline_id=dp.id)
        self.assertEqual(dp.display_name, "pipeline1")
        self.assertEqual(dp.id, dp2.id)
        status_code = fc.delete_data_pipeline(workspace_id, dp_new.id)
        self.assertEqual(status_code, 200)