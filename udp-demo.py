
import socket
import time
import vision_detection_pb2
import zss_debug_pb2
import zss_cmd_pb2

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("0.0.0.0", 23333))

while True:
    data, addr = s.recvfrom(0xFFFF)
    frame = vision_detection_pb2.Vision_DetectionFrame()
    frame.ParseFromString(data)
    x = frame.robots_blue[0].x
    y = frame.robots_blue[0].y

    Msgs = zss_debug_pb2.Debug_Msgs()
    msg = Msgs.msgs.add()
    msg.type = zss_debug_pb2.Debug_Msg.Debug_Type.ARC
    msg.color = zss_debug_pb2.Debug_Msg.Color.RED

    arc = msg.arc
    rec = arc.rectangle
    point1 = rec.point1
    point2 = rec.point2
    point1.x = (x/10-30)
    point1.y = (y/10-30)
    point2.x = (x/10+30)
    point2.y = (y/10+30)
    arc.start = 0
    arc.end = 360
    arc.FILL = True
    s.sendto(Msgs.SerializeToString(), ("127.0.0.1", 20001))
