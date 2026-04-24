"""
测试 scope 参数：class
"""
def test_ehlo(smtp_connection_class):
    """
    EHLO 是客户端连接 SMTP 服务器后发送的第一条指令，用于自我介绍并询问服务器支持哪些功能。
    :param smtp_connection_class:
    :return:
    """
    response, msg = smtp_connection_class.ehlo()  # 向服务器发送指令
    assert response == 250  # 250: SMTP 的标准成功状态码，响应成功
    assert b"smtp.gmail.com" in msg
    # assert 0    # 强制测试失败


def test_noop(smtp_connection_class):
    """
    NOOP (No Operation) 是一条简单的心跳指令，用来检查连接是否依然存活，服务器通常只回复一个 “OK”
    :param smtp_connection_class:
    :return:
    """
    response, msg = smtp_connection_class.noop()  # 发送心跳指令
    assert response == 250
    # assert 0