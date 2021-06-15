# 패키지 안 함수 실행
# 1
# import game.sound.echo
# game.sound.echo.echo_test()
# 2
# from game.sound import echo
# echo.echo_test()
# 3
# from game.sound.echo import echo_test
# echo_test()
def echo_test():
    print("echo")