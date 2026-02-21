# https://www.matiji.net/exam/brushquestion/20/3846/4C6668FEB8CFD6520DE73B365B31D1A4


def main():
    def distribute_tasks(t, k, task_times):

        # 判断是否能以 max_time 为上限分配任务给 k 个组员
        def can_distribute(max_time):
            groups, current_sum = 1, 0  # 当前组员，当前任务总时间为0
            for time in task_times:
                if current_sum + time > max_time:
                    groups += 1
                    current_sum = time
                    if groups > k:
                        return False
                else:
                    current_sum += time
            return True

        # 二分查找最小的最大工作量
        left, right = max(task_times), sum(task_times)
        while left < right:
            mid = (left + right) // 2
            if can_distribute(mid):
                right = mid  # 尝试更小的最大工作量
            else:
                left = mid + 1

        max_time = left  # 找到的最小的最大工作量

        # 根据 max_time 进行任务分配
        result = [[0, 0] for _ in range(k)]  # 记录每个组员的任务区间
        current_sum, start_task = 0, t
        group = k-1

        # 从后往前分配任务，尽量让后面的组员承担任务
        for i in range(t,0,-1):
            if group < 0:
                break
            if current_sum + task_times[i-1] > max_time:
                result[group] = [i+1, start_task]  # 给当前组员分配任务
                group -= 1
                current_sum = 0
                start_task = i
            current_sum += task_times[i-1]

        # 给最后一个组员分配剩余的任务
        if group >= 0:
            result[group] = [1,start_task]


        return result

    # 输入
    t, k = map(int, input().split())
    task_times = list(map(int, input().split()))

    # 任务分配
    result = distribute_tasks(t, k, task_times)

    # 输出
    for start, end in result:
        print(start, end)




if __name__ == '__main__':
    main()