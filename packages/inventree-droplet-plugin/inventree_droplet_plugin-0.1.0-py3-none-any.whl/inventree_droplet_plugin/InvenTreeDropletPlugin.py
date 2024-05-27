"""Surface Droplet info in InvenTree."""

import subprocess

from plugin import InvenTreePlugin
from plugin.mixins import SettingsContentMixin


class InvenTreeDropletPlugin(SettingsContentMixin, InvenTreePlugin):
    """Surface Droplet info in InvenTree."""

    NAME = 'InvenTreeDropletPlugin'
    SLUG = 'inventree_droplet_plugin'
    TITLE = "Droplet Info"
    MIN_VERSION = "0.13.0"

    def get_settings_content(self, request):
        """Get custom settings content for the plugin."""
        # Check apt for last update check
        try:
            last_update_check = subprocess.check_output('stat -c %y /var/lib/apt/periodic/update-success-stamp'.split())
        except subprocess.CalledProcessError as e:
            if e.returncode == 1:
                last_update_check = "Never"
            else:
                last_update_check = "Error getting last update check time"

        return f"""<p>Last apt-update check: {last_update_check}.<br>You should update your droplet regularly by running "apt update && apt upgrade" in your console.</p>"""
