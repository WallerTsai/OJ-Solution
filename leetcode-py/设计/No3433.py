import re
from typing import List


class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        events.sort(key=lambda x: (int(x[1]), -ord(x[0][0])))

        ans = [0] * numberOfUsers
        online_timestamp = [0] * numberOfUsers
        for action, timestamp, mention in events:
            cur_time = int(timestamp)

            if action == "OFFLINE":
                online_timestamp[int(mention)] = cur_time + 60
                continue

            if mention == "ALL":
                for i in range(numberOfUsers):
                    ans[i] += 1
            elif mention == "HERE":
                for i, t in enumerate(online_timestamp):
                    if t <= cur_time:
                        ans[i] += 1
            else:
                for ch_int in re.findall(r'\d+', mention):
                    ans[int(ch_int)] += 1
        
        return ans  # 53ms



