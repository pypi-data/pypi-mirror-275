# Copyright 2024 Davide Gessa

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

# http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import time


def repeat_until_done(f, n_iterations=10, wait_time=5):
    try:
        return f()
    except Exception as e:
        print(e)
        print(f"Function call failed, retrying in {wait_time} seconds ({n_iterations})")
        time.sleep(wait_time)
        return repeat_until_done(f, n_iterations - 1, wait_time)


class Blockchain:
    """Abstract blockchain provider"""

    def __init__(self, uri):
        pass

    def connect(self):
        raise Exception("Abstract: blockchain.connect")

    def contract_call(self, call_name, params):
        raise Exception("Abstract: blockchain.contract_call")

    def get_number_of_jobs(self) -> int:
        raise Exception("Abstract: blockchain.get_number_of_jobs")

    def get_jobs(self, from_index, limit):
        raise Exception("Abstract: blockchain.get_number_of_jobs")

    def get_jobs_paginated(self, from_index=0, to_index=None, limit=50, reverse=False):
        n = self.get_number_of_jobs() if to_index is None else to_index
        i = from_index
        js = []

        while i < n:
            js += self.get_jobs(from_index=i, limit=50)
            i += limit

        return js if not reverse else js[::-1]

    def get_all_jobs(self, reverse=False):
        return self.get_jobs_paginated(reverse=reverse)
