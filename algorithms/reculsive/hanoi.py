# 하노이의 탑 게임 아시나요? 이 게임의 목표는 왼쪽 기둥에 있는 원판들을 모두 오른쪽 기둥으로 옮기는 것입니다. 지켜야할 규칙은 두가지입니다:
#
# 한 번에 하나의 원판만 옮길 수 있다.
# 큰 원판이 작은 원판 위에 있어서는 안 된다.


# 하노이의 탑 게임의 해답을 출력해주는 함수 hanoi를 쓰세요.
# hanoi는 파라미터로 원판 수 num_disks, 게임을 시작하는 기둥 번호 start_peg,
# 그리고 목표로 하는 기둥 번호 end_peg를 받고, 재귀적으로 문제를 풀어 원판을 옮기는 순서를 모두 출력합니다.


def move_disk(disk_num, start_peg, end_peg):
    print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))

def hanoi(num_disks, start_peg, end_peg):
    if num_disks==1:
        return move_disk(1, start_peg, end_peg)
    # 코드를 입력하세요.
    hanoi(num_disks-1, start_peg, 6-start_peg-end_peg)
    move_disk(num_disks, start_peg, end_peg)
    hanoi(num_disks-1, 6-start_peg-end_peg, end_peg)


# 테스트 코드 (포함하여 제출해주세요)
hanoi(3, 1, 3)

# hanoi(2, 1, 2)
# -> hanoi(1, 1, 2) # 1개를 1에서 2로 이동
# -> move_disk(2, 1, 3) # 2번을 1에서 3로 이동
# -> hanoi(1, 3, 2) # 1개를 3에서 2로 이동
# -> 지금 1, 2번이 순서대로 2번으로 가있는 상태
#
# move_disk(3, 1, 3) # 3번을 1에서 3으로 이동
#
# hanoi(2, 2, 3)
# -> hanoi(1, 2, 1) # 1개를 2번에서 1번으로 이동
# -> move_disk(2, 2, 3) # 2번을 2번에서 3번으로 이동
# -> hanoi(1, 1, 3) # 1번을 1번에서 3번으로 이동