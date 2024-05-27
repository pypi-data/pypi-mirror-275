"""Tests for the keyraser client"""

import base64
import io
import os.path
import pathlib
import shutil
import subprocess
import tempfile
import unittest

from testcontainers.core.container import DockerContainer
from testcontainers.core.waiting_utils import wait_for_logs

from keyraser_client import Client, NdjsonFormat, IdFormat

data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'test-data')
keystore_credential_file = pathlib.Path(os.path.join(data_dir, 'keystore.kred'))
keystore_credential_value = base64.b64encode(keystore_credential_file.read_bytes())

client_credential_file = pathlib.Path(os.path.join(data_dir, 'client.kred'))
client_credential_value = base64.b64encode(keystore_credential_file.read_bytes())


class TestClient(unittest.TestCase):

    def setUp(self) -> None:
        self.temp_dir = tempfile.mkdtemp()
        self.container = DockerContainer(
            'public.ecr.aws/kantai/keyraser-keystore:latest'
        )
        self.container.with_command(['-address', ':1996'])
        self.container.with_exposed_ports(1996)
        self.container.with_volume_mapping(self.temp_dir, '/keys', 'rw')

        self.container.with_env('KR_CREDENTIAL', keystore_credential_value)
        self.container.start()
        self.address = (
            self.container.get_container_host_ip()
            + ':'
            + self.container.get_exposed_port(1996)
        )
        wait_for_logs(self.container, 'Restore complete')

    def tearDown(self) -> None:
        self.container.stop()
        shutil.rmtree(self.temp_dir)

    def test_encrypt_static_ndjson_file_with_custom_id_property(self):
        client = Client(
            keystore_address=self.address, credential_path=client_credential_file
        )

        src = pathlib.Path(os.path.join(data_dir, 'custom-id.ndjson'))
        dest = pathlib.Path(tempfile.mktemp())
        client.encrypt(NdjsonFormat(id_property='user_id'), src, dest)
        # self.assertEqual(True, False)  # add assertion here

    def test_encrypt_static_ndjson_file_with_default_id_property(self):
        client = Client(
            keystore_address=self.address, credential_path=client_credential_file
        )

        src = pathlib.Path(os.path.join(data_dir, 'default-id.ndjson'))
        dest = pathlib.Path(tempfile.mktemp())
        client.encrypt(NdjsonFormat(), src, dest)

        self.assertEqual(1124, len(dest.read_bytes()))

    def test_encrypt_static_ndjson_file_with_str_paths(self):
        client = Client(
            keystore_address=self.address, credential_path=client_credential_file
        )

        src = os.path.join(data_dir, 'default-id.ndjson')
        dest = tempfile.mktemp()
        client.encrypt(NdjsonFormat(), src, dest)

        self.assertEqual(1124, len(pathlib.Path(dest).read_bytes()))

    def test_encrypt_ndjson_from_stream(self):
        client = Client(
            keystore_address=self.address, credential_path=client_credential_file
        )

        src = io.BytesIO(
            b'''{"id": "abcdef01", "property": "value-1"}
{"id": "abcdef02", "property": "value-2"}
{"id": "abcdef03", "property": "value-3"}
{"id": "abcdef04", "property": "value-4"}
{"id": "abcdef05", "property": "value-5"}
{"id": "abcdef06", "property": "value-6"}
{"id": "abcdef07", "property": "value-7"}
{"id": "abcdef08", "property": "value-8"}
{"id": "abcdef09", "property": "value-9"}
{"id": "abcdef0a", "property": "value-10"}
'''
        )
        dest = pathlib.Path(tempfile.mktemp())
        client.encrypt(NdjsonFormat(), src, dest)

        self.assertEqual(1124, len(dest.read_bytes()))

    def test_encrypt_and_decrypt_ndjson_to_stream(self):
        client = Client(
            keystore_address=self.address, credential_path=client_credential_file
        )

        src = pathlib.Path(os.path.join(data_dir, 'default-id.ndjson'))
        enc_dest = io.BytesIO()
        client.encrypt(NdjsonFormat(), src, enc_dest)
        self.assertEqual(1124, len(enc_dest.getvalue()))

        enc_dest.seek(0)

        dec_dest = io.BytesIO()
        client.decrypt(enc_dest, dec_dest)

        self.assertEqual(src.read_bytes(), dec_dest.getvalue())

    def test_decrypt_static_ndjson_file_with_custom_id_property(self):
        client = Client(
            keystore_address=self.address, credential_path=client_credential_file
        )

        src = pathlib.Path(os.path.join(data_dir, 'default-id.ndjson'))
        enc_path = pathlib.Path(tempfile.mktemp())
        dec_path = pathlib.Path(tempfile.mktemp())
        client.encrypt(NdjsonFormat(), src, enc_path)
        client.decrypt(enc_path, dec_path)

        self.assertEqual(src.read_bytes(), dec_path.read_bytes())

    def test_encrypt_decrypt_block(self):
        client = Client(
            keystore_address=self.address, credential_path=client_credential_file
        )

        src = b'My test block data'
        dest = client.encrypt_block('1234', src)

        dec_data = client.decrypt_block(dest)
        self.assertEqual(src, dec_data)

    def test_create_keys_successfully(self):
        client = Client(
            keystore_address=self.address, credential_path=client_credential_file
        )
        client.create_keys(['ab', 'cd', 'ef'], id_format=IdFormat.HEX)

    def test_create_keys_fails_with_invalid_id_format(self):
        client = Client(
            keystore_address=self.address, credential_path=client_credential_file
        )

        with self.assertRaisesRegex(subprocess.CalledProcessError, ''):
            client.create_keys(['ghij'], id_format=IdFormat.HEX)

    def test_delete_keys_successfully(self):
        client = Client(
            keystore_address=self.address, credential_path=client_credential_file
        )
        client.delete_keys(['ab', 'cd', 'ef'], id_format=IdFormat.HEX)

    def test_delete_keys_fails_with_invalid_id_format(self):
        client = Client(
            keystore_address=self.address, credential_path=client_credential_file
        )

        with self.assertRaisesRegex(subprocess.CalledProcessError, ''):
            client.create_keys(['ghij'], id_format=IdFormat.HEX)


if __name__ == '__main__':
    unittest.main()
