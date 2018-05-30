# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy
# of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import itertools

import discovery.conf.api
import discovery.conf.default

_default_opt_lists = [
    discovery.conf.default.api_opts,
    discovery.conf.default.exc_log_opts,
    discovery.conf.default.path_opts,
    discovery.conf.default.service_opts,
    discovery.conf.default.utils_opts,
]

_opts = [
    ('DEFAULT', itertools.chain(*_default_opt_lists)),
    ('api', discovery.conf.api.opts),
]


def list_opts():
    """Return a list of oslo.config options available in Discovery code.

    The returned list includes all oslo.config options. Each element of
    the list is a tuple. The first element is the name of the group, the
    second element is the options.

    The function is discoverable via the 'mogan' entry point under the
    'oslo.config.opts' namespace.

    The function is used by Oslo sample config file generator to discover the
    options.

    :returns: a list of (group, options) tuples
    """
    return _opts
