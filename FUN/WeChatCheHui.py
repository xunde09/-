#coding=utf8
import itchat
import requests
import time
import os
import re
import threading

#全局变量,对于每个用户的机器人开关
User_bot_control_flag = {}
#全局变量,我的昵称
myNickName = ''

def bot_chat_init():
    # 获取好友列表
    friends = itchat.get_friends(update=True)[0:]
    #将标志位置为0
    for i in friends[1:]:
        User_bot_control_flag[i["UserName"]] = 0


@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
   #   获取到发送消息者身份,如果身份匹配,就做对应的事
   # itchat.send_msg('已经收到了文本消息，消息内容为%s' % msg['Text'], toUserName=msg['FromUserName'])
    # 如果图灵Key出现问题，那么reply将会是None
    if msg['Text']=='彭芊芊是谁':
        return u'彭芊芊是一个超级大瓜皮'
    if msg['Text'] == '郑勇军是谁':
        return u'郑勇军是帅哥'
    reply = get_response(msg['Text'])
    if not msg['FromUserName'] == myUserName:
        pass
        # 发送一条提示给文件助手
        # itchat.send_msg(u"[%s]收到好友@%s 的信息：%s\n" %
        #                 (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(msg['CreateTime'])),
        #                  msg['User']['NickName'],
        #                  msg['Text']), 'filehelper')
    # a or b的意思是，如果a有内容，那么返回a，否则返回b
    # 有内容一般就是指非空或者非None，你可以用`if a: print('True')`来测试
    return reply or u'[自动回复]您好，我现在有事不在，一会再和您联系。\n已经收到您的的信息：%s\n' % (msg['Text'])


def friend():
    # 初始化计数器，有男有女，当然，有些人是不填的
    # 获取好友列表
    friends = itchat.get_friends(update=True)[0:]
    male = female = other = 0

    # 遍历这个列表，列表里第一位是自己，所以从"自己"之后开始计算
    # 1表示男性，2女性
    for i in friends[1:]:
        print (i)           #打印出签名
        sex = i["Sex"]
        if sex == 1:
            male += 1
        elif sex == 2:
            female += 1
        else:
            other += 1
    # 总数算上，好计算比例啊～
    total = len(friends[1:])
    # 好了，打印结果
    print(u"共有好友：%d" % total)
    print (u"男性好友：%.2f%%" % (float(male) / total * 100))
    print (u"女性好友：%.2f%%" % (float(female) / total * 100))
    print (u"其他：%.2f%%" % (float(other) / total * 100))

def get_response(msg):
    # 这里我们就像在“3. 实现最简单的与图灵机器人的交互”中做的一样
    # 构造了要发送给服务器的数据
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : key,
        'info'   : msg,
        'userid' : 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        # 字典的get方法在字典没有'text'值的时候会返回None而不会抛出异常
        return r.get('text')+'----来自机器人小Z的智能回复----'
    # 为了防止服务器没有正常响应导致程序异常退出，这里用try-except捕获了异常
    # 如果服务器没能正常交互（返回非json或无法连接），那么就会进入下面的return
    except:
        # 将会返回一个None
        return


@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)  #msg['ActualNickName'] 群里发消息的人名 #msg['User']['NickName'] 群名称
def text_reply(msg):
    # print (msg['User'])       #一个宏大的结构体
    # print ("群聊名字"+msg['User']['NickName'])  #群聊名称
    # print (msg['FromUserName'])
    #监控所有群的消息,后来做统计用,后面可以做关键词分析什么的
    file_object = open(myNickName+"群"+msg['User']['NickName'], 'a')
    write_data = ''.join(time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime(msg['CreateTime'])))+" "+msg['ActualNickName']+": "+msg['Text']+"\n"
    file_object.write(write_data)
    file_object.close()
    #指定群聊可以智能群聊
    if  msg['User']['NickName'] == '184':
        print (" 184 ok")
        itchat.send(get_response(msg['Text']),msg['FromUserName'])
    #监控群聊内容发送到文件助手,已经被自己屏蔽掉了
    # itchat.send_msg(u"[%s]收到%s群 %s 的信息：%s\n" %
    #                 (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(msg['CreateTime']))
    #                  ,msg['User']['NickName'],msg['ActualNickName'],
    #                  msg['Text']), 'filehelper')
    # 判断是否有人@自己
    if (msg.isAt):
     # 如果有人@自己，就发一个消息告诉对方我已经收到了信息
        itchat.send_msg("我已经收到了来自{0}的消息，实际内容为{1}".format(msg['ActualNickName'], msg['Text']),
            toUserName=msg['FromUserName'])

# def sendmsgToPsh():
#      while (True):
#         pass
#          # print ("123456")
#
# threads = []
# t1 = threading.Thread(target=sendmsgToPsh())


