# Copyright [2010] [Anso Labs, LLC]
# 
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
# 
#        http://www.apache.org/licenses/LICENSE-2.0
# 
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

from nova import flags

FLAGS = flags.FLAGS

FLAGS.fake_libvirt = False
FLAGS.fake_storage = False
FLAGS.fake_rabbit = False
FLAGS.fake_network = False
FLAGS.fake_users = False
FLAGS.verbose = False
