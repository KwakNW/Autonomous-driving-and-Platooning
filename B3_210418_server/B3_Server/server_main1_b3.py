# -*- coding: utf-8 -*-
import server_socket_b3
import server_video_b3
import threading


if __name__ == '__main__':
    # host, port
    host, port= '141.223.140.21', 10250 #client1 포트  # ipconfig를 통해 ip확인 가능, 13기 파이팅 ^~^
    print("서버 시작")

    client = server_socket_b3.Server(host, port)

    # loop
    video_object = server_video_b3.VideoStreaming(client.Get_Client())
    video_object.streaming()

    #멀티스레싱
    # video_object = server_video_b3.VideoStreaming(client.Get_Client())
    # video_object_thread=threading.Thread(target=video_object.streaming, arg=())
    # video_object_thread.start()
    #
    # video_object2 = server_video_b3.VideoStreaming(client2.Get_Client())
    # video_object2_thread=threading.Thread(target=video_object2.streaming, arg=())
    # video_object2_thread.start()

    # 멀티프로세싱
    # video_object = server_video_b3.VideoStreaming(client.Get_Client())
    # video_object_thread=threading.Thread(target=video_object.streaming, arg=())
    # video_object_thread.start()
    #
    # video_object2 = server_video_b3.VideoStreaming(client2.Get_Client())
    # video_object2_thread=threading.Thread(target=video_object2.streaming, arg=())
    # video_object2_thread.start()