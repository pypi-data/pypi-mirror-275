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
    
    def test_kql_database(self):

        fc = self.fc
        workspace_id = 'd8a5abe0-9eed-406d-ab46-343bc57ddbe5'
        evenhouse_id = "14822d45-5460-4efa-9b30-8628510a9197"

        creation_payload = {"databaseType" : "ReadWrite",
                            "parentEventhouseItemId" : evenhouse_id}

        datetime_str = datetime.now().strftime("%Y%m%d%H%M%S")
        kqldb_name = "kql" + datetime_str
        kqldb = fc.create_kql_database(workspace_id = workspace_id, display_name=kqldb_name,
                                    creation_payload=creation_payload)
        self.assertEqual(kqldb.display_name, kqldb_name)

        kql_databases = fc.list_kql_databases(workspace_id)
        kql_database_names = [kqldb.display_name for kqldb in kql_databases]
        self.assertGreater(len(kql_databases), 0)
        self.assertIn(kqldb_name, kql_database_names)

        kqldb = fc.get_kql_database(workspace_id, kql_database_name=kqldb_name)
        self.assertIsNotNone(kqldb.id)
        self.assertEqual(kqldb.display_name, kqldb_name)
        
        new_name = kqldb_name+"2"
        kqldb2 = fc.update_kql_database(workspace_id, kqldb.id, display_name=new_name)

        kqldb = fc.get_kql_database(workspace_id, kql_database_id=kqldb.id)
        self.assertEqual(kqldb.display_name, new_name)
        self.assertEqual(kqldb.id, kqldb2.id)
        
        status_code = fc.delete_kql_database(workspace_id, kqldb.id)
        self.assertEqual(status_code, 200)