# 说明：可以撤回的有文本文字、语音、视频、图片、位置、名片、分享、附件

# {msg_id:(msg_from,msg_to,msg_time,msg_time_rec,msg_type,msg_content,msg_share_url)}
msg_dict = {}

# 文件存储临时目录
rev_tmp_dir = "C:/Users/Administrator/Desktop/WorkSpider/FUN"
if not os.path.exists(rev_tmp_dir): os.mkdir(rev_tmp_dir)

# 表情有一个问题 | 接受信息和接受note的msg_id不一致 巧合解决方案
face_bug = None


# # 将接收到的消息存放在字典中，当接收到新消息时对字典中超时的消息进行清理 | 不接受不具有撤回功能的信息
# # [TEXT, PICTURE, MAP, CARD, SHARING, RECORDING, ATTACHMENT, VIDEO, FRIENDS, NOTE]
# @itchat.msg_register([itchat.content.TEXT, itchat.content.PICTURE, itchat.content.MAP, itchat.content.CARD, itchat.content.SHARING,
#                       itchat.content.RECORDING,itchat.content. ATTACHMENT, itchat.content.VIDEO],isGroupChat=True)
# def handler_receive_msg(msg):
#     #回复特定用户消息
#     # if msg['User']['NickName']=='YYYYY' or msg['User']['NickName']=='彭芊芊':
#     #     print ("yhj ok")
#     #     itchat.send_msg(get_response(msg['Text']), toUserName=msg['FromUserName'])
#     # 先获取对方说来的话
#     # 下面一行是获取发送消息者昵称
#     send_user_name = itchat.search_friends(userName=msg['FromUserName'])['NickName']
#     file_object = open(myNickName + "&" + msg['User']['NickName'], 'a')
#     write_data = ''.join(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(msg['CreateTime']))) + " " + \
#                  send_user_name + ": " + msg['Text'] + "\n"
#     file_object.write(write_data)
#     file_object.close()
#
#     #控制指令检测模块
#     if msg['Text'] == 'service robot start':
#         User_bot_control_flag[msg['FromUserName']]=1      #检测到开启指令后开启机器人
#         itchat.send_msg("Robot small Z started...waiting for your service", toUserName=msg['FromUserName'])
#     if msg['Text'] == 'service robot stop':
#         User_bot_control_flag[msg['FromUserName']]=0      #检测到开启指令后关闭机器人
#         itchat.send_msg("Robot small Z stoped...get 'service robot start' restarted", toUserName=msg['FromUserName'])
#     #在开关开启的情况下回复对方对话
#     if not msg['FromUserName'] == myUserName:
#         if User_bot_control_flag[msg['FromUserName']]:
#             # 存储单人对话模块
#             # 下面一行是获取发送消息者昵称
#             reply = get_response(msg['Text'])
#             file_object = open(myNickName + "&" + msg['User']['NickName'], 'a')
#             write_data = ''.join(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(msg['CreateTime']))) + " " + \
#                          myNickName + ": " + reply + "\n"
#             file_object.write(write_data)
#             file_object.close()
#             itchat.send_msg(reply, toUserName=msg['FromUserName'])
#
#     global face_bug
#     # 获取的是本地时间戳并格式化本地时间戳 e: 2017-04-21 21:30:08
#     msg_time_rec = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#     # 消息ID
#     msg_id = msg['MsgId']
#     # 消息时间
#     msg_time = msg['CreateTime']
#     # 消息发送人昵称 | 这里也可以使用RemarkName备注　但是自己或者没有备注的人为None
#     msg_from = (itchat.search_friends(userName=msg['FromUserName']))["NickName"]
#     # 消息内容
#     msg_content = None
#     # 分享的链接
#     msg_share_url = None
#     if msg['Type'] == 'Text' \
#             or msg['Type'] == 'Friends':
#         msg_content = msg['Text']
#     elif msg['Type'] == 'Recording' \
#             or msg['Type'] == 'Attachment' \
#             or msg['Type'] == 'Video' \
#             or msg['Type'] == 'Picture':
#         msg_content = r"" + msg['FileName']
#         # 保存文件
#         msg['Text'](rev_tmp_dir + msg['FileName'])
#     elif msg['Type'] == 'Card':
#         msg_content = msg['RecommendInfo']['NickName'] + r" 的名片"
#     elif msg['Type'] == 'Map':
#         x, y, location = re.search(
#             "<location x=\"(.*?)\" y=\"(.*?)\".*label=\"(.*?)\".*", msg['OriContent']).group(1, 2, 3)
#         if location is None:
#             msg_content = r"纬度->" + x.__str__() + " 经度->" + y.__str__()
#         else:
#             msg_content = r"" + location
#     elif msg['Type'] == 'Sharing':
#         msg_content = msg['Text']
#         msg_share_url = msg['Url']
#     face_bug = msg_content
#     # 更新字典
#     msg_dict.update(
#         {
#             msg_id: {
#                 "msg_from": msg_from, "msg_time": msg_time, "msg_time_rec": msg_time_rec,
#                 "msg_type": msg["Type"],
#                 "msg_content": msg_content, "msg_share_url": msg_share_url
#             }
#         }
#     )

