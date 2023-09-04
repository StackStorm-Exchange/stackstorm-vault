from read_kv import VaultReadKVAction
from tests.vault_action_tests_base import VaultActionTestCase


class ReadKVActionTestCase(VaultActionTestCase):
    action_cls = VaultReadKVAction

    secret_v1 = True
    secret_v2 = True

    def test_read_kv1(self):
        mount_point = "kvv1"

        # setup
        self.client.kv.v1.create_or_update_secret(
            path="stanley",
            secret={"st2": "awesome"},
            mount_point=mount_point,
        )

        # test
        action = self.get_action_instance(config=self.dummy_pack_config)
        _, result = action.run(
            path="stanley",
            kv_version=1,
            mount_point=mount_point,
            version="1",
        )
        self.assertEqual(result["data"]["st2"], "awesome")

        # cleanup
        self.client.kv.v1.delete_secret(
            path="stanley",
            mount_point=mount_point,
        )

    def test_read_kv2(self):
        mount_point = "kvv2"

        # setup
        self.client.kv.v2.create_or_update_secret(
            path="stanley",
            secret={"st2": "awesome"},
            mount_point=mount_point,
        )

        # test
        action = self.get_action_instance(config=self.dummy_pack_config)
        _, result = action.run(
            path="stanley",
            kv_version=2,
            mount_point=mount_point,
            version="1",
        )
        # v2 puts the secret one level deeper than v1
        self.assertEqual(result["data"]["data"]["st2"], "awesome")

        # cleanup
        self.client.kv.v2.delete_metadata_and_all_versions(
            path="stanley",
            mount_point=mount_point,
        )
