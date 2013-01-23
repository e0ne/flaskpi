# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2013 Ivan Kolodyazhny.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.


from flask.ext import script

import commands

if __name__ == "__main__":
    from main import app_factory
    import config

    manager = script.Manager(app_factory)
    manager.add_option("-c", "--config",
                       dest="config",
                       required=False,
                       default=config.Dev)
    manager.add_command("test", commands.Test())
    manager.run()