# 将接收到的消息存放在字典中，当接收到新消息时对字典中超时的消息进行清理 | 不接受不具有撤回功能的信息
# [TEXT, PICTURE, MAP, CARD, SHARING, RECORDING, ATTACHMENT, VIDEO, FRIENDS, NOTE]
@itchat.msg_register([itchat.content.TEXT, itchat.content.PICTURE, itchat.content.MAP, itchat.content.CARD, itchat.content.SHARING,
                      itchat.content.RECORDING,itchat.content. ATTACHMENT, itchat.content.VIDEO])
def handler_receive_msg(msg):
    #回复特定用户消息
    # if msg['User']['NickName']=='YYYYY' or msg['User']['NickName']=='彭芊芊':
    #     print ("yhj ok")
    #     itchat.send_msg(get_response(msg['Text']), toUserName=msg['FromUserName'])
    # 先获取对方说来的话
    # 下面一行是获取发送消息者昵称
    send_user_name = itchat.search_friends(userName=msg['FromUserName'])['NickName']
    file_object = open(myNickName + "&" + msg['User']['NickName'], 'a')
    write_data = ''.join(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(msg['CreateTime']))) + " " + \
                 send_user_name + ": " + msg['Text'] + "\n"
    file_object.write(write_data)
    file_object.close()

    #控制指令检测模块
    if msg['Text'] == 'service robot start':
        User_bot_control_flag[msg['FromUserName']]=1      #检测到开启指令后开启机器人
        itchat.send_msg("Robot small Z started...waiting for your service", toUserName=msg['FromUserName'])
    if msg['Text'] == 'service robot stop':
        User_bot_control_flag[msg['FromUserName']]=0      #检测到开启指令后关闭机器人
        itchat.send_msg("Robot small Z stoped...get 'service robot start' restarted", toUserName=msg['FromUserName'])
    #在开关开启的情况下回复对方对话
    if not msg['FromUserName'] == myUserName:
        if User_bot_control_flag[msg['FromUserName']]:
            # 存储单人对话模块
            # 下面一行是获取发送消息者昵称
            reply = get_response(msg['Text'])
            file_object = open(myNickName + "&" + msg['User']['NickName'], 'a')
            write_data = ''.join(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(msg['CreateTime']))) + " " + \
                         myNickName + ": " + reply + "\n"
            file_object.write(write_data)
            file_object.close()
            itchat.send_msg(reply, toUserName=msg['FromUserName'])

    global face_bug
    # 获取的是本地时间戳并格式化本地时间戳 e: 2017-04-21 21:30:08
    msg_time_rec = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # 消息ID
    msg_id = msg['MsgId']
    # 消息时间
    msg_time = msg['CreateTime']
    # 消息发送人昵称 | 这里也可以使用RemarkName备注　但是自己或者没有备注的人为None
    msg_from = (itchat.search_friends(userName=msg['FromUserName']))["NickName"]
    # 消息内容
    msg_content = None
    # 分享的链接
    msg_share_url = None
    if msg['Type'] == 'Text' \
            or msg['Type'] == 'Friends':
        msg_content = msg['Text']
    elif msg['Type'] == 'Recording' \
            or msg['Type'] == 'Attachment' \
            or msg['Type'] == 'Video' \
            or msg['Type'] == 'Picture':
        msg_content = r"" + msg['FileName']
        # 保存文件
        msg['Text'](rev_tmp_dir + msg['FileName'])
    elif msg['Type'] == 'Card':
        msg_content = msg['RecommendInfo']['NickName'] + r" 的名片"
    elif msg['Type'] == 'Map':
        x, y, location = re.search(
            "<location x=\"(.*?)\" y=\"(.*?)\".*label=\"(.*?)\".*", msg['OriContent']).group(1, 2, 3)
        if location is None:
            msg_content = r"纬度->" + x.__str__() + " 经度->" + y.__str__()
        else:
            msg_content = r"" + location
    elif msg['Type'] == 'Sharing':
        msg_content = msg['Text']
        msg_share_url = msg['Url']
    face_bug = msg_content
    # 更新字典
    msg_dict.update(
        {
            msg_id: {
                "msg_from": msg_from, "msg_time": msg_time, "msg_time_rec": msg_time_rec,
                "msg_type": msg["Type"],
                "msg_content": msg_content, "msg_share_url": msg_share_url
            }
        }
    )


