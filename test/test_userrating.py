import six
import unittest

from beets.library import Item

from test.helper import TestHelper

from beetsplug.userrating import UserRatingsPlugin


class UserRatingsPluginTest(TestHelper, unittest.TestCase):

    def setUp(self):
        self.setup_beets()

        try:
            self.load_plugins('userrating')
        except Exception:
            import sys
            # store exception info so an error in teardown does not swallow it
            exc_info = sys.exc_info()
            try:
                self.teardown_beets()
                self.unload_plugins()
            except Exception:
                # if load_plugins() failed then setup is incomplete and
                # teardown operations may fail. In particular # {Item,Album}
                # may not have the _original_types attribute in unload_plugins
                pass
            six.reraise(exc_info[1], None, exc_info[2])

        self.album_mp3 = self.add_album_fixture(1, ext='mp3')
        for item in self.album_mp3.items():
            self._reset_userrating(item)

        self.album_wma = self.add_album_fixture(1, ext='wma')
        for item in self.album_wma.items():
            self._reset_userrating(item)

        self.album_flac = self.add_album_fixture(1, ext='flac')
        for item in self.album_flac.items():
            self._reset_userrating(item)

        albums = self.lib.albums()
        items = self.lib.items()
        self.assertEqual(3, len(albums))
        self.assertEqual(3, len(items))

    def tearDown(self):
        self.teardown_beets()
        self.unload_plugins()

    @staticmethod
    def _reset_userrating(item, value=None):
        item['userrating'] = value
        item.write()
        item.store()

    def test_cli_rating_list_without_rating(self):
        for item in self.lib.items():
            self.assertNotIn('userrating', item, '%s is not rated' % item.path)
        self.run_command('userrating')

    def test_cli_rating_update_without_rating(self):
        for item in self.lib.items():
            self.assertNotIn('userrating', item, '%s is not rated' % item.path)
        self.run_command('userrating', '-u', '1')
        for item in self.lib.items():
            self.assertIn('userrating', item, '%s is not rated' % item.path)
            self.assertEqual(item.userrating, 1)

    def test_cli_rating_update_with_rating(self):
        for item in self.lib.items():
            self.assertNotIn('userrating', item, '%s is not rated' % item.path)
        self.run_command('userrating', '-u', '1')

        self.run_command('userrating', '-u', '2')
        for item in self.lib.items():
            self.assertIn('userrating', item, '%s is not rated' % item.path)
            self.assertEqual(item.userrating, 1)

        self.run_command('userrating', '-u', '2', '-o')
        for item in self.lib.items():
            self.assertIn('userrating', item, '%s is not rated' % item.path)
            self.assertEqual(item.userrating, 2)

    def test_cli_rating_list_with_rating(self):
        for item in self.lib.items():
            self._reset_userrating(item, 1)
        for item in self.lib.items():
            self.assertIn('userrating', item, '%s is not rated' % item.path)
        self.run_command('userrating')


def suite():
    return unittest.TestLoader().loadTestsFromName(__name__)


if __name__ == '__main__':
    unittest.main(defaultTest='suite')
