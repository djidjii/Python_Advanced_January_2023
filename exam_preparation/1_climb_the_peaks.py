from collections import deque


def climb_the_peaks_func(food_portions, stamina):
    food_portions, stamina = deque(food_portions), deque(stamina)
    mountain_peaks_data = {'Vihren': 80, 'Kutelo': 90, 'Banski Suhodol': 100, 'Polezhan': 60, 'Kamenitza': 70}
    conquered_peaks = []
    failed_condition = False

    for peak_name, difficult in mountain_peaks_data.items():
        while True:
            daily_sum_of_elements = food_portions.pop() + stamina.popleft()

            if daily_sum_of_elements >= difficult:
                conquered_peaks.append(peak_name)
                break
            elif len(food_portions) == 0 or len(stamina) == 0:
                failed_condition = True
                break

        if failed_condition:
            if len(conquered_peaks) == 0:
                return f'Alex failed! He has to organize his journey better next time -> @PIRINWINS'
            else:
                data_representation = '\n'.join(conquered_peaks)
                return f'Alex failed! He has to organize his journey better next time -> @PIRINWINS\nConquered peaks:\n{data_representation}'

    data_representation = '\n'.join(conquered_peaks)
    return f"Alex failed! He has to organize his journey better next time -> @PIRINWINS"


food = list(map(int, input().split(', ')))
stamina = list(map(int, input().split(', ')))
print(climb_the_peaks_func(food, stamina))