# # 收到note通知类消息，判断是不是撤回并进行相应操作,针对于群
# @itchat.msg_register([itchat.content.NOTE],isGroupChat=True)
# def send_msg_helper(msg):
#     global face_bug
#     if re.search(r"\<\!\[CDATA\[.*撤回了一条消息\]\]\>", msg['Content']) is not None:
#         # 获取消息的id
#         old_msg_id = re.search("\<msgid\>(.*?)\<\/msgid\>", msg['Content']).group(1)
#         old_msg = msg_dict.get(old_msg_id, {})
#         if len(old_msg_id) < 11:
#             itchat.send_file(rev_tmp_dir + face_bug, toUserName='filehelper')
#             os.remove(rev_tmp_dir + face_bug)
#         else:
#             msg_body = "告诉你一个秘密~" + "\n" \
#                        + old_msg.get('msg_from') + " 撤回了 " + old_msg.get("msg_type") + " 消息" + "\n" \
#                        + old_msg.get('msg_time_rec') + "\n" \
#                        + "撤回了什么 ⇣" + "\n" \
#                        + r"" + old_msg.get('msg_content')
#             # 如果是分享存在链接
#             if old_msg['msg_type'] == "Sharing": msg_body += "\n就是这个链接➣ " + old_msg.get('msg_share_url')
#
#             # 将撤回消息发送到文件助手
#             itchat.send(msg_body, toUserName='filehelper')
#             # 有文件的话也要将文件发送回去
#             if old_msg["msg_type"] == "Picture" \
#                     or old_msg["msg_type"] == "Recording" \
#                     or old_msg["msg_type"] == "Video" \
#                     or old_msg["msg_type"] == "Attachment":
#                 file = '@fil@%s' % (rev_tmp_dir + old_msg['msg_content'])
#                 itchat.send(msg=file, toUserName='filehelper')
#                 os.remove(rev_tmp_dir + old_msg['msg_content'])
#             # 删除字典旧消息
#             msg_dict.pop(old_msg_id)

# 收到note通知类消息，判断是不是撤回并进行相应操作
@itchat.msg_register([itchat.content.NOTE])
def send_msg_helper(msg):
    global face_bug
    if re.search(r"\<\!\[CDATA\[.*撤回了一条消息\]\]\>", msg['Content']) is not None:
        # 获取消息的id
        old_msg_id = re.search("\<msgid\>(.*?)\<\/msgid\>", msg['Content']).group(1)
        old_msg = msg_dict.get(old_msg_id, {})
        if len(old_msg_id) < 11:
            itchat.send_file(rev_tmp_dir + face_bug, toUserName='filehelper')
            os.remove(rev_tmp_dir + face_bug)
        else:
            msg_body = "告诉你一个秘密~" + "\n" \
                       + old_msg.get('msg_from') + " 撤回了 " + old_msg.get("msg_type") + " 消息" + "\n" \
                       + old_msg.get('msg_time_rec') + "\n" \
                       + "撤回了什么 ⇣" + "\n" \
                       + r"" + old_msg.get('msg_content')
            # 如果是分享存在链接
            if old_msg['msg_type'] == "Sharing": msg_body += "\n就是这个链接➣ " + old_msg.get('msg_share_url')

            # 将撤回消息发送到文件助手
            itchat.send(msg_body, toUserName='filehelper')
            # 有文件的话也要将文件发送回去
            if old_msg["msg_type"] == "Picture" \
                    or old_msg["msg_type"] == "Recording" \
                    or old_msg["msg_type"] == "Video" \
                    or old_msg["msg_type"] == "Attachment":
                file = '@fil@%s' % (rev_tmp_dir + old_msg['msg_content'])
                itchat.send(msg=file, toUserName='filehelper')
                os.remove(rev_tmp_dir + old_msg['msg_content'])
            # 删除字典旧消息
            msg_dict.pop(old_msg_id)




key = '02dd1dd1b5594e179aa4aca9a6a690a6'
if __name__ == '__main__':
    itchat.auto_login(hotReload=True)
    # 获取自己的UserName
    myNickName = itchat.get_friends(update=True)[0]["NickName"]
    myUserName = itchat.get_friends(update=True)[0]["UserName"]
    #做函数功能的实验
   # print (itchat.search_friends(name='彭芊芊')[0]['UserName'])
   # print(type(itchat.search_friends(name='彭芊芊')))
    #itchat.send("init messages to dindsong,A message from bangbangtang,distant areas...", toUserName='@509f2668d9380a6aeb1951585256827dc1d475c2de885b62fae401401d522f9b')
    friend()          #获取朋友信息

    bot_chat_init()    #初始化开关模块
    itchat.run()
